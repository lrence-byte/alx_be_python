def safe_divide(numerator, denominator):

    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator
        return f"Result: {result:.2f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please provide valid numeric values for both numerator and denominator."

import sys
from robust_division_calculator import safe_divide

def main():
 
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)

    print(result)

if __name__ == "__main__":
    main()
