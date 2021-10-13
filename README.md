# Tipster - JTC App Project 1
***
Tipster is a command line Python tip calculator that allows the user to input the bill, number of parties, and tip amount, with the option to evenly or unevenly split the bill, which outputs how much each party will need to pay with a 10% tax included.
***

## Table of Contents

- Installation/Technology Requirements
    - Python ver. 3.9.7
- Usage
    - Run Tipster Python script from command line
    - User Inputs: bill, number of people, and tip amount
    - Outputs: total amount per person, if bill divided evenly, including tax
- Bonus Features
    - Input Checks
    - Uneven Bill Calculator
- License
- Links

***
## Installation/Technology Requirements
Tipster was made using Python ver. 3.9.7 and should work on subsequent versions of Python.
***

## Usage
To run Tipster, please type on the command line:
~~~
python tipster.py
~~~
User Inputs: bill, number of people, and tip amount
~~~
What was the total bill without taxes?
~~~
~~~
How many people are in your party?
~~~
~~~
How much do you want to tip (please enter a %)?
~~~
Outputs: total amount per person, if bill divided evenly, including tax
~~~
print(f'Total bill: ${Formatted_bill_amount}\nEach person should pay: ${Formatted_per_person_cost}')
~~~
***
## Bonus Features
### Input Checks:
Every user input is checked to make sure it is a valid entry, i.e., a positive float/int, no negative numbers/strings where required.
### Uneven Bill Calculator:
There is an option to calculate each person's total amount if the bill is split unevenly and some people do not buy/pay anything. User will have to provide the portion of the total bill each person is paying and the amount each person will tip. Each paying person's total amount including tip and tax will be outputed.
~~~
print(f'Person {count} is paying ${Formatted_each_person_cost}.')
~~~
***
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
***
## License
[MIT](https://choosealicense.com/licenses/mit/)
***
Copyright (c) 10/13/2021 Rakesh Perani



