import math
import sympy as sp
import numpy as np


# Function to solve linear equations
def solve_linear_equation(equation):
    symbols = set(ch for ch in equation if ch.isalpha())  # Get all alphabets from the equation
    symbols = [sp.symbols(symbol) for symbol in symbols]  # Create symbols dynamically
    lhs, rhs = equation.split('=')
    for symbol in symbols:
        lhs = lhs.replace(symbol.name, f'*{symbol.name}')  # Replace each symbol in lhs with '*symbol'
    lhs = sp.sympify(lhs)
    rhs = sp.sympify(rhs)
    solution = sp.solve(lhs - rhs, symbols)
    return solution


# Function to solve quadratic equations
def solve_quadratic_equation(a, b, c):
    x = sp.symbols('x')
    solutions = sp.solve(a * x ** 2 + b * x + c, x)
    return solutions


# Function to solve polynomial equations
def solve_polynomial_equation(coefficients):
    x = sp.symbols('x')
    polynomial = sum(coef * x ** i for i, coef in enumerate(reversed(coefficients)))
    roots = sp.solve(polynomial, x)
    return roots


# Function to solve cubic equations
def solve_cubic_equation(a, b, c, d):
    x = sp.symbols('x')
    cubic_eq = a * x ** 3 + b * x ** 2 + c * x + d
    roots = sp.solve(cubic_eq, x)
    return roots


# Function to differentiate expressions
def differentiate(expression):
    x = sp.symbols('x')
    expr = sp.sympify(expression)
    derivative = sp.diff(expr, x)
    return derivative


# Function to integrate expressions
def integrate(expression):
    x = sp.symbols('x')
    expr = sp.sympify(expression)
    integral = sp.integrate(expr, x)
    return integral


# Function to invert a matrix
def matrix_inversion(matrix):
    try:
        inv_matrix = np.linalg.inv(matrix)
        return inv_matrix
    except np.linalg.LinAlgError:
        return None


# Function to calculate determinant of a matrix
def matrix_determinant(matrix):
    try:
        det = np.linalg.det(matrix)
        return det
    except np.linalg.LinAlgError:
        return None


class DestiSolverApp:
    def __init__(self):
        pass

    def run(self):
        print("Welcome to DestiSolver AI")
        print("Select an option:")
        print("1. Solve linear equation")
        print("2. Solve quadratic equation")
        print("3. Solve polynomial equation")
        print("4. Solve cubic equation")
        print("5. Differentiate expression")
        print("6. Integrate expression")
        print("7. Exponential functions")
        print("8. Trigonometric functions")
        print("9. Matrix Inversion")
        print("10. Matrix Determinant")
        print("11. Exit")

        while True:
            choice = input("Enter your choice (1-11): ")
            if choice == '1':
                equation = input("Enter linear equation (e.g., 2x + 3 = 0): ")
                print("Solution:", solve_linear_equation(equation))
            elif choice == '2':
                a = float(input("Enter coefficient 'a' for ax^2: "))
                b = float(input("Enter coefficient 'b' for bx: "))
                c = float(input("Enter coefficient 'c': "))
                print("Solutions:", solve_quadratic_equation(a, b, c))
            elif choice == '3':
                coefficients = input("Enter polynomial coefficients as comma-separated values (e.g., 1, -3, 2): ")
                coefficients = [float(coef) for coef in coefficients.split(',')]
                print("Solutions:", solve_polynomial_equation(coefficients))
            elif choice == '4':
                a = float(input("Enter coefficient 'a' for ax^3: "))
                b = float(input("Enter coefficient 'b' for bx^2: "))
                c = float(input("Enter coefficient 'c' for cx: "))
                d = float(input("Enter coefficient 'd': "))
                print("Solutions:", solve_cubic_equation(a, b, c, d))
            elif choice == '5':
                expression = input("Enter the expression to differentiate: ")
                print("Derivative:", differentiate(expression))
            elif choice == '6':
                expression = input("Enter the expression to integrate: ")
                print("Integral:", integrate(expression))
            elif choice == '7':
                base = float(input("Enter the base: "))
                exponent = float(input("Enter the exponent: "))
                print("Result:", base ** exponent)
            elif choice == '8':
                expression = input("Enter the trigonometric function (e.g., sin(30)): ")
                print("Result:",
                      eval(expression, {'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'radians': math.radians}))
            elif choice == '9':
                matrix_str = input("Enter the matrix as comma-separated rows (e.g., [[1, 2], [3, 4]]): ")
                matrix = eval(matrix_str)
                print("Inverted Matrix:", matrix_inversion(matrix))
            elif choice == '10':
                matrix_str = input("Enter the matrix as comma-separated rows (e.g., [[1, 2], [3, 4]]): ")
                matrix = eval(matrix_str)
                print("Determinant:", matrix_determinant(matrix))
            elif choice == '11':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 11.")


if __name__ == "__main__":
    app = DestiSolverApp()
    app.run()
