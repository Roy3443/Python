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
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}:")
            return False
    return True

def process_coins():
    """returns total calculated from coins inserted"""
    print("please input coins:")
    total=int(input("How many quarters"))*0.25
    total+=int(input("How many dimes"))*0.1
    total+=int(input("How many nickels"))*0.05
    total+=int(input("How many pennies"))*0.01
    return total


def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"here is your {drink_name}")

def is_trans_successful(amount_recieved,drink_cost):
    """return true if payment accepted or return false if money insuffiecent"""
    if amount_recieved>=drink_cost:
        change=round(amount_recieved-drink_cost, 2)
        print(f"money is {change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("sorry not enaf money.Money refunded")
        return False
is_on=True
while True:
    choice=input("what would you like?(espresso/latte/capuccino:")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
           payment=process_coins()
           if is_trans_successful(payment,drink["cost"]):
               make_coffee(choice,drink["ingredients"])

