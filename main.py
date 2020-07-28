from flask import Flask, render_template, jsonify, url_for, request
import sys
import logging
import tabulate
import csv
from csv import DictReader
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

#items = [{"Name": "Milk", "Quantity": 120, "Unit": "l", "Unit Price (PLN)": 2.3}, {"Name": "Sugar", "Quantity": 1000, "Unit": "kg", "Unit Price (PLN)": 3}, {"Name": "Flour", "Quantity": 12000, "Unit": "kg", "Unit Price (PLN)": 1.2}, {"Name": "Coffee", "Quantity": 25, "Unit": "kg", "Unit Price (PLN)": 40}]
#sold_items = []
#list_of_dict = []


@app.route('/')
def homepage():
    return render_template("base.html")


class Product:
   def __init__(self, name, quantity, unit, unit_price):
       self.name = name
       self.quantity = quantity
       self.unit = unit
       self.unit_price = unit_price

Milk = Product(name="Milk", quantity=120, unit="l", unit_price=2.3)
Sugar = Product(name="Sugar", quantity=1000, unit="kg", unit_price=3)
Flour = Product(name="Flour", quantity=12000, unit="kg", unit_price=1.2)
Coffee = Product(name="Coffee", quantity=25, unit="kg", unit_price=40)

items = []

items.append(Milk)
items.append(Sugar)
items.append(Flour)
items.append(Coffee)

@app.route('/product_list')
def get_items():
    items=items
    return render_template("product_list.html", items=items)

