# imports

import time

from data import menu, supplies, coins

# user interface variables

drinks = list(menu.keys())
menu_prompt = "Coffee menu:\n"
drinks_prompt = ""
BLUE_TEXT = "\033[34m"
GREEN_TEXT = "\033[32m"
YELLOW_TEXT = "\033[33m"
RED_TEXT = "\033[31m"
DEFAULT_TEXT = "\033[0m"

# machine operation variables

machine_on = True
machine_money = 0.00
machine_supplies = supplies
machine_supplies_list = list(machine_supplies.keys())

for drink in drinks:
    drinks_prompt += f"{str(drinks.index(drink) + 1)}. {drink} - {menu[drink]["price"]["currency"]}{float(menu[drink]["price"]["amount"]):.2f}\n"

def serve():
    global machine_on
    global machine_money

    paid = 0.00
    overpaid = True
    change_amount = 0.00

    try:
        command = input(BLUE_TEXT + menu_prompt + DEFAULT_TEXT + drinks_prompt + "\nMake your selection: #").lower()
        if command == "report":
            print(f"\n{YELLOW_TEXT}** ADMIN REPORT start **{DEFAULT_TEXT}\n")
            print("Machine supplies:")
            for supply in machine_supplies_list:
                print(f"\t{supply}: {machine_supplies[supply]["amount"]} {machine_supplies[supply]["units"]}")
            print(f"\nAvailable cash: {GREEN_TEXT}${machine_money:.2f}{DEFAULT_TEXT}")
            print(f"\n{YELLOW_TEXT}** ADMIN REPORT end **{DEFAULT_TEXT}\n")
        elif command == "off":
            machine_on = False
            power_off = f"Shutting down..."
            print(power_off)
            for bar in range(len(power_off) + 1):
                loaded = "." * bar
                pending = "%" * (len(power_off) - bar)
                print(f"\r[{loaded}{pending}]", end="", flush=True)
                time.sleep(0.05)
        else:
            order = int(command) - 1
            price = menu[drinks[order]]["price"]["amount"]
            print(f"\nPlease insert coins to prepare your {drinks[order]}.")
            print(f"Due: {RED_TEXT}${float(price):.2f}{DEFAULT_TEXT}\n")
            for coin in coins:
                if paid < price:
                    paid += float(input(f"Amount of {coin}: ")) * (coins[coin])
                else:
                    machine_money += price
                    change_amount = paid - price

                    if paid == price:
                        prepareDrink(not overpaid, paid, change_amount, drinks[order], menu[drinks[order]]["ingredients"])
                        return
                    elif paid > price:
                        prepareDrink(overpaid, paid, change_amount, drinks[order], menu[drinks[order]]["ingredients"])
                        return
                
                print(f"Paid: {GREEN_TEXT}${paid:.2f}{DEFAULT_TEXT}/${float(price):.2f}\n")

            if paid < price:
                reimburse = f"{RED_TEXT}Insufficient funds, here's your refund: ${float(paid):.2f}{DEFAULT_TEXT}"
                print(reimburse)
                for char in reimburse:
                    print("_", end="")
                print("\n")
        
    except (ValueError, IndexError):
        print("\n**INVALID SELECTION**\n\n")
        serve()

def prepareDrink(give_change, refund, change, drink, ingredients):
    # TODO check if supplies are enough

    for supply in machine_supplies_list:
        if machine_supplies[supply]["amount"] < ingredients[supply]["amount"]:
            print(f"Not enough supplies. Here's your refund {GREEN_TEXT}${float(refund):.2f}{DEFAULT_TEXT}\n")
            return

    if give_change:
        print(f"Here's your change: {GREEN_TEXT}${float(change):.2f}{DEFAULT_TEXT}\n\n")

    preparing = f"Preparing your {drink}..."
    print(preparing)
    for bar in range(len(preparing) + 1):
        loaded = "#" * bar
        pending = "." * (len(preparing) - bar)
        print(f"\r[{loaded}{pending}]", end="", flush=True)
        time.sleep(0.05)
    
    print("\n")

    for supply in machine_supplies_list:
        machine_supplies[supply]["amount"] -= ingredients[supply]["amount"]
    
    deliver = f"Here's your {drink} ☕, enjoy!"
    print(deliver)

    for char in deliver:
        print("_", end="")

    print("\n")

def run():
    while machine_on:
        serve()