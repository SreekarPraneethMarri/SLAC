import subprocess
import string
import random
from tkinter import *
import webbrowser

print ("Welcome")

def callback(event):
     webbrowser.open_new(event)


def main_ho(x):
    if(x==1):
        dept()
    elif(x==2):
         
         print("########### BMI ##############")
         while (True):
             name = input("Enter the name of patient ")
             if (name!=""):
                 break
             else:
                 print("Incorrect Input. Please Verify it and Enter again")
                 continue
         while(True):
             email = input("Enter the email address of patient ")
             if (email!=""):
                 break
             else:
                 print("Incorrect Input. Please Verify it and Enter again") 
                 continue
         while (True):
             phone = input("Enter the mobile number of patient ")
             if (phone!="" and len(phone)==10):
                 break
             else:
                 print("Incorrect Input. Please Verify it and Enter again")
                 continue
         while(True):
             a=float(input("Enter the weight(in kg)  of the patient"))
             if (a!=""):
                 break
             else:
                 print("Incorrrect Input. Please Enter again")
                 continue
         b=float(input("Enter the height(in m) of the patient (Upto 2 decimal places)"))
         bmi=a/pow(b,2)         
         print("Your BMI is",bmi)
         if (bmi<18.5):
             print("You are undwerweight")
         elif (18.5<bmi<25):
             print("You are healthy")
         elif (25<bmi<30):
             print("You are overweight")
         else:
             print("You are obese")
    
    elif(x==3):
        contact()
        
    else:
        print("Please check your input")

def dept():
    print("The departments in our healthcare are:")
    print("1. General Physician")
    print("2. ENT")
    print("3. Dermetology")
    print("4. Orthopadics")
    ni = int(input("Please enter your choice"))
    if(ni == 1):
        print("General Physician")
        print("The cost for consultation per patient is: ₹800")
        nip = int(input("Enter the number of patients"))
        if(nip != 0 and nip < 5):
            cost = 800*nip
            print("The total cost is: ",cost)
            checkchoice = input("Proceed to PAYMENT?(y/n)")
            if(checkchoice == "y"):
                checkout(nip,cost)
            elif(checkchoice == "n"):
                print("Thanks so much for stopping by! Wising You A Fast Recovery!!")
            else:
                print("Bad input. Please check your input")
    if(ni == 2):
        print("ENT")
        print("The cost for consultation per patient is: ₹850")
        nip = int(input("Enter the number of patients"))
        if(nip != 0 and nip < 5):
            cost = 850*nip
            print("The total cost is: ",cost)
            checkchoice = input("Proceed to PAYMENT?(y/n)")
            if(checkchoice == "y"):
                checkout(nip,cost)
            elif(checkchoice == "n"):
                print("Thanks so much for stopping by! Wising You A Fast Recovery!!")
            else:
                print("Bad input. Please check your input")
    if(ni == 3):
        print("Dermetology")
        print("The cost for consultation per patient is: ₹700")
        nip = int(input("Enter the number of patients"))
        if(nip != 0 and nip < 5):
            cost = 700*nip
            print("The total cost is: ",cost)
            checkchoice = input("Proceed to PAYMENT?(y/n)")
            if(checkchoice == "y"):
                checkout(nip,cost)
            elif(checkchoice == "n"):
                print("Thanks so much for stopping by! Have a great Day!!")
            else:
                print("Bad input. Please check your input")
    if(ni == 4):
        print("Orthopadics")
        print("The cost for consultation per patient is: ₹750")
        nip = int(input("Enter the number of patients"))
        if(nip != 0 and nip < 5):
            cost = 750*nip
            print("The total cost is: ",cost)
            checkchoice = input("Proceed to PAYMENT?(y/n)")
            if(checkchoice == "y"):
                checkout(nip,cost)
            elif(checkchoice == "n"):
                print("Thanks so much for stopping by! Have a great Day!!")
            else:
                print("Bad input. Please check your input")
    if(ni >4 or ni <= 0):
        print("Invalid Input! Please correct the same")

def checkout(pax,price):
    print("SPVM CITRUS PAY -- PAYMENT GATEWAY")
    print("Total number of patients: ",pax)
    print("TOTAL COST: ",price)
    for i in range(0, pax):
        while (True):
            name = input("Enter the name of Patient ")
            if (name!=""):
                break
            else:
                print("Incorrect Input. Please Verify it and Enter again")
                continue
        while(True):
            email = input("Enter the email address of patient ")
            if (email!=""):
                break
            else:
                print("Incorrect Input. Please Verify it and Enter again") 
                continue
        while (True):
            phone = input("Enter the mobile number of patient ")
            if (phone!="" and len(phone)==10):
                break
            else:
                print("Incorrect Input. Please Verify it and Enter again")
                continue
    print("Payment Options")
    print("1. CREDIT / DEBIT CARD")
    print("2. WALLETS")
    pay = int(input("ENTER YOUR PAYMENT METHOD "))
    if (pay == 1):
        while (True):
            s = input("Enter your 16 Digit Card Number ")
            if (len(s) == 16):
                break
            else:
                print("Incorrect Input. Please Verify it and Enter again")
                continue
        while(True):
            pin = input("Please enter your CVC ")
            if (len(pin)!=3):
                continue
            else:
                break
        print("PAYMENT SUCCESSFUL! We hope that you will get well soon !")
    elif (pay == 2):
        root = Tk()
        link1 = Label(root, text="Paytm Gateway", fg="orange", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("www.paytm.com"))

        link2 = Label(root, text="Google Pay", fg="blue", cursor="hand2")
        link2.pack()
        link2.bind("<Button-1>", lambda e: callback("www.gpay.com"))

        link3 = Label(root, text="PhonePe", fg="blue", cursor="hand2")
        link3.pack()
        link3.bind("<Button-1>", lambda e: callback("https://www.phonepe.com/en/"))

        button = Button(root, text="Click to Complete Payment", command=lambda:root.destroy()).pack()
        root.mainloop()

        print("PAYMENT SUCCESSFUL! We hope that you will get well soon !")

def contact():
    print("~~~~~~~~~~~~~~ SPVH Healthcare ~~~~~~~~~~~~~")
    print("Address: CA 21, Mahatma Gandhi Road, Bangalore, India")
    print("Email: consult.spvhhealth@gmail.com")
    print("Web: www.spvhhealth.in")
    print("Please feel free to contact us regarding any emergency services. We're available 24x7 for our valuable customers. Thank you.")


ch = "y"

while(ch=="y"):
    
    print("Welcome to Healthcare")
    print("1. Departments")
    print("2. Health Status")
    print("3. Contact Us")
    n = int(input("Enter your choice :"))
    main_ho(n)
    ch = input("Do you wish to continue? (y/n) ")

if(ch == "n"):
    print("Thank you! Wishing you a Fast Recovery! ")

