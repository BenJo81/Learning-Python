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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
coffee_order = True


def check_resources(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        return "Sorry, there is not enough water"
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        return "Sorry, there is not enough coffee"
    elif drink != "espresso" and resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        return "Sorry, there is not enough milk"
    else:
        return "Please insert coins."


while coffee_order:
    # TODO: 1. Prompt user, asking "What would you like? (espresso/latte/cappuccino):"
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
    if user_input == "off":
        coffee_order = False
    # TODO: 3. Print report
    elif user_input == "report":
        water_level = resources["water"]
        milk_level = resources["milk"]
        coffee_level = resources["coffee"]
        money_total = money
        print(f"Water: {water_level}ml")
        print(f"Milk: {milk_level}ml")
        print(f"Coffee: {coffee_level}g")
        print(f"Money: ${money_total}")
    else:
    # TODO: 4. Check resources sufficient?
        problem = check_resources(user_input)
        print(problem)

        # TODO: 5. Process coins
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        money_input_total = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
        money += money_input_total

        if money_input_total < MENU[user_input]["cost"]:
            print("Sorry that's not enough money. Money refunded")
            money -= money_input_total
        else:
            new_total = money_input_total - MENU[user_input]["cost"]
            money -= new_total
            if new_total > 0:
                print(f"Here is ${new_total:.2f} in change")
            print(f"Here is your {user_input} ☕️. Enjoy!")
            resources["water"] -= MENU[user_input]["ingredients"]["water"]
            if user_input != "espresso":
                resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
            resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
# TODO: 6. Check transaction successful?


# TODO: 7. Make coffee