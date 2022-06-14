from app import app
from flask import render_template, redirect, url_for, request
import json
import os
from app.models.product import Product

@app.route('/')
def index():
    return render_template("index.html.jinja")

@app.route('/extract', methods = ["POST", "GET"])
def extract():
    if request.method == "POST":
        product_id = request.form.get("product_id")
        product = Product(product_id)
        product.extract_name()
        if product.product_name:
            product.extract_opinions()
            product.export_opinions()
            product.export_product()
        else:
            error = "Upss.."
            return redirect(url_for('product', product_id=product_id))

        return redirect(url_for('product', product_id=product_id))
    else:
        return render_template("extract.html.jinja")
        
@app.route('/products')
def products():
    products = [filename.split(".")[0] for filename in os.listdir("app/opinions")]
    return render_template("products.html.jinja", products=products)

@app.route('/about')
def about():
    return render_template("about.html.jinja")

@app.route('/product/<product_id>')
def product(product_id):

    return render_template("product.html.jinja", product_id=product_id, stats=stats, opinions=opinions)
