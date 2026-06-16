import json
import os

class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

# Load existing expenses or start fresh
if os.path.exists("expenses.json"):
    with open("expenses.json") as f:
        expenses = json.load(f)
else:
    expenses = []

# Get new expense from user
name = input("Expense name: ")
amount = int(input("Amount: "))
category = input("Category: ")

# Create expense object and save to list
new_expense = Expense(name, amount, category)
expenses.append({
    "name": new_expense.name,
    "amount": new_expense.amount,
    "category": new_expense.category
})

# Save updated list to file
with open("expenses.json", "w") as f:
    json.dump(expenses, f)

# Calculate and print total
total = 0
for expense in expenses:
    total += expense["amount"]

print("Total spent:", total)