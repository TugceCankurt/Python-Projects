#Create create a program that allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.
import math
print("investment - to calculate the amount of interest you'll earn on your investment\nbond - to calculate the amount you'll have to pay on a home loan ")

#Get user's selection and convert it to lower case
users_selection=input("Enter either 'investment' or 'bond' from the menu above to proceed:").lower()
print(users_selection)

#If users select investment 
if users_selection=="investment":
    users_deposit=int(input("Please enter the amount of money that you are depositing:"))
    interest_rate=int(input("Please enter your interest rate(Only the number of the interest rate should be entered):"))
    year= int(input("Please enter the number of years you plan on investing:"))
    interest_type=input("Please enter your input if they want “simple” or “compound” interest :").lower()
    print(users_deposit)
    print(interest_rate)
    print(year)
    print(interest_type)
    #If users select simple investment
    if interest_type== "simple":
        simple_interest= users_deposit*(1+(interest_rate/100)*year)
        print(simple_interest)
    #If users select compound investment
    elif interest_type== "compound":
        compound_interest=users_deposit* math.pow((1+interest_rate/100),year)
        print(compound_interest)
    else:
        print("You input is unvalid, please type only “simple” or “compound")
#If users select bond
elif users_selection=="bond":
    present_value=int(input("Please enter the present value of the house e.g. 100000 :"))
    interest_rate=int(input("Please enter  The interest rate. e.g. 7 :"))
    months=int(input("Please enter The number of months they plan to take to repay the bond. e.g. 120 :"))
    print(present_value)
    print(interest_rate)
    print(months)
    i= (interest_rate/100)/12
    repayment= (i*present_value)/(1-(1+i)**(-months))
    print(repayment)
else: 
    print("You input is unvalid, please type only “investment” or “bond")



    
