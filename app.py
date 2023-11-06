from flask import Flask, render_template,jsonify
from database import load_product_from_db

app = Flask (__name__)

@app.route ('/')
def hello_world ():
  productss = load_product_from_db()
  return render_template('home.html', products=productss)
  
@app.route("/api/products")
def list_products():
  productss = load_product_from_db()
  return jsonify(productss)

if __name__ == '__main__':
  app.run (host='0.0.0.0', debug = True)	