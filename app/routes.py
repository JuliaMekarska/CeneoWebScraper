from app import app
from flask import render_template, redirect, url_for, request
import json
import os
from app.models.product import Product

def get_item(ancestor, selector, attribute = None, return_list = False):
    try:
        if return_list:
            return [item.get_text().strip() for item in ancestor.select(selector)]
        if attribute:
            return ancestor.select_one(selector)[attribute]
        return ancestor.select_one(selector).get_text().strip()
    except (AttributeError, TypeError):
        return None

selectors = {
    "author": ["span.user-post__author-name"],
    "recommendation":["span.user-post__author-recomendation > em"],
    "stars":["span.user-post__score-count"],
    "content":["div.user-post__text"],
    "useful":["button.vote-yes > span"],
    "useless":["button.vote-no > span"],
    "published":["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchased":["span.user-post__published > time:nth-child(2)", "datetime"],
    "pros":["div[class$=positives] ~ div.review-feature__item", None, True],
    "cons":["div[class$=negatives] ~ div.review-feature__item", None, True]
}

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
            product.extract_opinions().calculate_stats().draw_charts()
        else:
            pass

        if not os.path.exists("app/opinions"):
            os.makedirs("app/opinions")

        with open(f"app/opinions/{product_id}.json", "w", encoding ="UTF-8") as jf:
            json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
        print(product_id)
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
