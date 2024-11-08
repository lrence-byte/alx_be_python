shopping_list = []

def add_item(item):
  """Adds an item to the shopping list."""
  shopping_list.append(item)
  print(f"{item} added to the list!")

def remove_item(item):
  """Removes an item from the shopping list."""
  if item in shopping_list:
    shopping_list.remove(item)
    print(f"{item} removed from the list!")
  else:
    print(f"{item} not found in the list.")

def display_menu():
  """Prints the current shopping list."""
  if shopping_list:
    print(f"Shopping List:")
    for item in shopping_list:
      print(f"- {item}")
  else:
    print(f"The shopping list is empty.")

def main():
  """Main loop for user interaction."""
  while True:
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Display menu")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      item = input("Enter item name: ")
      add_item(item)
    elif choice == '2':
      item = input("Enter item name to remove: ")
      remove_item(item)
    elif choice == '3':
      display_menu()
    elif choice == '4':
      print("Exiting Shopping List Manager.")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
  main()
