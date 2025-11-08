#---------------------------- PART 1------------------------------------------
# Initialize the expenses and incomes lists 
expenses = []
incomes = []

#----------------------------- PART 2------------------------------------------
# import the json library
import json
# This function takes in the expenses list, income lists, and json file
def save_financial_data(expenses, incomes, filename="data.json"):
    # Combine expenses and incomes lists into one dictionary
    data = {"expenses": expenses, "incomes": incomes}

    # Attempt to write data to a file
    try:
      # Open the file in write mode
      with open(filename, "w") as file:
        # Use json's dump function to add data into the json file
        json.dump(data, file, indent=4)
        print("Data saved successfully.")
    # Handle exception when writing fails
    except IOError as e:
        print("An error has occured while writing to the file:", e)
# This function takes in the json file
def load_financial_data(filename="data.json"):
    # Attempt to load data from a file
    try:
      # Open the file in read mode 
      with open(filename, "r") as file:
        # Use json's load function and return the expenses and incomes data separately
        data = json.load(file)
        return data["expenses"], data["incomes"]
    #  Handle exception when file cannot be found, and return empty lists
    except FileNotFoundError:
      print("File not found.")
      return [], []
    # Handle exception when json loading fails, and return empty lists
    except json.JSONDecodeError:
      print("JSON loading failed.")
      return [], []
    # General exception for any other exceptions, and return empty lists
    except Exception as e:
      print("An error has occured while writing to the file:", e)
      return [], []        
#-----------------------------PART 3------------------------------------------
# This function takes in the entries, either the expenses or incomes list, and the entry_type (either 'expenses' or 'incomes')
def add_financial_entry(entries_list, entry_type):
  # Attempt to collect user input
  try:
    # Add category and amount variables to collect user input
    category = input(f"Category: {entry_type}")
    amount = float(input(f"Enter amount: {entry_type}"))

    # Create and add the new dictionary entries into the lists
    entries_list.append({"category": category, "amount": amount})
    print(f"{entry_type.capitalize()} added: {category} - ${amount}")
    # Print the category and amount added using f-strings
    print(f"{category}, {amount}")
  # Handle exception when user input is not valid for the amount
  except ValueError:
    print("User input is not valid.")

def user_interface():
  # call the load_financial_data function
  expenses, incomes = load_financial_data(filename="data.json")

  # add a while loop that continues as long as the user does not select option 3
  while True:
        # Show options to the user
        print("\nOptions: [1] Add Expense [2] Add Income [3] Save and Exit")
        # Get the user's input, either 1, 2, or 3
        user_input = input("Enter your choice (1, 2, or 3): ").strip()
        # if they select 1, call the add_financial_entry function, and specify the expenses list and the string 'expense'
        if user_input == "1":
            add_financial_entry(expenses, "expenses\n")
        elif user_input == "2":
            add_financial_entry(incomes, "incomes\n")
        elif user_input == "3":
            save_financial_data(expenses, incomes)
            print("Exiting program.")
            print(expenses)
            break
        # else, print a message saying that the option they entered is invalid
        else:
          print("User input is not valid.")

# Run the user interface
user_interface()
