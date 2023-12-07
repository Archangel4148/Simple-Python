import math
from fractions import Fraction
while True:
    response = input("Enter the 3 coefficients, separated by spaces: ")   
    while len(response.split()) != 3:
        print("Invalid input. Enter 3 coefficients (if necessary, add zeros)\n")
        response = input("\nEnter the 3 coefficients, separated by spaces: ")    
    l = response.split()
    try:
        a, b, c = float(l[0]), float(l[1]), float(l[2])
    except ValueError:
        print("Invalid input. Please use only number values...\n")
        continue
    
    if a == int(a):
        a = int(a)
    if b == int(b):
        b = int(b)
    if c == int(c):
        c = int(c)

    print(f"\nEquation: ", end="")
    if a < 0:
        print("- ", end="")
    if a != 1 and a != -1:
        print(a, end="")
    print("x^2", end=" ")
    if b < 0:
        print("- ", end="")
    else:
        print("+ ", end="")
        
    print(f"{abs(b)}x", end=" ")
    if c < 0:
        print("- ", end="")
    else:
        print("+ ", end="")
    print(f"{abs(c)}", end=" ")

    print("\n\nSolution(s):\n")

    if (b**2 - 4*a*c) < 0:
        print("No Real Solutions!\n")
    else:
        x1 = ((0-b) + math.sqrt(b**2 - 4*(a)*(c)))/(2*a)
        x2 = ((0-b) - math.sqrt(b**2 - 4*(a)*(c)))/(2*a)


        if x1 == int(x1):
            x1 = int(((0-b) + math.sqrt(b**2 - 4*(a)*(c)))/(2*a))
        if x2 == int(x2):
            x2 = int(((0-b) - math.sqrt(b**2 - 4*(a)*(c)))/(2*a))
        print(f"Decimal: x = {x1}")
        print(f"Fraction: x = {Fraction(x1).limit_denominator()}")
        if x2 != x1:
            print(f"Decimal: x = {x2}")
            print(f"Fraction: x = {Fraction(x2).limit_denominator()}")
            
