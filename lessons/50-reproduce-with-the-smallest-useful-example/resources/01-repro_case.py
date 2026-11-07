import argparse
import csv
from decimal import Decimal

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("--category", required=True)
parser.add_argument("--from-date", required=True)
parser.add_argument("--to-date", required=True)
args = parser.parse_args()

total = Decimal("0.00")
with open(args.input_file, newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        if (
            row["category"] == args.category
            and args.from_date < row["date"] <= args.to_date
        ):
            total += Decimal(row["amount"])

print(f"Total: {total:.2f}")
