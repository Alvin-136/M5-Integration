import tkinter as tk
import os

# Price dictionaries
price_size = {"Small": 5, "Medium": 8, "Large": 12}
price_topping = {"Cheese": 1, "Pepperoni": 2, "Mix": 3}
price_drink = {"No Drink": 0, "Cola": 1.5, "Pepsi": 1.5, "Sprite": 1.5}
price_crust = {"Thin Crust": 0, "Cheese Crust": 2, "Normal Crust": 0}

# GUI function to update chat log
def update_chat(text):
    chat_log.insert(tk.END, text + "\n")

# Save order to a file
def save_order(size, topping, drink, crust, price):
    with open("orders.txt", "a") as file:  # Append mode
        file.write(f"{size} pizza with {topping}, {drink}, {crust} - ${price:.2f}\n")

# View order history
def view_history():
    if os.path.exists("orders.txt"):
        with open("orders.txt", "r") as file:
            history = file.readlines()
        if history:
            update_chat("📜 PizzaBot: Here is your order history:")
            for order in history:
                update_chat("  - " + order.strip())
        else:
            update_chat("📜 PizzaBot: No previous orders found.")
    else:
        update_chat("📜 PizzaBot: No previous orders found.")

# When "Place Order" is clicked
def place_order():
    size = size_var.get()
    topping = topping_var.get()
    drink = drink_var.get()
    crust = crust_var.get()

    # Calculate total price
    total_price = price_size[size] + price_topping[topping] + price_drink[drink] + price_crust[crust]

    update_chat(f"You: I'd like a {size} pizza with {topping}, {drink}, {crust}.")
    update_chat(f"PizzaBot: Great choice! That will be ${total_price:.2f}. Your order is saved! 🍕🥤")

    # Save to file
    save_order(size, topping, drink, crust, total_price)

# Cancel order
def cancel_order():
    update_chat("You: I'd like to cancel my order.")
    update_chat("PizzaBot: Sorry to hear that! Come back any time. 🍕🥤")

# Main window
root = tk.Tk()
root.title("PizzaBot v3.3 - Order History")

# Chat log
chat_log = tk.Text(root, width=100, height=15, bg="mint cream", font=("Arial", 12))
chat_log.pack(padx=10, pady=10)

# Dropdown options
sizes = list(price_size.keys())
toppings = list(price_topping.keys())
drinks = list(price_drink.keys())
crusts = list(price_crust.keys())

# Variables to store selected values
size_var = tk.StringVar(value=sizes[0])
topping_var = tk.StringVar(value=toppings[0])
drink_var = tk.StringVar(value=drinks[0])
crust_var = tk.StringVar(value=crusts[0])

# Dropdown Menus
form_frame = tk.Frame(root)
form_frame.pack(pady=5)

tk.Label(form_frame, text="Choose Size:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
tk.OptionMenu(form_frame, size_var, *sizes).grid(row=0, column=1, padx=5)

tk.Label(form_frame, text="Choose Topping:", font=("Arial", 12)).grid(row=1, column=0, padx=5)
tk.OptionMenu(form_frame, topping_var, *toppings).grid(row=1, column=1, padx=5)

tk.Label(form_frame, text="Choose Drink:", font=("Arial", 12)).grid(row=2, column=0, padx=5)
tk.OptionMenu(form_frame, drink_var, *drinks).grid(row=2, column=1, padx=5)

tk.Label(form_frame, text="Choose Crust:", font=("Arial", 12)).grid(row=3, column=0, padx=5)
tk.OptionMenu(form_frame, crust_var, *crusts).grid(row=3, column=1, padx=5)

# Buttons
order_button = tk.Button(root, text="Place Order", command=place_order, bg="tomato", font=("Arial", 12))
order_button.pack(pady=5)

cancel_button = tk.Button(root, text="Cancel Order", command=cancel_order, bg="orange", font=("Arial", 12))
cancel_button.pack(pady=5)

history_button = tk.Button(root, text="View Order History", command=view_history, bg="lightblue", font=("Arial", 12))
history_button.pack(pady=5)

root.mainloop()
