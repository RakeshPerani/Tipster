# Tipster is a command line tip calculator app that allows the user to input the bill, number of people paying, and tip amount. It will output the total amount due including a 10% tip whether the bill is divided evenly or unevenly. 
# Bonus features include input checks to check for valid user inputs and an uneven tip option in the situations where the bill is not split evenly and everyone wants to leave their own personalized tip amount.
print()
print('Welcome To Tipster!')
print('A quick and easy tip calculator for you and your friends that includes a 10% tax.')
print()

#Function to input the bill amount and check if it user input is valid, i.e., not a string or negative number.
def get_bill():
    x = 0   
    while x <= 0:
        try:
            x = round(float(input("What was the total bill ($) without taxes? ")),2)
            if x <= 0:
                print('Invalid entry. Sorry, please enter a positive numerical dollar amount.')
                print()
        except:
            print('Invalid entry. Sorry, please enter a numerical value.')
            print()
    return(x)

#Function to input the number of parties that also checks if the user input is valid, i.e., not a string or negative number.
def get_parties():
    y = 0   
    while y <= 0:
        try:
            y = int(input("How many people are in your party? "))
            if y < 0:
                print('Invalid entry. Sorry, please enter a positive number of people.')
                print()
            if y == 0:
                print('Zero people is not a valid entry.')
                print()
        except:
            print('Invalid entry. Sorry, please enter a numerical value.')
            print()
    return(y)

#Function to input the tip amount and check if it is a valid input, i.e., not a string or negative number.
def get_tip_amount():
    z = -1  
    while z < 0:
        try:
            z = float(input("How much do you want to tip (please enter a %)? "))
            if z < 0:
                print('Invalid entry. Sorry, please enter a positive numerical dollar amount.')
        except:
            print('Invalid entry. Sorry, please enter a numerical value.')
    if z == 0:
        print()
        print('Cheapskate?! Not leaving a tip?')
    return(z)

#Function to calculate and print tip if bill is split evenly.
def bill_split_evenly(bill_amount, party, even_tip):
    total_bill_amount = (bill_amount*.1)+(bill_amount*even_tip+bill_amount)
    Formatted_bill_amount = '{:,.2f}'.format(total_bill_amount)
    per_person = total_bill_amount/party
    Formatted_per_person = '{:,.2f}'.format(per_person)
    if party == 1:
        print()
        print(f'Total bill: ${Formatted_bill_amount}')
    else:
        print()
        print(f'Total bill: ${Formatted_bill_amount}\nEach person should pay: ${Formatted_per_person}')

#Function to get user inputs of individualized tip percentage if the bill is split unevenly and make sure it is a valid input.
def get_uneven_tip_amount(cnt):
    z = -1  
    while z < 0:
        try:
            z = float(input(f"How much does person {cnt} want to tip (please enter a %)? "))
            if z < 0:
                print('Invalid entry. Sorry, please enter a positive numerical percentage')
                print()
        except:
            print('Invalid entry. Sorry, please enter a numerical value.')
            print()
    if z == 0:
        print('Cheapskate?! Not leaving a tip?')
        print()
    return(z)

#Function that accepts user inputs of the portion of the total bill they will pay in the event the bill is split unevenly. User inputs are checked to ensure everyone who is unevenly paying is covering the total bill and the total bill is not being shorted.
def bill_split_uneven(people, total_bill_to_be_split):
    person = []
    uneven_per_person_tip = []
    count = 1
    uneven_bill_total = total_bill_to_be_split
    while uneven_bill_total > 0:
        while people >= count:
            try:
                person.append(round(float(input(f'How much is person {count} paying? ')),2))
                print()
            except:
                print('Invalid entry. Sorry, please enter a positive numerical dollar amount.')
                print()
            uneven_per_person_tip.append(get_uneven_tip_amount(count))
            count += 1
        for individual in person:
            uneven_bill_total -= individual
        if uneven_bill_total != 0:
            print("Please check your payments for each party. It is not equaling the total bill.")
            print()
            count = 1
            person = []
            uneven_per_person_tip = []
            uneven_bill_total = total_bill_to_be_split
    person.append(uneven_per_person_tip)
    return person

#Function that calculates the individualized total bill of each person based on their portion of the total bill being split unevenly and the amount of tip they wish to pay.
def uneven_split_calc(uneven_split_list):
    count = 1
    uneven_tip = uneven_split_list[-1]
    uneven_split_list.remove(uneven_tip)
    for each_person in uneven_split_list:
        each_person = ((each_person*(uneven_tip[count-1]*.01))+each_person)+(each_person*.1)
        Formatted_each_person = '{:,.2f}'.format(each_person)
        print(f'Person {count} is paying ${Formatted_each_person}.')
        count += 1

#Start of code
bill = get_bill() #Function get_bill being called
print()
parties = get_parties() #Function get_parties getting called
print()
if parties == 1:
    tip = get_tip_amount()*.01
    bill_split_evenly(bill, parties, tip)
else: #Asking if bill will be split evenly or unevenly before asking for tip
    will_bill_be_split_evenly = ''
    while will_bill_be_split_evenly != 'y' and will_bill_be_split_evenly != 'n':
        will_bill_be_split_evenly = input('Will the bill be split evenly among all parties? Please enter Y or N. ').lower()
        print()
        if will_bill_be_split_evenly != 'y' and will_bill_be_split_evenly != 'n':
            print('Please enter Y or N only.')
            print()
    if will_bill_be_split_evenly == 'y':
        tip = get_tip_amount()*.01
        bill_split_evenly(bill, parties, tip)
    else:
        paying_people_count = 0
        while not paying_people_count:
            letters = False
            try: #Asking how many people are paying in the event some people may not being paying and checking inputs.
                paying_people_count = int(input('How many people are actually paying? '))
            except:
                print('Please enter a numerical value.')
                print()
                letters = True
            if paying_people_count > parties:
                    print('The number of people you entered exceeds the total number of people. Please enter the correct number of people.')
                    print()
                    paying_people_count = 0
            elif paying_people_count < 0:
                print('Please enter a positive number of people.')
                print()
                paying_people_count = 0
            elif paying_people_count == 0 and not letters:
                print('Zero people is not a valid entry.')
                print()
        amount_per_person = bill_split_uneven(paying_people_count, bill)
        uneven_split_calc(amount_per_person)

