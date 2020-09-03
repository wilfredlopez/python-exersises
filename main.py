# # This entrypoint for arithmetic_arrangement
# from arithmetic_arranger import arithmetic_arranger
# from unittest import main


# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# # Run unit tests automatically
# main(module='test_arithmetic', exit=False)

# **************************************************************************
# This entrypoint for time_calculator
# from time_calculator import add_time
# from unittest import main


# print(add_time("11:06 PM", "2:02"))


# # Run unit tests automatically
# main(module='test_time', exit=False)

# ****************************************************************************
# This entrypoint for budget
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
main(module='test_budget', exit=False)
