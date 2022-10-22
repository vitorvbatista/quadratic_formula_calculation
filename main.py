# solving simple quadratic formula without sympy
import re
from math import sqrt


def check_formula(equation):
    # This function will analyse all variables (a, b and c) and check if they need to have any handling
    # Will return the same equation but revised
    a_ = equation[0]

    if a_ == "x":
        equation = '1' + equation
    else:
        pass

    x_b = re.findall(r"^.*x²", equation)[0]
    temp_eq_ = equation.replace(x_b, "")

    sign_ = temp_eq_[0]
    b_ = temp_eq_[1]

    if b_ == "x":
        temp_eq_ = temp_eq_.replace(temp_eq_[0:2], "")
        b_ = sign_ + '1' + b_
        equation = x_b + b_ + temp_eq_
    else:
        pass

    return equation


def calculate_delta(var_b, var_a, var_c):
    # This function will solve delta, receiving a, b and c and return the result
    calc_delta = (-var_b) ** 2 - 4 * var_a * var_c
    return calc_delta


def calculate_final_result(calc_delta, var_a, var_b):
    x_1 = float((-var_b + sqrt(calc_delta)) / (2 * var_a))
    x_2 = float((-var_b - sqrt(calc_delta)) / (2 * var_a))
    return x_1, x_2


if __name__ == '__main__':

    # We start this program requesting a quadratic equation
    # So far, only these quadratic equation models are accepted:
    # x² - 5x + 6 = 0
    # -x² + x + 12 = 0
    # 6x² + x - 1 = 0

    input_equation = str(input('Write your equation:'))
    input_equation = input_equation.replace(" ", "").replace("–", "-").replace("x2", "x²").replace("x^2", "x²")
    # To ensure the correct equation modelling we'll replace some characters
    print(input_equation)

    input_equation = check_formula(input_equation)  # Calling function check_formula

    # Below there's new treatment for a,b and c. We have to ensure all of them are correct and prepared for calculation
    # That's why we'll use regex for this type of validation
    try:
        a = int(re.findall(r".*?(?=x²)", input_equation)[0])
    except ValueError:
        a = -1

    b = int(re.findall(r"(?<=x²).*?(?=x)", input_equation)[0])

    try:
        c = int(re.findall(r"(?<=x)([+-] *\d+)", input_equation)[0])
    except IndexError:
        c = 0

    print("a=", a, "b=", b, "c=", c)

    delta = calculate_delta(b, a, c)  # Calculating delta through function 'calculate_delta'

    # Check if delta equals 0 or negative. So far we can only solve all problem with positive values
    # But is possible to continue if you're working with complex numbers
    if int(delta) <= 0:
        print(u'\u0394', "=", delta, "Cannot take square root of 0 or negative number. You can solve using complex "
                                     "numbers")

    else:
        # If delta is positive, solve quadratic formula, using 'calculate_final_result'
        # x1_result is x' and x2_result is x''.

        x1_result, _ = calculate_final_result(delta, a, b)
        _, x2_result = calculate_final_result(delta, a, b)

        # If x1 or x2 is integer, we'll use round to avoid decimal numbers
        # If x1 or x2 is floating, we'll use round '2' to add two decimals
        if x1_result.is_integer():
            x1_result = round(x1_result)
        else:
            x1_result = round(x1_result, 2)

        if x2_result.is_integer():
            x2_result = round(x2_result)
        else:
            x2_result = round(x2_result, 2)

        # print final result
        print("{", x1_result, ",", x2_result, "}")
