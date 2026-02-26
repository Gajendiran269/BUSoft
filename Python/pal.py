str1 = "mmamm"
l = 0
r = len(str1)-1
pal = False
while(l<=r):
    if str1[l] != str1[r]:
        pal = False
        break
    else:
        pal = True
        l+=1
        r-=1
print("pal") if pal else print("not")