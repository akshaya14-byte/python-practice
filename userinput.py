#shopping cart program
cart = []

while True:
    print("Welcome to the shopping cart program!")
    print("You can add items to your cart.")
    item = input("Enter the item you want to add to the cart: " )
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))

    cart.append({"item": item, "quantity": quantity, "price": price})
    choice = input("Do you want to add more items to the cart? (yes/no)").lower()
    if choice == "no":
            break
    
print("Your shopping cart contains:")
subtotal = [i["quantity"] * i["price"] for i in cart]
for i in cart:
    print(f"Item: {i['item']}, Quantity: {i['quantity']}, Price: ${i['price']}")
    print(f"Subtotal: ${i['quantity'] * i['price']}")
total = sum([i["quantity"] * i["price"] for i in cart])
print(f"Total: ${total}")
print("Thank you for shopping with us!")