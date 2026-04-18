print("="*25)
name = input("Enter your name: ")
budget = float(input("Enter your weekly budget: "))

categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]
print("="*25)
print("\nWEEKLY EXPENSE -- CATEGORIES")
for i in range(len(categories)):
    print(f"{i+1}. {categories[i]}")

expenses = []
total_spent = 0

for i in range(4):
    print("="*26)
    print(f"\n--- EXPENSE {i+1} ---")
    cat_num = int(input("Category (0 to skip): "))

    if cat_num == 0:
        print("Skipped.")
        continue

    if 1 <= cat_num <= 5:
        desc = input("Description: ")
        amount = float(input("Amount: "))

        high_expense = ""
        if amount > 0.25 * budget:
            high_expense = " ! High Expense Alert!"

        expenses.append({
            "category": categories[cat_num - 1],
            "description": desc,
            "amount": amount,
            "alert": high_expense
        })

        total_spent += amount
    else:
        print("Invalid category. Skipped.")

remaining = budget - total_spent

if remaining > 0:
    status = "Budget OK! Keep it up."
elif remaining == 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending!"

print("\n========================================")
print(f"{name.upper()} -- WEEKLY EXPENSE LOG")
print("========================================")
print(f"Weekly Budget : P{budget:.2f}")

for i, exp in enumerate(expenses):
    print(f"[{i+1}] {exp['category']}")
    print(f"    {exp['description']}")
    print(f"    P{exp['amount']:.2f}{exp['alert']}")

print("----------------------------------------")
print(f"Total Spent : P{total_spent:.2f}")
print(f"Remaining   : P{remaining:.2f}")
print(f"Status      : {status}")
print("========================================")
