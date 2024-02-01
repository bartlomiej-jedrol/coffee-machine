"""Module contains code for Virtual Coffee Machine."""

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
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def is_resource_sufficient(ingredients):
    """Returns True if resources for ingredients are available."""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough: {item}.")
            return False
        return True


def process_coins():
    """Calculates total for the inserted coins."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * coins["quarters"]
    total += int(input("How many dims? ")) * coins["dimes"]
    total += int(input("How many nickles? ")) * coins["nickles"]
    total += int(input("How many pennies? ")) * coins["pennies"]
    return round(total, 2)


def is_transaction_successful(amount, cost):
    """Verifies if the transaction is successful."""
    if amount >= cost:
        if amount > cost:
            change = round(amount - cost, 2)
            print(f"Here is ${change} in change.")
        resources["money"] += cost
        return True
    print("Sorry, that's not enough money.")
    return False


def make_coffee(ingredients):
    """Makes a coffee. Deducts resources. Adds profit."""
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {product}. Enjoy!")


should_continue = True
while should_continue:
    product = input(" What would you like? espresso/latte/cappuccino: ")
    if product == "off":
        should_continue = False
    elif product == "report":
        print_resources_report()
    elif product in ("espresso", "latte", "cappuccino"):
        order_ingredients = MENU[product]["ingredients"]
        if is_resource_sufficient(ingredients=order_ingredients):
            total_coins = process_coins()
            drink_cost = MENU[product]["cost"]
            if is_transaction_successful(amount=total_coins, cost=drink_cost):
                make_coffee(ingredients=order_ingredients)
    else:
        should_continue = False
