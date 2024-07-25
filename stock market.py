import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class StockMarketApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Stock Market App")

        # Initialize user account data
        self.user_account = {
            "username": "USER",
            "balance": 100000,  # Initial balance for the user
        }

        # Login Frame
        self.login_frame = tk.Frame(root, bg="#fff8dc")  # Light green background color
        self.login_frame.pack(padx=20, pady=20)

        # Username Label and Entry
        tk.Label(self.login_frame, text="Username:", bg="#c1ffc1").grid(row=0, column=0, sticky=tk.W)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        # Password Label and Entry
        tk.Label(self.login_frame, text="Password:", bg="#c1ffc1").grid(row=1, column=0, sticky=tk.W)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Login Button
        tk.Button(self.login_frame, text="Login", command=self.login, bg="#c1ffc1", bd=3, relief=tk.RAISED).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.login_frame, text="Create Account", command=self.create_account, bg="#c1ffc1", bd=3, relief=tk.RAISED).grid(row=3, column=0, columnspan=2, pady=10)

    def destroy_frame(self, frame):
        frame.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Perform authentication (for demonstration purposes, let's assume username='prateeth' and password='prateeth123')



    if username == "prateeth" and password == "prateeth123" or username == "Nanjundi" and password == "Nanjundi123" or username == "omprakash" and password == "omprakash123" or username == "anil" and password == "anil123":
            self.destroy_frame(self.login_frame)
            self.show_stock_market_data()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Try again.")

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            messagebox.showinfo("Success", "Account created successfully")
            self.destroy_frame(self.login_frame)
            self.show_stock_market_data()
        else:
            messagebox.showerror("Error", "Username and password are required")

    def show_stock_market_data(self):
        # Destroy login frame
        self.destroy_frame(self.login_frame)

        # Stock Market Frame
        self.stock_frame = tk.Frame(self.root, bg="#d3ffd3")  # Light green background color
        self.stock_frame.pack(padx=20, pady=20)

        # Create a ttk Treeview widget
        tree = ttk.Treeview(self.stock_frame, columns=('Stock Name', 'Symbol', 'Price', "value (cr)", 'Total Holdings'))

        # Insert data into the table
        # Define the columns
        tree.heading('#0', text='Holder')
        tree.heading('#1', text='Stock Name')
        tree.heading('#2', text='Symbol')
        tree.heading('#3', text='Price')
        tree.heading('#4', text="value (cr)")
        tree.heading('#5', text='Total Holdings')
        stocks = [
            ("Tata inv crop", "TIC", "4501", 2195.36, 30),
            ("HDFC Bank", "HDFC", "1505.20", 1455.14, 25),
            ("Bajaj finance", "Bj", "7068.60", 1354.58, 11),
            ("ICICI Bank", "IC", "921.45", 974.59, 20),
            ("Adani Total Gas", "ATS", "570.65", 4.525, 50),
            ("s&p500 ", "SP", "134", 16.59, 100),
            ("vedanta", 'VD', "239.55", 42.19, 100),
            ("suzlon energy", 'SE', "39.90", 55.65, 10),
            ("JSW Steel", 'JSW', "773.30", 18628.2, 20)
            # Add more stocks as needed
        ]

        for i, stock in enumerate(stocks, start=1):
            tree.insert('', i, text=str(i), values=stock)

        # Add the Treeview to the window
        tree.pack(expand=True, fill=tk.BOTH)

        # Buy and Sell Buttons
        tk.Button(self.stock_frame, text="Buy Stock", command=self.buy_stock, bg="#FF83FA", bd=3, relief=tk.RAISED).pack(side=tk.LEFT, padx=10)
        tk.Button(self.stock_frame, text="Sell Stock", command=self.sell_stock, bg="#FF83FA", bd=3, relief=tk.RAISED).pack(side=tk.LEFT, padx=10)

    def buy_stock(self):
        buy_frame = tk.Toplevel(self.root)
        buy_frame.title("Buy Stock")
        buy_frame.configure(bg="#d3ffd3", bd=5, relief=tk.RIDGE)  # Light green background color, 5-pixel border with RIDGE relief

        tk.Label(buy_frame, text="Stock Name:", bg="#d3ffd3").grid(row=0, column=0, sticky=tk.W)
        stock_name_entry = tk.Entry(buy_frame)
        stock_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(buy_frame, text="Quantity:", bg="#d3ffd3").grid(row=1, column=0, sticky=tk.W)
        quantity_entry = tk.Entry(buy_frame)
        quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(buy_frame, text="Buy", command=lambda: [self.process_transaction(stock_name_entry.get(), quantity_entry.get(), "buy"), self.destroy_frame(buy_frame)], bg="#FF83FA", bd=3, relief=tk.RAISED).grid(row=2, column=0, columnspan=2, pady=10)

    def sell_stock(self):
        sell_frame = tk.Toplevel(self.root)
        sell_frame.title("Sell Stock")
        sell_frame.configure(bg="#d3ffd3", bd=5, relief=tk.RIDGE)  # Light green background color, 5-pixel border with RIDGE relief

        tk.Label(sell_frame, text="Stock Name:", bg="#d3ffd3").grid(row=0, column=0, sticky=tk.W)
        stock_name_entry = tk.Entry(sell_frame)
        stock_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(sell_frame, text="Quantity:", bg="#d3ffd3").grid(row=1, column=0, sticky=tk.W)
        quantity_entry = tk.Entry(sell_frame)
        quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(sell_frame, text="Sell", command=lambda: [self.process_transaction(stock_name_entry.get(), quantity_entry.get(), "sell"), self.destroy_frame(sell_frame)], bg="#FF83FA", bd=3, relief=tk.RAISED).grid(row=2, column=0, columnspan=2, pady=10)

    def process_transaction(self, stock_name, quantity, transaction_type):
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("Quantity must be a positive integer.")
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity. Please enter a positive integer.")
            return

        # For simplicity, assume each stock has a fixed price
        stock_prices = {"Tata inv crop": 4501, "HDFC Bank": 1505.20, "Bajaj finance": 7068.60,
                        "ICICI Bank": 921.45, "Adani Total Gas": 570.65, "vedanta": 239.55, "suzlon energy": 39.90,
                        "JSW Steel": 773.30}

        if stock_name not in stock_prices:
            messagebox.showerror("Error", f"Invalid stock name: {stock_name}")
            return

        total_cost = stock_prices[stock_name] * quantity

        if transaction_type == "buy":
            if total_cost > self.user_account["balance"]:
                messagebox.showerror("Insufficient Funds", "You don't have enough funds to buy this stock.")
            else:
                self.user_account["balance"] -= total_cost
                messagebox.showinfo("Success", f"You have successfully bought {quantity} shares of {stock_name} stock for ₹ {total_cost}.")
                self.show_receipt(stock_name, quantity, total_cost)
        elif transaction_type == "sell":
            # For simplicity, assume the user has the stocks they want to sell
            self.user_account["balance"] += total_cost
            messagebox.showinfo("Success", f"You have successfully sold {quantity} shares of {stock_name} stock for ₹ {total_cost}.")
            self.show_receipt(stock_name, quantity, total_cost)
        else:
            messagebox.showerror("Error", "Invalid transaction type.")

        # Update the user's account information (for demonstration purposes)
        print("Updated User Account:", self.user_account)

    def show_receipt(self, stock_name, quantity, total_cost):
        receipt_frame = tk.Toplevel(self.root)
        receipt_frame.title("Receipt")
        receipt_frame.configure(bg="lightblue", bd=10, relief=tk.RIDGE)  # Light green background color, 5-pixel border with RIDGE relief

        tk.Label(receipt_frame, text="Receipt", font=("Helvetica", 16, "bold"), bg="lightblue").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(receipt_frame, text=f"Stock Name: {stock_name}", bg="lightblue").grid(row=1, column=0, sticky=tk.W)
        tk.Label(receipt_frame, text=f"Quantity: {quantity}", bg="lightblue").grid(row=2, column=0, sticky=tk.W)
        tk.Label(receipt_frame, text=f"Total Cost: ₹ {total_cost}", bg="lightblue").grid(row=3, column=0, sticky=tk.W)
        remaining_balance_label = tk.Label(receipt_frame, text=f"Remaining Balance: ₹ {self.user_account['balance']}", bg="lightblue")
        remaining_balance_label.grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(receipt_frame, text="print", command=lambda: [self.destroy_frame(receipt_frame), self.root.destroy()], bg="white", bd=3, relief=tk.RAISED).grid(row=5, column=0, columnspan=2, pady=10)

# Main function to run the program
def main():
    root = tk.Tk()
    app = StockMarketApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()