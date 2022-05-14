class Atm(object):
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber = cardnumber
        self.pin = pin
    def check_balance(self):
        print("Your balance is 5000")
    def withdrawl(self,amount):
        new_amount = 5000-amount
        print("You withdrawed: ",+ str(amount) +, "Your remaining balance is: " + str(new_amount))

def main():
    card_number = input("insert your card number: ")
    pin_number = input("enter your pin number: ")

    new_user = Atm(card_number, pin_number)

    print("choose your activity")
    print("1.Balance Enquiry 2.withdrawl")
    activity = int(input("enter activity number:  "))

    if(activity ==1):
        new_user.check_balance()
    elif(activity ==2):
    else:
        print("Enter a vaild number")

if __name__=="__main__":
    main()