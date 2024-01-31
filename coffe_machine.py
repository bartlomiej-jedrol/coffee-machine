"""Module contains code for Virtual Coffee Machine."""
import sys

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
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 2.5,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}


def print_resources_report():
    """Prints current resources values and units."""
    water_value = resources["water"]
    milk_value = resources["milk"]
    coffee_value = resources["coffee"]
    money_value = resources["money"]
    print(f"Water: {water_value}ml")
    print(f"Milk: {milk_value}ml")
    print(f"Coffee: {coffee_value}g")
    print(f"Money: ${money_value}")


def check_depleted_resources(product):
    """Checks if resources are depleted. Return depleted resources list."""
    depleted_resources_list = []
    for key, value in MENU[product]["ingredients"].items():
        if value > resources[key]:
            depleted_resources_list.append(key)
    return len(depleted_resources_list) > 0, depleted_resources_list


def calculate_coins():
    """Calculates amount of inserted coins."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dims = int(input("How many dims? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    amount = (
        quarters * coins["quarters"]
        + dims * coins["dimes"]
        + nickles * coins["nickles"]
        + pennies * coins["pennies"]
    )
    return round(amount, 2)


def is_enough_money(product, amount):
    """Calculates money difference between amount and cost."""
    money_difference = amount - MENU[product]["cost"]
    return money_difference > 0, round(money_difference, 2)


def make_coffee(product):
    """Makes a coffee. Deducts resources. Adds profit."""
    for ingredient, ingredient_amount in MENU[product]["ingredients"].items():
        resources[ingredient] -= ingredient_amount
    resources["money"] += MENU[product]["cost"]


def run_machine():
    """Runs the coffee machine."""
    should_continue = True
    while should_continue:
        product = input(" What would you like? espresso/latte/cappuccino: ")
        if product == "off":
            sys.exit()
        elif product == "report":
            print_resources_report()
        elif product in ("espresso", "latte", "cappuccino"):
            depleted_resources, depleted_resources_list = check_depleted_resources(
                product=product
            )
            if depleted_resources:
                print(
                    f"Sorry, there is not enough: {', '.join(depleted_resources_list)}."
                )
            elif not depleted_resources:
                total_coins = calculate_coins()
                enough_money, change = is_enough_money(
                    product=product, amount=total_coins
                )
                if not enough_money:
                    print("Sorry, that's not enough money.")
                elif enough_money:
                    if change > 0:
                        print(f"Here is ${change} in change.")
                    make_coffee(product)
                    print(f"Here is your {product}. Enjoy!")


run_machine()
