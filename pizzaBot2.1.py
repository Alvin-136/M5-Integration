import tkinter as tk

# GUI function to update chat log
def update_chat(text):
    chat_log.insert(tk.END, text + "\n")

# When "Place Order" is clicked
def place_order():
    size = size_var.get()
    topping = topping_var.get()
    drink = drink_var.get()

    update_chat(f"You: I'd like a {size} pizza with {topping} and a {drink}.")
    update_chat(f"PizzaBot: Great choice! A {size} pizza with {topping} and {drink} is on its way. 🍕🥤")

# Main window
root = tk.Tk()
root.title("PizzaBot v3.0")

# Chat log
chat_log = tk.Text(root, width=100, height=15, bg="mint cream", font=("Arial", 12))
chat_log.pack(padx=10, pady=10)

# Dropdown options
sizes = ["Small", "Medium", "Large"]
toppings = ["Cheese", "Pepperoni", "Mix"]
drinks = ["No Drink", "Cola", "Pepsi", "Sprite"]

# Variables to store selected values
size_var = tk.StringVar(value=sizes[0])
topping_var = tk.StringVar(value=toppings[0])
drink_var = tk.StringVar(value=drinks[0])

# Dropdown Menus
form_frame = tk.Frame(root)
form_frame.pack(pady=5)

tk.Label(form_frame, text="Choose Size:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
tk.OptionMenu(form_frame, size_var, *sizes).grid(row=0, column=1, padx=5)

tk.Label(form_frame, text="Choose Topping:", font=("Arial", 12)).grid(row=1, column=0, padx=5)
tk.OptionMenu(form_frame, topping_var, *toppings).grid(row=1, column=1, padx=5)

tk.Label(form_frame, text="Choose Drink:", font=("Arial", 12)).grid(row=2, column=0, padx=5)
tk.OptionMenu(form_frame, drink_var, *drinks).grid(row=2, column=1, padx=5)

# Submit Button
order_button = tk.Button(root, text="Place Order", command=place_order, bg="tomato", font=("Arial", 12))
order_button.pack(pady=10)

root.mainloop()
