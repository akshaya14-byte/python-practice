#shopping cart program
while True:
    print("Welcome to the shopping cart program!")
    print("You can add items to your cart.")
    item = input("Enter the item you want to add to the cart: " )
    quantity = input("Enter the quantity: ")
    price = input("Enter the price: ")
    cart = []
    cart.append({"item": item, "quantity": quantity, "price": price})
    choice = input("Do you want to add more items to the cart? (yes/no)").lower()
    if choice == "yes":
        item = input("Enter the item you want to add to the cart: " )
        quantity = input("Enter the quantity: ")
        price = input("Enter the price: ")
        cart.append({"item": item, "quantity": quantity, "price": price})
        if choice == "no":
            break
    else:
        print("No more items to add.")
print("Your shopping cart contains:")
for i in cart:
    print(f"Item: {i['item']}, Quantity: {i['quantity']}, Price: {i['price']}")