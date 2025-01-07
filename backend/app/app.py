from flask import Flask, request, jsonify
from debt_calculator import lp_debt_solver

app = Flask(__name__)

@app.route('/optimize-payments', methods=['POST'])
def optimize_payments():
    data = request.json
    
    # Input validation
    if 'balances' not in data or 'budget' not in data:
        return {"error": "Missing required fields"}, 400
    
    if not isinstance(data['budget'], (int, float)):
        return {"error": "Budget must be a number"}, 400
    
    # Solve LP problem
    result = lp_debt_solver(data)
    return jsonify({"optimized_payments": result})

