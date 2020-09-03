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
# import budget
# from budget import create_spend_chart
# from unittest import main

# food = budget.Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = budget.Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = budget.Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print(food)
# print(clothing)

# print(create_spend_chart([food, clothing, auto]))

# # Run unit tests automatically
# main(module='test_budget', exit=False)

# ***********************************************************************
# This entrypoint for shape_calculator
# import shape_calculator
# from unittest import main


# rect = shape_calculator.Rectangle(5, 10)
# print(rect.get_area())
# rect.set_width(3)
# print(rect.get_perimeter())
# print(rect)

# sq = shape_calculator.Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)


# # Run unit tests automatically
# main(module='test_shape_calculator', exit=False)

# *********************************************************************************
# This entrypoint for prob_calculator
import prob_calculator
from unittest import main

hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)

# Run unit tests automatically
main(module='test_prob_calculator', exit=False)
