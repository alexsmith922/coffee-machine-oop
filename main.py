from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
drink_title = MenuItem()
drinks = Menu()
is_on = True
report = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    drink_choice = input("What would you like to drink?" + " " + drinks.get_items() )
    if drink_choice == "report":
        report.report()
        money_machine.report()
    elif drink_choice == "off":
        print("Shutting down...")
        is_on = False
    else:
        report.is_resource_sufficient(drink_title.name)