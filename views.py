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
@app.route('/product_list/', methods=["GET", "POST"])
def export_items_to_csv():
    form = ProductForm()
    error = ""
    #items = Product(form.data['name'], form.data['quantity'], form.data['unit'], form.data['unit_price'])
    #ITEMS[form.data['name']] = Product(form.data['name'], form.data['unit'], form.data['unit_price'], form.data['quantity'])
    #items = ITEMS[form.data['name']]
    items = ITEMS[Product]
    if request.method == "POST":
        with open('magazyn.csv', 'w', newline='') as csvfile:
        #with open(sys.argv[1], 'w', newline='') as csvfile:
            fieldnames = ["name", "quantity", "unit", "unit_price"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            #for item in ITEMS[form.data['name']]:
            for item in items:
            #for item in ITEMS(values):
            #for item in Product(form.data['name'], form.data['quantity'], form.data['unit'], form.data['unit_price']):
                writer.writerow(item)
        return render_template("product_list.html", form=form, fieldnames=fieldnames, csvfile=csvfile, items=ITEMS, error=error)
    #return "Stock data export completed successfully!"



if __name__ == '__main__':
    app.run(debug=True)