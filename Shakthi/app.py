from flask import Flask, request, jsonify

app = Flask(__name__)

# Normal route
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# Route with dynamic variables in URL
@app.route('/<a>/<b>')
def dynamic_route(a, b):
    return f"Values received: a={a}, b={b}"

# Route that accepts JSON data
@app.route('/json', methods=['POST'])
def json_route():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data received"}), 400
    return jsonify({"received": data})

# Route with query parameters (args data)
@app.route('/args')
def args_route():
    param1 = request.args.get('param1', 'default1')
    param2 = request.args.get('param2', 'default2')
    print(param1,param2)
    return jsonify({"param1": param1, "param2": param2})

if __name__ == '__main__':
    app.run(debug=True)
