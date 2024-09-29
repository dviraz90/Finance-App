from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Configuration settings
SERVICE_URLS = {
    'auth': 'http://auth-service:5001',
    'budget': 'http://budget-service:5002',
    'transaction': 'http://transaction-service:5003',
    'user': 'http://user-service:5004',
    'savings': 'http://savings-service:5005',
    'investment': 'http://investment-service:5006',
    'notification': 'http://notification-service:5007',
    'analytics': 'http://analytics-service:5008'
}


@app.route('/user/register', methods=['POST'])
def register_user():
    response = requests.post(f"{SERVICE_URLS['auth']}/auth/register", json=request.json)
    return jsonify(response.json()), response.status_code


@app.route('/budget/set', methods=['POST'])
def set_budget():
    response = requests.post(f"{SERVICE_URLS['budget']}/budget/set", json=request.json)
    return jsonify(response.json()), response.status_code


@app.route('/transaction/log', methods=['POST'])
def log_transaction():
    response = requests.post(f"{SERVICE_URLS['transaction']}/transaction/log", json=request.json)
    return jsonify(response.json()), response.status_code




if __name__ == '__main__':
    app.run(host='localhost', port=5000)
