from flask import Flask, render_template,jsonify, request
from database import load_product_from_db, load_products_from_db

app = Flask (__name__)

@app.route ('/')
def hello_world ():
  productss = load_product_from_db()
  return render_template('home.html', products=productss)

@app.route("/api/products")
def list_products():
  productss = load_product_from_db()
  return jsonify(productss)

@app.route("/product/<id>")
def show_product(id):
  product = load_products_from_db(id)

  if not product:
    return "Product not found", 404
  return render_template('product_info.html', product=product)



@app.route("/product/<id>/apply", methods=['post'])
def apply_to_buy(id):
  data = request.form

  product = load_products_from_db(id)

  return render_template('application_submitted.html', 
                         application=data,
                        product=product)



if __name__ == '__main__':
  app.run (host='0.0.0.0', debug = True)	