# Empty variables to store items and prices
items = []
prices = []
total_cost = 0

done = False

while not done:
    print("")
    print("-+" * 12 + " " + "CB'S MOTOR SUPPLIES STORE" + " " + "-+" * 12)
    print("-" * 75)
    print("""Please select one of the following:

    1. Add item to cart
    2. Remove item from cart
    3. View total cost of cart and items
    4. Checkout
    """)

    # Add items to baskets
    selection = int(input("Please enter the number of the option you would like to choose:\n"))
    if selection == 1:
        item = input("What item would you like to add to your cart: ")
        price = float(input("How much does the item cost: £"))
        
        items.append(item)
        prices.append(price)
        
        print(f"{item} has been added to your cart")
    elif selection == 2:
        remove_item = input("Enter the item you would like to remove: ")
        
        # Remove items from basket
        if remove_item in items:
            index = items.index(remove_item)
            items.remove(remove_item)
            prices.pop(index)
            
            print(f"{remove_item} has been removed from your cart")
        else:
            print("That item is not in your cart")
            
    elif selection == 3:
        for i in prices:
            total_cost += i   # For loop to calculate the total cost in basket
        
        items_space = ", ".join(items)
        print("-" *75)
        print(f"The Items in your cart are: {items_space}")  # Print the items in basket
        print(f"The total of your basket is: £{total_cost}")  # Print the total basket value
        print("-" * 75)

    elif selection == 4:
        print("\nThank you for shopping at CB'S MOTOR SUPPLIES")
        done = True

    else:
        print("This is not a valid option")