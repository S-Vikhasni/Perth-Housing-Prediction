from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_suburb_names')
def get_suburb_names ():
   response = jsonify({
      'suburbs' : util.get_suburb_names ()
   })
   response.headers.add('Access-Control-Allow-Origin', '*')
   return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
 suburb = request.form['suburb']
 bedrooms = int (request.form['bedrooms'])
 bathrooms =  int (request.form['bathrooms'])
 garage = float (request.form['garage'])
 land_area = int (request.form['land_area'])
 floor_area = int (request.form['floor_area'])
 
 response = jsonify({
'estimated_price': util.get_estimated_price(suburb, bedrooms, bathrooms, garage, land_area, floor_area)
})

 response.headers.add('Access-Control-Allow-Origin', '*')
 return response

if __name__ == "__main__":
  print ("Starting Python Flask Server...")
  util.load_saved_artifacts()
  app.run()