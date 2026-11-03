menu = {
    "coffee": 50,
    "tea": 20,
    "burger": 80,
    "pizza": 150,
    "pasta": 100,
    "momos": 70
}

total_sales = 0

def show_menu():           
    print("\n====== MENU CARD =====")
    print("------------------------------")
    for item, price in menu.items():
        print(f"{item.capitalize():10} | ₹{price:3}")
    print("----------------------------")


def order():
    global total_sales
    bill = 0
    cart = []   
    while True:
        show_menu()
        item = input("\nEnter item name (or type 'done' to finish): ").lower()

        if item in ["done", "finish", "exit"]:
            break

        if item in menu:
            while True:
                try:
                    quantity = int(input(f"Enter quantity for {item}: "))
                    if quantity <= 0:
                        print("Quantity must be positive!")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number!")

            cost = menu[item] * quantity
            bill += cost
            cart.append(f"{quantity} × {item} = ₹{cost}")
            print(f"Added → {quantity} × {item} = ₹{cost}")
        else:
            print("Sorry, item not available in menu.")

    if bill > 0:
        print("\n" + "="*30)
        print("      YOUR ORDER SUMMARY")
        print("="*30)
        for line in cart:
            print(line)
        print("-"*30)
        print(f"Total Bill : ₹{bill}")
        print("="*30)
    else:
        print("\nNo items were ordered.")

    total_sales += bill
    input("\nPress Enter to continue...")


def feedback():
    print("\n======== FEEDBACK =======")
    name = input("Enter your name: ")
    while True:
        try:
            rating = int(input("Rate our cafe (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Please enter number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

    comment = input("Your feedback / suggestions: ")
    print("\nThank you so much for your feedback!")
    print(f"{name}, you gave us {rating}/5")
    print("Comment:", comment if comment else "No comment")
    input("\nPress Enter to continue...")


def report():
    print("="*35)
    print("      CAFE SALES REPORT")
    print("=============================")
    print(f"Today's Total Sales : ₹{total_sales}")
    print("=============================")
    input("\nPress Enter to continue...")


def main():
    while True:
        print("\n" + "="*30)
        print("     CAFE MANAGEMENT SYSTEM")
        print("="*30)
        print(" 1 → Show Menu")
        print(" 2 → Place Order")
        print(" 3 → Give Feedback")
        print(" 4 → View Sales Report")
        print(" 5 → Exit")
        print("-"*30)

        try:
            ch = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Please enter a number!")
            continue

        if ch == 1:
            show_menu()
            input("\nPress Enter to continue...")
        elif ch == 2:
            order()
        elif ch == 3:
            feedback()
        elif ch == 4:
            report()
        elif ch == 5:
            print("\nThank you for visiting our Cafe!")
            print("Visit Again... ❤️")
            break
        else:
            print("Invalid choice! Please select 1 to 5.")


if __name__ == "__main__":
    main()
