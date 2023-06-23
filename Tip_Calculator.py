#Group 7 Cohort 4
#email: isaac.agbogah@azubiafrica.org


print('Welcome To the Asanka Hotel Tip Calculator')

print('\n========================================')

while True:
    # ask user for charge of the food
    name = (input("Please Enter your name: ")).capitalize()
    charge = float(input("Enter the charge for the food: "))

    print('\n========================================')

    # calculate 18% tip of charge and 7% sales tax of charge
    tip = 0.18 * charge
    sales_tax = 0.07 * charge

    # calculate total amount
    total = charge + tip + sales_tax

    # display results
    print(f"Hello! {name}")
    print("Your 8% Tip Amount is $",round(tip, 2))
    print("Your 7% Sales Tax is $",round(sales_tax, 2))

    print('\n---------------------------------------')

    print("Your Total Amount is $",round(total, 2))

    print('\n========================================')

    # ask user if they want to calculate another tip and tax
    response = input(f"{name} Do you want to calculate tip and tax for another food charge? (y/n): ")

    print('\n========================================')

    if response.lower() != 'y':
        print(f"Thanks for Using the Calculator. See You Soon {name}")
        print("This App is Powered by Fantastic Rambo!")
        exit()
