import sys
import csv
from csv import DictReader
from csv import DictWriter


class Product:
    def __init__(self, name, unit, unit_price, quantity):
        self.name = name
        self.unit = unit
        self.unit_price = unit_price
        self.quantity = quantity


def export_items_to_csv():
    with open('magazyn.csv', 'w', newline='') as csvfile:
    #with open(sys.argv[1], 'w', newline='') as csvfile:
        fieldnames = ["name", "quantity", "unit", "unit_price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in items:
            writer.writerow(item)
    return "Stock data export completed successfully!"

def export_sales_to_csv():
    with open('sales.csv', 'a', newline='') as csvfile:
        fieldnames = ["name", "quantity", "unit", "unit_price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in sold_items:
            writer.writerow(item)
    return "Sale data export completed successfully!"

def load_items_from_csv():
    items.clear()
    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(row['name'], row['quantity'], row['unit'], row['unit_price'])
            items.append(row)