import os
import csv
import argparse
from datetime import datetime

if os.path.exists('../data/expenses.csv'):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "category", 
        nargs='?',
        default="Food", 
        type=str.capitalize, 
        help="The category to generate a report for (default: Food)"
    )
    args = parser.parse_args()
    with open('../data/expenses.csv', 'r') as file:
        records = list(csv.DictReader(file))
    
        for row in records:
            row['amount'] = float(row['amount'])

        filtered = [row for row in records if row['category'] == args.category]
        total = sum(row['amount'] for row in filtered)

        today = datetime.now().strftime("%B %d, %Y")
        with open(f"{args.category.lower()}_report.txt", 'w') as file:
            file.write(f"{args.category} Expense Report - generated {today}\n")

            for row in filtered:
                file.write(f"{row['date']}: ${row['amount']:.2f}\n")

            file.write(f"Total: ${total:.2f}")
                
else:
    print("expenses.csv not found.")