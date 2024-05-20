def ATM(index):
    u_password=input("Enter the password:")
    for i in range(3):
        if(u_password!=password[index]):
            if(i!=2):
                print("Password is incorrect! You have ",2-i,"attempts")
                u_password=input("Enter the password again:")
            else:
                print("Account is blocked. Please try after some time")
                exit()
    print("Password is correct")
    print("Press 1 for withdrawal")
    print("Press 2 for deposit")
    print("Press 3 for balance")
    print("Press 4 for Password change")
    ch=int(input("Enter your choice:"))
    # while(1):
    #     if(ch in [1,2,3,4]):
    #         pass
    #     else:
    #         ch=int(input("Re Enter your choice:"))
    if(ch==1):
        with_am=int(input("Enter the amount to be withdrawn: "))
        b=balance[index]
        if with_am>b:
            print("Insufficient Balance !!")
            exit()
        pin=int(input("Enter your pin:"))
        if(pin!=pins[index]):
            print("Invalid pin")
            print("END")
        else:
            b=b-with_am
            print(with_am,"has been withdrawn successfully")
            bli=input("Do you want to check your balance ?(Y/N)")
            if bli=='Y':
                print("The balance is:",b)
            else:
                pass
    if(ch==2):
        dep_am=int(input("Enter the amount to be deposited: "))
        pin=int(input("Enter your pin:"))
        if(pin!=pins[index]):
            print("Invalid pin")
            print("END")
        else:
            b=balance[index]
            b=b+dep_am
            print(dep_am,"has been deposited successfully")
            bli=input("Do you want to check your balance ?(Y/N)")
            if bli=='Y':
                print("The balance is:",b)
            else:
                pass
    if(ch==3):
        pin=int(input("Enter your pin:"))
        if(pin!=pins[index]):
            print("Invalid pin")
            print("END")
        else:
            b=balance[index]
            print("The balance is:",b)
    if(ch==4):
        pin=int(input("Enter your pin:"))
        if(pin!=pins[index]):
            print("Invalid pin")
            print("END")
        else:
            new_p=input("Enter new password :")
            rnew_p=input("Re-Enter the password :")
            if(new_p==rnew_p):
                print("Password Changed Successfully !")
                print("END")
            else:
                for i in range(2):
                    rnew_p=input("Re-Enter the password :")
                    if(rnew_p==new_p):
                        print("Password changed succeesfully !")
                        break
user_name=["Anjali","Sarayu","Vasanthi","Aiswarya","Binod","Rajeswari","Jyothi"]
password=['Anju123','Sara@345','Vasu@789','Ishu*67','Binu&23','Raje$456','Jyo^45']
pins=[2211,2264,9865,9962,7856,7965,4523]
balance=[150208,1523640,256320,160234,150956,180562]
user=input("Enter User Name:")
if(user not in user_name):
    print("The user is not available")
else:
    for i in range(len(user_name)):
        if user_name[i]==user:
            ATM(i)
