from flask import Flask, render_template

from app import app

@app.route("/")
@app.route("/<name>")
def hello(name = "world"):
    return render_template("index.html", name = name )

@app.route("extract")
def hello():
    return render_template("extract.html")

@app.route("product")
def hello():
    return render_template("products.html")

@app.route("/eprduct/<product_id>")
def hello(product_id):
    return render_template("product.html", product_id = product_id)

@app.route("author")
def hello(product_id):
    return render_template("author.html")



