from datetime import datetime, timedelta

def display_current_datetime():
  """Gets the current date and time and prints it in a readable format."""
  current_date = datetime.now()
  formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current Date and Time: {formatted_datetime}")

def calculate_future_date(days):
  """Calculates the future date based on the provided number of days."""
  current_date = datetime.now()
  future_date = current_date + timedelta(days=days)
  formatted_future_date = future_date.strftime("%Y-%m-%d")
  print(f"Future Date (after {days} days): {formatted_future_date}") 


if __name__ == "__main__":
  display_current_datetime()

  while True:
    try:
      days = int(input("Enter the number of days to add (or 0 to exit): "))
      if days == 0:
        break
      calculate_future_date(days)
    except ValueError:
      print("Invalid input. Please enter a whole number of days.")