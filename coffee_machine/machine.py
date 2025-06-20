# imports

from data import menu, supplies, coins

# user interface variables

drinks = list(menu.keys())
menu_prompt = "Coffee menu:\n"
drinks_prompt = ""
BLUE_TEXT = "\033[34m"
GREEN_TEXT = "\033[32m"
YELLOW_TEXT = "\033[33m"
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
        else:
            order = int(command) - 1
            price = menu[drinks[order]]["price"]["amount"]
            print(f"\nPlease insert coins to prepare your {drinks[order]}:\n")
            for coin in coins:
                if paid < price:
                    paid += float(input(f"Amount of {coin}: ")) * (coins[coin])
                else:
                    machine_money += price
                    change_amount = paid - price

                    if paid == price:
                        prepareDrink(not overpaid, change_amount, drinks[order], menu[drinks[order]]["ingredients"])
                        return
                    elif paid > price:
                        prepareDrink(overpaid, change_amount, drinks[order], menu[drinks[order]]["ingredients"])
                        return
                
                print(f"Paid: {GREEN_TEXT}${paid:.2f}{DEFAULT_TEXT}/${float(price):.2f}\n")

            if paid < price:
                print(f"Insufficient funds, here's your reimburse: ${paid}\n")
                print("___________________________\n")
        
    except (ValueError, IndexError):
        print("\n**INVALID SELECTION**\n\n")
        serve()

def prepareDrink(give_change, change, drink, ingredients):
    if give_change:
        print(f"Here's your change: {GREEN_TEXT}${float(change):.2f}{DEFAULT_TEXT}\n\n")
    print(f"Preparing your {drink}...")
    for supply in machine_supplies_list:
        machine_supplies[supply]["amount"] -= ingredients[supply]["amount"]
    
    print(f"Here's your {drink}, enjoy!\n")
    print("___________________________\n")

def run():
    while machine_on:
        serve()