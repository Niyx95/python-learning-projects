import sys, time, ascii

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "matcha latte": {
        'ingredients': {
            'water': 100,
            'milk': 200,
            'coffee': 18,
            'matcha': 45
        },
        'cost': 4.5,
    }
}

resources = {
    "water": 1100,
    "milk": 700,
    "coffee": 300,
    'matcha': 250,
}

#function to handle payment
def payment(name):
    #take the cost from dictionary / set a variable to store
    cost = MENU[name]['cost']
    total_paid = 0
    #looping trough cost to check if user entered sufficient money and handle change
    while total_paid < cost:
        try:
            print(f'Your total is: {cost}$')
            pay = float(input('Please insert coins! $ '))
            total_paid += pay
            if total_paid < cost:
                print('you need to insert more coins')
            elif total_paid == cost:
                print('Purchase complete.Thank you!')
            elif total_paid > cost:
                change = total_paid - cost
                print(f'The total cost for your coffee is: {cost} $')
                time.sleep(0.5)
                print(f'Here is your change {change} $')
        except ValueError:
            print('Invalid input. Please insert a number:')

#function to check if resources are enough and subtract if.
def enough_resources(name):
    #look to the ingredients
    ingredients = MENU[name]['ingredients']
    # check if resources are enough and subtract choice from resources
    for key, value in ingredients.items():
        if resources[key] < value:
            print('sorry not enough resources')
            sys.exit()
        else:
            resources[key] -= value

#coffee making function
def coffee_making(name):
    #iterate with dictionary to set the ingredients and the cost
    cost = MENU[name]['cost']
    print(f'making {name}')
#function to show user resources
def show_resources():
    print('Current resources are:')
    for key, value in resources.items():
        print(f'{key}: {value}')

#print logo and greet customer
print(ascii.logo)
print('Welcome to Nyx virtual coffee machine, what would you like today?')
#loop to get machine started and running until user wants
while True:
    #turn on machine and user prompt
    print('This is the menu: espresso, latte, cappuccino or matcha latte:')
    choice = input('select you coffe: >> ')
    #Turn off machine
    if choice not in MENU:
        print('invalid choice')
        sys.exit()
    #calling functions to run machine logic
    payment(choice)
    enough_resources(choice)
    coffee_making(choice)
    #asking user if he wants another coffe
    add = input('Do you want another coffee? (y/n) TYPE "R" to see machine resources! > ').lower().strip()
    if add == 'n':
        sys.exit()
    elif add == 'r':
        show_resources()
    else:
        continue
