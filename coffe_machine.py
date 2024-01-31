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


def is_enough_money(item, amount):
    """Calculates money difference between amount and cost."""
    return amount - MENU[item]["cost"] >= 0


def process_change(amount, cost):
    """Calculates money difference between amount and cost."""
    print(f"Here is ${round(amount - cost, 2)} in change.")


def make_coffee(ingredients, profit):
    """Makes a coffee. Deducts resources. Adds profit."""
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    resources["money"] += profit


should_continue = True
while should_continue:
    product = input(" What would you like? espresso/latte/cappuccino: ")
    print("test")
    if product == "off":
        should_continue = False
    elif product == "report":
        print_resources_report()
    elif product in ("espresso", "latte", "cappuccino"):
        print("test1")
        order_ingredients = MENU[product]["ingredients"]
        # Check if there are sufficient resources to make an order.
        if is_resource_sufficient(ingredients=order_ingredients):
            print("test2")
            total_coins = process_coins()
            # Check if there is enough money to make an order.
            if is_enough_money(item=product, amount=total_coins):
                price = MENU[product]["cost"]
                # Check if change is required.
                if total_coins - price > 0:
                    process_change(amount=total_coins, cost=price)

                make_coffee(ingredients=order_ingredients, profit=price)
                print(f"Here is your {product}. Enjoy!")
            else:
                print("Sorry, that's not enough money.")
    else:
        should_continue = False
