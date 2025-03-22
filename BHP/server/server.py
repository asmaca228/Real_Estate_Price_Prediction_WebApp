from flask import Flask, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

@app.route('/get_location_names', methods=["GET"])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    return response

@app.route('/predict_home_price', methods=["POST"])
def predict_home_price():
    data = request.form

    location = data.get("location")
    bhk = int(data.get("bhk", 0))  # Default value to prevent errors
    bath = int(data.get("bath", 0))
    total_sqft = float(data.get("total_sqft", 0))

    estimated_price = util.get_estimated_price(location, bhk, bath, total_sqft)

    response = jsonify({
        "estimated_price": estimated_price
    })
    return response

if __name__ == "__main__":
    print("Starting Python Flask for house price prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)  # Added debug mode for better error tracking
