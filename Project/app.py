from flask import Flask, request, jsonify, render_template_string
import pandas as pd
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import random

app = Flask(__name__)

# ================= CONFIG =================

EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

# Thresholds
TEMP_LIMIT = 45
CURRENT_LIMIT = 1.2
VIB_LIMIT = 2.0
SOUND_LIMIT = 5  # seconds

# ===========================================

latest_data = {
    "temperature": 0,
    "current": 0,
    "vibration": 0,
    "sound_duration": 0,
    "status": "HEALTHY",
    "time": ""
}

alert_active = False

# ================= EMAIL FUNCTION =================

def send_email_alert(data):
    subject = "🚨 MACHINE CRITICAL ALERT"
    body = f"""
Machine Fault Detected!

Temperature: {data['temperature']} °C
Current: {data['current']} A
Vibration: {data['vibration']}
Sound Duration: {data['sound_duration']} sec
Time: {data['time']}

Immediate inspection required.
"""

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("📧 Email Sent")
    except Exception as e:
        print("Email Error:", e)

# ================= TELEGRAM FUNCTION =================

def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, data=data)
        print("📱 Telegram Sent")
    except:
        print("Telegram Error")

# ================= STATUS LOGIC =================

def get_status(temp, current, vib, sound_dur):
    if (temp > TEMP_LIMIT or
        current > CURRENT_LIMIT or
        vib > VIB_LIMIT or
        sound_dur > SOUND_LIMIT):
        return "CRITICAL"
    return "HEALTHY"

# ================= RECEIVE DATA =================

@app.route('/data', methods=['POST'])
def receive_data():
    global alert_active, latest_data

    data = request.json

    temperature = data['temperature']
    current = data['current']
    vibration = data['vibration']
    sound_duration = data['sound_duration']

    status = get_status(temperature, current, vibration, sound_duration)

    latest_data = {
        "temperature": temperature,
        "current": current,
        "vibration": vibration,
        "sound_duration": sound_duration,
        "status": status,
        "time": datetime.now().strftime("%H:%M:%S")
    }

    # Save to CSV
    file_exists = os.path.isfile("data_log.csv")
    df = pd.DataFrame([{
        "timestamp": datetime.now(),
        "temperature": temperature,
        "current": current,
        "vibration": vibration,
        "sound_duration": sound_duration,
        "status": status
    }])
    df.to_csv("data_log.csv", mode='a', header=not file_exists, index=False)

    # Alert Logic
    if status == "CRITICAL" and not alert_active:
        send_email_alert(latest_data)
        send_telegram(
            f"🚨 MACHINE ALERT!\n"
            f"Temp: {temperature}°C\n"
            f"Current: {current}A\n"
            f"Vibration: {vibration}\n"
            f"Sound: {sound_duration}s"
        )
        alert_active = True

    if status == "HEALTHY":
        alert_active = False

    return jsonify({"status": "received"})

# ================= SIMULATION =================

@app.route("/simulate")
def simulate():
    fake_data = {
        "temperature": round(random.uniform(30, 60), 2),
        "current": round(random.uniform(0.5, 1.5), 2),
        "vibration": round(random.uniform(0.5, 3.0), 2),
        "sound_duration": round(random.uniform(0, 7), 2)
    }

    with app.test_request_context(json=fake_data):
        receive_data()

    return jsonify({"simulation": "sent", "data": fake_data})

# ================= API =================

@app.route('/latest')
def latest():
    return jsonify(latest_data)

# ================= DASHBOARD =================

@app.route("/")
def dashboard():
    try:
        df = pd.read_csv("data_log.csv")
        graph_data = df.tail(20).to_dict(orient="records")
    except:
        graph_data = []

    return render_template_string(dashboard_template,
                                  graph_data=graph_data)

# ================= HTML TEMPLATE =================

dashboard_template = """
<!DOCTYPE html>
<html>
<head>
<title>Machine Monitoring</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
body { font-family: Arial; background:#f4f4f4; margin:20px; }
h1 { text-align:center; }
.grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}

.card {
    background:white;
    padding:12px;
    border-radius:10px;
    box-shadow:0 3px 8px rgba(0,0,0,0.1);
    text-align:center;
}

.value { font-size:20px; font-weight:bold; margin-bottom:8px; }
canvas { height:150px !important; }

.healthy { border-left:6px solid green; }
.critical { border-left:6px solid red; }
</style>
</head>

<body>

<h1>⚙ Machine Condition Monitoring</h1>

<div class="grid">
<div class="card" id="tempCard">
<h3>🌡 Temperature</h3>
<div class="value" id="temp">0 °C</div>
<canvas id="tempChart"></canvas>
</div>

<div class="card" id="currentCard">
<h3>⚡ Current</h3>
<div class="value" id="current">0 A</div>
<canvas id="currentChart"></canvas>
</div>

<div class="card" id="vibCard">
<h3>📳 Vibration</h3>
<div class="value" id="vibration">0 m/s²</div>
<canvas id="vibChart"></canvas>
</div>

<div class="card" id="soundCard">
<h3>🔊 Sound Duration</h3>
<div class="value" id="sound">0 sec</div>
<canvas id="soundChart"></canvas>
</div>
</div>

<script>

let timeCounter = 0;

function createChart(id, label, color, unit) {
return new Chart(document.getElementById(id), {
type:'line',
data:{ labels:[], datasets:[{
label: label + " ("+unit+")",
data:[],
borderColor:color,
backgroundColor:color+"33",
fill:true,
tension:0.3
}]},
options:{
animation:false,
responsive:true,
scales:{
x:{ title:{display:true,text:"Time (sec)"} },
y:{ title:{display:true,text:label+" ("+unit+")"}, beginAtZero:true }
}
}
});
}

let tempChart = createChart("tempChart","Temperature","red","°C");
let currentChart = createChart("currentChart","Current","green","A");
let vibChart = createChart("vibChart","Vibration","blue","m/s²");
let soundChart = createChart("soundChart","Sound Duration","orange","sec");

setInterval(()=>{
fetch("/latest")
.then(res=>res.json())
.then(d=>{

timeCounter++;

document.getElementById("temp").innerText = d.temperature+" °C";
document.getElementById("current").innerText = d.current+" A";
document.getElementById("vibration").innerText = d.vibration+" m/s²";
document.getElementById("sound").innerText = d.sound_duration+" sec";

let cards=document.querySelectorAll(".card");
cards.forEach(c=>c.classList.remove("healthy","critical"));

if(d.status==="CRITICAL"){
cards.forEach(c=>c.classList.add("critical"));
document.body.style.background="#ffe5e5";
}else{
cards.forEach(c=>c.classList.add("healthy"));
document.body.style.background="#f4f4f4";
}

[tempChart,currentChart,vibChart,soundChart].forEach(chart=>{
chart.data.labels.push(timeCounter);
if(chart.data.labels.length>20){
chart.data.labels.shift();
chart.data.datasets[0].data.shift();
}
});

tempChart.data.datasets[0].data.push(d.temperature);
currentChart.data.datasets[0].data.push(d.current);
vibChart.data.datasets[0].data.push(d.vibration);
soundChart.data.datasets[0].data.push(d.sound_duration);

tempChart.update();
currentChart.update();
vibChart.update();
soundChart.update();

});
},1000);

</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)