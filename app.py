from flask import Flask, render_template,jsonify
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

# @app.route("/api/job/<id>")
# def show_Product_json(id):
#   job = load_products_from_db(id)
#   return jsonify(job)

# @app.route("/job/<id>/apply", methods=['post'])
# def apply_to_job(id):
#   data = request.form
#   job = load_products_from_db(id)
#   add_application_to_db(id, data)
#   return render_template('application_submitted.html', 
#                          application=data,
#                          job=job)

if __name__ == '__main__':
  app.run (host='0.0.0.0', debug = True)	


