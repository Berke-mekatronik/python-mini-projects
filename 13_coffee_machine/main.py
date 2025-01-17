from menu import MENU
from menu import resources

def print_report(current_water, current_milk, current_coffee, money):
    print(f"Water: {current_water}ml")
    print(f"Milk: {current_milk}ml")
    print(f"Coffee: {current_coffee}g")
    print(f"Money: ${money}")

def enough_resources(current_water, current_milk, current_coffee,user_select):
    if current_water < MENU[user_select]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return True
    elif current_milk < MENU[user_select]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return True
    elif current_coffee < MENU[user_select]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return True

def process_coin(q, d, n, p, user_select):
    total = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
    if total < MENU[user_select]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = total - MENU[user_select]["cost"]
        change = round(change, 2)
        print(f"Here is ${change} in change.")
    return total

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
machine_working = True
total_money = 0

while machine_working:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        machine_working = False
    elif user_choice =="report":
        print_report(water, milk, coffee, total_money)
        machine_working = True
    else:
        if enough_resources(water, milk, coffee, user_choice):
            #machine_working = False
            pass
        else:
            print("Please insert coins.")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickle = int(input("How many nickles?: "))
            penny = int(input("How many pennies?: "))
            total_money = process_coin(quarter, dime, nickle, penny, user_choice)
            print(f"Here is your {user_choice}☕️. Enjoy!")
            machine_working = True

            water -= MENU[user_choice]["ingredients"]["water"]
            milk -= MENU[user_choice]["ingredients"]["milk"]
            coffee -= MENU[user_choice]["ingredients"]["coffee"]


