FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  """Converts a temperature from Fahrenheit to Celsius and returns the result."""
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

def convert_to_fahrenheit(celsius):
  """Converts a temperature from Celsius to Fahrenheit and returns the result."""
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit

def main():
  """Prompts the user for temperature input and performs conversion."""
  while True:
    try:
      temperature = float(input("Enter temperature: "))
      unit = input("(C)elsius or (F)ahrenheit: ").upper()

      if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature:.2f}°C is equivalent to {converted_temp:.2f}°F")
      elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature:.2f}°F is equivalent to {converted_temp:.2f}°C")
      else:
        print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")
    break  # Exit the loop after one successful conversion

if __name__ == "__main__":
  main()