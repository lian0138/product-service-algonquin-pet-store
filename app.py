from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

app = Flask(__name__)

# Enable CORS to allow requests from any origin
CORS(app)

# Fetch the port from the environment or default to 3030
PORT = int(os.getenv("PORT", 3030))

# Define a route for "/products"
@app.route('/products', methods=['GET'])
def get_products():
    # Return a JSON response with a list of products
    return jsonify([
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ])

if __name__ == '__main__':
    # Start the Flask web server
    app.run(host='0.0.0.0', port=PORT)