from flask import Flask, render_template,jsonify

app = Flask (__name__)

PRODUCT = [
  {
    'id': 1,
    'name': 'Pick up Service',
    'description': 'Pick up service for pickup trucks and delivery trucks'	
  },
  {
    'id': 2,
    'name': 'Fertilizers',
    'description': 'Fertilizers for plants'	
  },
  {
    'id': 3,
    'name': 'Earthworms',
    'description': 'Earthworms for soil'
  }
]

@app.route ('/')
def hello_world ():
  return render_template('home.html', products=PRODUCT)
  
@app.route("/api/products")
def list_products():
  return jsonify(PRODUCT)

if __name__ == '__main__':
  app.run (host='0.0.0.0', debug = True)	