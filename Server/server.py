from flask import Flask, request, jsonify, make_response
import util # util includes locations
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify ({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price', methods=['POST']) # here we use POST method
def predict_home_price():
    print(request.headers)
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    size_num = int(request.form['size_num'])
    bath = int(request.form['bath'])

    print("{0}, {1}, {2}, {3}".format(location, total_sqft, size_num, bath))
    print(util.get_estimated_price(location, total_sqft, size_num, bath))
    response = jsonify({
            'estimated_price': util.get_estimated_price(location,total_sqft,size_num,bath)
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()