# writing code for calculating the simple interest 


def interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period in years: "))

    intrst =  (principal * rate * time) / 100

    print(f"interest on the amount {principal} with the rate of  {rate}% for {time} years is {intrst}")


I = True
while(I):
    interest()

    print("Want to calculate more interest ?")
    
    choice = input("Enter 'A' for yes or click any key to exit \n")

    if choice=="A" or choice == "a":
        I = True
    else:
        break


