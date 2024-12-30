from flask import Flask
from flask_cors import CORS

# Create the Flask app
app = Flask(__name__)

# Enable CORS for frontend-backend communication
CORS(app)

# Define a basic route
@app.route('/')
def home():
    return {"message": "Welcome to the Debt Payment Calculator API!"}

# Start the server
if __name__ == "__main__":
    app.run(debug=True)