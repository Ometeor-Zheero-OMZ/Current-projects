from menu import Menu
from drink_maker import DrinkMaker
from payment_system import PaymentSystem

payment_system = PaymentSystem()
drink_maker = DrinkMaker()
menu = Menu()

is_on = True

print("いらっしゃいませ! マリーナカフェへようこそ!")
while is_on:
    options = menu.get_items()
    choice = input(f"どのメニューにしますか？ ({options}): \n")
    if choice == "enough":
        print("ありがとうございました!")
        is_on = False
    elif choice == "report":
        drink_maker.report()
        payment_system.report()
    else:
        drink = menu.find_drink(choice)
        if drink == False:
            continue

        if drink_maker.is_resource_sufficient(drink) and payment_system.make_payment(drink.cost):
            drink_maker.make_coffee(drink)
