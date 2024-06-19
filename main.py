from datetime import datetime, timedelta
from data import items_list


# Constants
ITEM_TYPES = ["Headset", "Earpods", "Mouse", "Keyboard", "Webcam"]


def print_menu_options():
    print("\n***Main Menu***")
    print("Select your choice from the options below.\n")
    print("1. View item")
    print("2. Borrow item")
    print("3. Return item")
    print("4. Extend duration")
    print("5. Admin options (Add or Remove items)")
    print("6. Exit")
    print()


def validate_data(items_list):
    validated_items = []
    for item in items_list:
        error_message = validate_item(item, validated_items)
        if not error_message:
            validated_items.append(item)
        else:
            print(f"Invalid item: {item}")
            print(error_message)
            print("Removing item from list...")
            print()
    return validated_items


def validate_item(item, validated_items):
    if 'ID' not in item.keys():
        return 'ID field not found'
    if not isinstance(item['ID'], str) or item['ID'] == "":  # ID must be str and not empty
        return 'ID is not a non-empty string'
    try:
        int(item['ID'])  # ID must be a number
    except ValueError:
        return 'ID is not a number'
    for checked_item in validated_items:
        if checked_item['ID'] == item['ID']:  # ID must be unique
            return 'ID is not unique'
    
    if 'Type' not in item.keys():
        return 'Type field not found'
    if not isinstance(item['Type'], str) or item['ID'] == "":  # Type must be str and not empty
        return 'Type is not a non-empty string'
    if item['Type'] not in ITEM_TYPES:  # Type must be one of ITEM_TYPES
        return 'Type is not a valid item type'
    
    if 'Model' not in item.keys():
        return 'Model field not found'
    if not isinstance(item['Model'], str) or item['Model'] == "":  # Model must be str and not empty
        return 'Model is not a non-empty string'
    
    if 'Features' not in item.keys():
        return 'Features field not found'
    if not isinstance(item['Features'], str) and item['Features'] is not None:  # Features must be str (can be empty)
        return 'Features is not a string'
    
    if 'Rate' not in item.keys():
        return 'Rate field not found'
    if not isinstance(item['Rate'], float):  # Rate must be float
        return 'Rate must be a float'
    if not 0 <= item['Rate'] <= 5:  # Rate in range 0.0 - 5.0
        return 'Rate is not 0 to 5'
    
    if 'RateCount' not in item.keys():
        return 'RateCount field not found'
    if not isinstance(item['RateCount'], int) or item['RateCount'] < 0:  #RateCount must be non-negative int
        return 'RateCount is not a non-negative integer'

    if 'Status' not in item.keys():
        return 'Status field not found'
    if item['Status'] not in ["Available", "Being used", "Overdue", "Broken"]:  # Status must be one of Available, Being used, Overdue, Broken
        return 'Status is not Available, Being used, Overdue, or Broken'

    if 'User' not in item.keys():
        return 'User field not found'
    if not isinstance(item['User'], str) or item['User'] == "":  # User must be str and not empty
        return 'User is not a non empty string'

    if 'User email' not in item.keys():
        return 'User email field not found'
    if not isinstance(item['User email'], str) or item['User email'] == "":  # User email must be str and not empty
        return 'User email is not a non empty string'
    if item['User email'] != "n/a" and not '@' in item['User email']:  # User email must contain @ if it is not 'n/a'
        return 'User email does not contain @ or is not n/a'

    if 'Due by' not in item.keys():
        return 'Due by field not found'
    if not isinstance(item['Due by'], str) or item['Due by'] == "":  # Due by must be str and not empty
        return 'Due by is not a non empty string'
    # TODO Add validation for date format

    if 'Cost' not in item.keys():
        return 'Cost field not found'
    if not isinstance(item['Cost'], str) or item['Cost'] == "":  # Cost must be str and not empty
        return 'Cost is not a non empty string'
    if not '£' in item['Cost']:  # Cost must contain £
        return 'Cost does not contain £'
    try:
        if not 0 <= float(item['Cost'].lstrip('£')) <= 1000:  # Cost must be between 0 and 1000
            return 'Cost is not between £0 and £1000'
    except ValueError:
        return 'Cost is not £ followed by float'  # Cost with £ must be a float

    if 'Short description' not in item.keys():
        return 'Short description field not found'
    if not isinstance(item['Short description'], str) and item['Short description'] is not None:  # Features must be str (can be empty)
        return 'Short description is not a string'

    return None


# Combines columns (fields) with suitable widths and prints as a table
def print_table(columns, column_widths, items):

    # Print headings
    for column, column_width in zip(columns, column_widths):
        print(f"{column:{column_width}} ", end="")
    print()

    # Print items
    for row in items:
        for column, column_width in zip(columns, column_widths):
            value = row[column]
            print(f"{value:{column_width}} ", end="")
        print()


def print_items_list(items_list):
    print_table(
        [
            "ID",
            "Type",
            "Model",
            "Features",
            "Rate",
            "RateCount",
            "Status",
            "Due by",
            "Cost",
        ],
        ["<4", "<9", "<30", "<35", "<5", "<10", "<11", "<17", "<10"],
        items_list,
    )


def print_available_items(items_list):
    available_items = []
    for item in items_list:
        if item['Status'] == "Available":
            available_items.append(item)

    print_table(
        [
            "ID",
            "Type",
            "Model",
            "Features",
            "Rate",
            "RateCount",
            "Status",
            "Due by",
            "Cost",
        ],
        ["<4", "<9", "<30", "<35", "<5", "<10", "<11", "<17", "<10"],
        available_items,
    )


def view_item(item):

    print()

    # Print basic item details
    print(f"Type: {item['Type']}")
    print(f"Model: {item['Model']}")
    print(f"Features: {item['Features']}")
    print(
        f"This item has a rating of {item['Rate']} out of 5 from {item['RateCount']} users."
    )
    print(f"Short description: {item['Short description']}")
    print(f"Status: {item['Status']}")

    # Print information based on item status
    if item["Status"] == "Being used":
        print(
            f"This item is currently being used by {item['User']}. It is due to be returned by {item['Due by']}."
        )
    elif item["Status"] == "Overdue":
        print(
            f"This item is overdue! Contact {item['User']} at {item['User email']} to return it."
        )
    elif item["Status"] == "Broken":
        print(f"This item is broken and cannot be borrowed at this time.")
    
    # Pause so user can see the item before returning
    wait = input("\nPress any key to return to main menu.")


def borrow_item(item):
    
    if item is None:
        print("Item not found. Please double-check the ID.")
    elif item["Status"] != "Available":
        print("This item is not available for borrowing.")
    else:
        name = input("Please enter your name: ")
        
        email = input("Please enter your email address: ")
        # Validation - Presence Check
        while "@" not in email:
            print("Invalid email address. Please try again.")
            email = input("Please enter your email address: ")
        
        # Update the item fields
        item["Status"] = "Being used"
        item["User"] = name
        item["User email"] = email

        # Set the due date to 18:00 on the current day
        due_date = datetime.now().replace(hour=18,
                                          minute=0,
                                          second=0,
                                          microsecond=0)
        item["Due by"] = due_date.strftime("%Y-%m-%d %H:%M")

        print(
            f"You have borrowed the {item['Type']} with ID {item['ID']}. Please return it by {item['Due by']}."
        )

    input("\nEnter any key to return to main menu: ")


def return_item(item):
    if item["Status"] not in ["Being used", "Overdue"]:
        print("Please check you have entered the correct ID")
        return

    print(f"The {item['Type']} with ID {item['ID']} has been returned by {item['User']}.")
    item["Status"] = "Available"
    item["Due by"] = "n/a"
    item["User"] = "n/a"
    item["User email"] = "n/a"
    
    leave_rating = input("\nWould you like to leave a rating? (y/n): ").upper()
    if leave_rating == "Y":
        user_rating = rate_item(item)
        print(f"Thank you for your rating of {user_rating} out of 5.")
        
        new_rate = round((item["Rate"] * item["RateCount"] + user_rating) / (item["RateCount"] + 1), 1)
        new_rate_count = item["RateCount"] + 1

        for record in items_list:
            if record["Model"] == item["Model"]:
                record["Rate"] = new_rate
                record["RateCount"] = new_rate_count
        
    input("Enter any key to return to main menu: ")


def extend_duration(item):
    if item is None or item["Status"] != "Being used":
        print("\nPlease check you have entered the correct ID")
        return
    print("How much longer would you like to borrow the item for? Select an opiton below.")
    print("1. 1 day")
    print("2. 2 days")
    print("3. 3 days")
    print("4. 4 days")
    print("5. 5 days")
    
    while True:
        user_choice = input("\nEnter your choice: ")
        if user_choice not in ("1", "2", "3", "4", "5"):
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue
        else:
            user_choice = int(user_choice)
            item["Due by"] = (datetime.now() + timedelta(days=user_choice)).strftime("%Y-%m-%d %H:%M")
            print(f"You have extended the borrowing period of {item['Model']} to {user_choice} days. The new due date is {item['Due by']}.")
            break
    
    input("Enter any key to return to main menu: ")    


def admin_options():
    while True:
        print("\n--- Admin options menu ---\nDo not use unless you have admin privileges.")
        print("Create or Delete an item record from the table:")
        admin_action = input("Type C to create item\n  \"  D to delete item\n  \"  U to update status \n  \" (M for main menu)\n> ").upper()
        if admin_action == "M":
            break
        elif admin_action == "C":
            create_item()
        elif admin_action == "D":
            delete_item()
        elif admin_action == "U":
            update_item_status()
        else:
            print("Invalid option. Please try again.")


def create_item():
    print("Create a new item record.")
    print("* = mandatory")
    item_type = ask_for_type()
    item_model = input("*Enter the model of the item: ")
    item_features = input("Enter the features of the item: ")
    while True:
        try:
            item_cost = float(input("*Enter the cost of the item £"))
            # Validation - Range check
            if item_cost < 0 or item_cost > 1000:
                print("Please enter a cost between £0 - £1,000.")
                continue
        except ValueError:
            print("Please input a number.")
            continue
        break
    item_cost = f"£{item_cost}"
    item_short_description = input("Enter a short description of the item: ")
    item_id = str(int(items_list[-1]['ID']) + 1)  # Picks an ID that is 1 larger than the last in the list, so there will be no duplicates

    new_item = {
        'ID': item_id,
        'Type': item_type,
        'Model': item_model,
        'Feautres': item_features,
        'Rate': 0.0,
        'RateCount': 0,
        'Status': "Available",
        'User': "n/a",
        'User email': "n/a",
        'Due by': "n/a",
        'Cost': item_cost,
        'Short description': item_short_description,
    }

    add_new_item_to_list(items_list, new_item)


def add_new_item_to_list(list, item):
    list.append(item)
    print("Item created successfully.")


def ask_for_type():
    while True:
        item_type = input('Enter the type of item: ')
        # Validation - Presence Check
        if item_type == '':
            print('Type cannot be empty.')
            continue
        if item_type not in ITEM_TYPES:
            print(f'Invalid type. Select one of: {", ".join(ITEM_TYPES)}')
            continue
        return item_type


def ask_for_model():
    while True:
        item_model = input('Enter the model of the item: ')
        if item_model == '':
            print('Model cannot be empty.')
            continue
        return item_model


def ask_for_cost():
    while True:
        item_cost = input('Enter the cost of the item: ')
        # Validation - Presence Check
        if item_cost == '':
            print('Cost cannot be empty.')
            continue
        return item_cost


def delete_item():
    print("Permanently delete an item from the table. WARNING this cannot be undone!")
    
    # Allow user to cancel the deletion process
    user_choice = input("Type X to cancel or any other key to continue: ").upper()
    if user_choice == "X":
        return  
    
    item_id = input("Enter the ID of the item to delete: ")
    item = find_item_by_id(item_id)

    # Check item eligibility for deletion
    if item is None:
        print("Item with that ID does not exist.")
        return
    if item["Status"] == "Being used" or item["Status"] == "Overdue":
        print("Cannot delete item until the item is returned.")
        return

    # Confirm deletion from the user        
    delete_confirmation = input(f"Are you sure you want to delete the {item['Type']} {item['Model']} with ID {item['ID']}? (Y/N): ")
    if delete_confirmation.upper() == "Y":
        items_list.remove(item)
        print("Item deleted successfully.")
    else:
        print("Deletion cancelled.")


def update_item_status():
    while True:
        print("\n--- Update Item Status ---")
        choice = input("Type B to set Broken\n  \"  A to set Available\n  \"  M to return to Admin Menu\n> ").upper()

        if choice == "B":
            item_id = input("Enter the ID of the item to update: ")
            item = find_item_by_id(item_id)

            if item is None:
                print("\nItem not found.")
                continue

            if item["Status"] == "Available":
                item["Status"] = "Broken"
                print(f"\nItem {item_id} status set to Broken.")
            else:
                print(f"\nItem {item_id} cannot be set to Broken as it is currently {item['Status']}.")

        elif choice == "A":
            item_id = input("Enter the ID of the item to update: ")
            item = find_item_by_id(item_id)

            if item is None:
                print("\nItem not found.")
                continue

            if item["Status"] == "Broken":
                item["Status"] = "Available"
                print(f"\nItem {item_id} status set to Available.")
            else:
                print(f"\nItem {item_id} is not broken and cannot be set to Available.")

        elif choice == "M":
            break
        else:
            print("\nInvalid choice. Please try again.")


# Request ID from user
def get_item(action):
    while True:
        item_id = input(f"\nEnter the ID of an item to {action} (M for main menu): ")
        if item_id.upper() == "M":
            return "M"
        item = find_item_by_id(item_id)
        if item == None:
            print("Item not found. Please double-check the ID.")
            continue
        return item


# Find the item with the specified ID
def find_item_by_id(ID):
    for item in items_list:
        if item["ID"] == ID:
            return item


def rate_item(item):
    while True:
        try:
            rating = int(input("Please enter a rating (1-5): "))
        except ValueError:
            print("Input an integer.")
            continue
        if rating < 1 or rating > 5:  # Validation - Range Check
            print("Invalid rating. Please enter a number between 1 and 5.")
            continue
        return rating


def view_item_menu():
    while True:
        print("\n--- View item menu ---")
        print("1. View item")
        print("2. View available items only")
        print("3. View full details of an item")
        response = input("Enter your choice (M for main menu): ")
        if response == "1":
            return response
        elif response == "2":
            print_available_items(items_list)
        elif response == "3":
            while True:
                item_id = input(f"\nEnter the ID of an item to view in full details: ")
                item = find_item_by_id(item_id)
                if item == None:
                    print("Item not found. Please double-check the ID.")
                    continue
                break
            view_full_details(item)
            continue
        else:
            break

def view_full_details(item):
    print()
    print(f"ID: {item['ID']}")
    print(f"Type: {item['Type']}")
    print(f"Model: {item['Model']}")
    print(f"Features: {item['Features']}")
    print(f"Rate: {item['Rate']}")
    print(f"Rate Count: {item['RateCount']}")
    print(f"Status: {item['Status']}")
    print(f"User: {item['User']}")
    print(f"User email: {item['User email']}")
    print(f"Due by: {item['Due by']}")
    print(f"Cost: {item['Cost']}")
    print(f"Short description: {item['Short description']}")
    wait = input("\nPress any key to return to View item menu.")

    
def main():
    """
    Main function to run the application. It initializes the system, displays the main menu, 
    and handles user interactions.
    """

    print("\nWelcome to L&G's IT Asset borrowing system!\nVersion 1.0\n")

    global items_list
    items_list = validate_data(items_list)  # Removes invalid items

    # Loop of the main menu
    returning_to_main_menu = False
    while True:
        if returning_to_main_menu:
            print("\nReturning to main menu...\n")
        returning_to_main_menu = True

        print_items_list(items_list)
        print_menu_options()

        choice = input("Enter your choice: ")

        # Handling menu options
        if choice == "1":
            view_item_choice = view_item_menu()
            if view_item_choice == "1":
                item_id = get_item("view")
                if item_id == "M":
                    continue
                view_item(item_id)
        elif choice == "2":
            item_id = get_item("borrow")
            if item_id == "M":
                continue
            borrow_item(item_id)
        elif choice == "3":
            item_id = get_item("return")
            if item_id == "M":
                continue
            return_item(item_id)
        elif choice == "4":
            item_id = get_item("extend")
            if item_id == "M":
                continue
            extend_duration(item_id)
        elif choice == "5":
            admin_options()
        elif choice == "6":
            exit_confirmation = input("Are you sure you want to exit? (Y/N): ").upper()
            if exit_confirmation == "Y":
                print("Thank you for using L&G's IT Asset borrowing system!")
                print("Exiting the program.")
                break
            else:
                input("Enter any key to return to main menu: ")
                continue
        else:
            print("Invalid choice. Please enter a number 1 to 6.")
            input("Press any key to return to main menu: ")


if __name__ == "__main__":
    main()
