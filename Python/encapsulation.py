class Bank:
    def __init__(self,holder,balance):
        self.holder  = holder
        self.__balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance +=amount
    def withdraw(self,amount):
        if 0 < amount <=self.__balance:
            self.__balance -= amount
            print("withdraw Succesfull")
        else:
            print("No fund")
    def getbalance(self):
        return self.__balance
account = Bank("arun",1000)
account.withdraw(100)
print(account.getbalance())
