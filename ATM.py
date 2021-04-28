class ATM:
    def __init__(self,cardNumber,PIN):
        self.cardNumber=cardNumber
        self.PIN=PIN
    def Balance_Inquire (self):
        print("your balance is *insert number here*")
    def withdrawl(self,amount):
        newAmount=(7*10^67)-amount
        print("amount withdraw",str(newAmount))
def main():
    cardnumber=input("Insert Card")
    pinNumber=input("insertPin")
    newUser=ATM(cardnumber,pinNumber)
    print("choose an activity, 1.Balance Inquire, 2.WithDraw")
    activity=int(input("Enter Activity Number"))
    if (activity==1):
        newUser.Balance_Inquire()
    elif(activity==2):
        amount=int(input("Enter the Amount"))
        newUser.withdrawl(amount)
    else:
        print("Enter Valid Pin Number")
if __name__=="__main__":
    main()