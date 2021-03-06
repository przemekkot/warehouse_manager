from flask import Flask, render_template, request, url_for, redirect, flash
from forms import ProductForm, ProductSaleForm
from client import Product
import sys
import csv
from csv import DictReader
from csv import DictWriter


app = Flask(__name__)
app.config["SECRET_KEY"] = "zyrafyidadoszafy"


ITEMS = {"Milk" : Product("Milk", "l", 2.3, 120),
         "Sugar" : Product("Sugar", "kg", 3, 1000),
         "Flour" : Product("Flour", "kg", 1.2, 12000),
         "Coffee" : Product("Coffee", "kg", 40, 25)}


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/products/', methods=["GET", "POST"])
def product_list():
    form = ProductForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            # jeśli klucz istnieje ilość i cena się nadpiszą
            ITEMS[form.data['name']] = Product(form.data['name'], form.data['unit'], form.data['unit_price'], form.data['quantity'])
        else:
            error = form.errors
        return redirect(url_for("product_list"))
    return render_template("product_list.html", items=ITEMS, form=form, error=error)


@app.route('/sell/<product_name>', methods=["GET", "POST"])
def sell_product(product_name):
    form = ProductSaleForm()
    error = ""
    if request.method == "POST":
        ITEMS[product_name].quantity -= form.data['quantity']
        return redirect(url_for("product_list"))
    return render_template("sell_product.html", form=form, product_name=product_name, items=ITEMS, error=error)


# Export do pliku csv
@app.route('/product_list/', methods=["POST"])
def export_items_to_csv():
    form = ProductForm()
    error = ""
    if request.method == "POST":
        with open('magazyn.csv', 'w', newline='') as csvfile:
        #with open(sys.argv[1], 'w', newline='') as csvfile:
            fieldnames = ["name", "quantity", "unit", "unit_price"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in ITEMS.values():
                record = {"name" : item.name, "quantity" : item.quantity, "unit": item.unit, "unit_price" : item.unit_price}
                writer.writerow(record)
        return render_template("product_list.html", form=form, fieldnames=fieldnames, csvfile=csvfile, items=ITEMS, error=error)


# Import z pliku csv
@app.route('/product_list/', methods=["GET"])
def import_items_from_csv():
    form = ProductForm()
    error = ""
    if request.method == "GET":
        with open('magazyn.csv', newline='') as csvfile:
            fieldnames = ["name", "quantity", "unit", "unit_price"]
            reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=',')
            ITEMS.clear()
            for row in reader:
                if row["name"] != "name":
                    ITEMS[row["name"]] = Product(row["name"], row["unit"], row["unit_price"], row["quantity"])
        return render_template("product_list.html", form=form, items=ITEMS, error=error)


if __name__ == '__main__':
    app.run(debug=True)