loan= float(input("Enter loan amount: "))
r= float(input("Enter annual interest rate: "))
n= float(input("Enter a loan duration: "))
payment= (r*(loan))/(1-(1 + r)**-n)
print(payment)
