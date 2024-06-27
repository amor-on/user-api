from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos simulada
database = [
    {"id": 1, "name": "Manuel", "favorite_food": "Chocolate", "neighborhood": "Canido"},
    {"id": 2, "name": "Alejandro", "favorite_food": "Tortilla", "neighborhood": "Magdalena"},
    {"id": 3, "name": "Damián", "favorite_food": "Ensaladilla", "neighborhood": "Catabois"}
]

@app.route('/')
def home():
    return "Bienvenido a la API de Usuarios!"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(database)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in database if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    new_user["id"] = len(database) + 1
    database.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
