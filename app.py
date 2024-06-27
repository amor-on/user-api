from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos simulada
database = [
    {"id": 1, "name": "Manuel", "favorite_food": "Chocolate", "neighborhood": "Canido"},
    {"id": 2, "name": "Alejandro", "favorite_food": "Tortilla", "neighborhood": "Magdalena"},
    {"id": 3, "name": "Damián", "favorite_food": "Ensaladilla", "neighborhood": "Catabois"},
    {"id": 4, "name": "Jacobo", "favorite_food": "Pulpo a la gallega", "neighborhood": "Ferrol Vello"},
    {"id": 5, "name": "Antonio", "favorite_food": "Lacón con grelos", "neighborhood": "Esteiro"},
    {"id": 6, "name": "Carlos", "favorite_food": "Mariscada", "neighborhood": "Caranza"},
    {"id": 7, "name": "Diego", "favorite_food": "Callos a la gallega", "neighborhood": "Canido"},
    {"id": 8, "name": "Patricia", "favorite_food": "Pimientos de Padrón", "neighborhood": "Recimil"},
    {"id": 9, "name": "Sara", "favorite_food": "Tarta de Santiago", "neighborhood": "Santa Mariña"},
    {"id": 10, "name": "Aida", "favorite_food": "Caldo gallego", "neighborhood": "San Xoán"},
    {"id": 11, "name": "María", "favorite_food": "Raxo", "neighborhood": "Catabois"},
    {"id": 12, "name": "Marcos", "favorite_food": "Churrasco", "neighborhood": "Serantes"},
    {"id": 13, "name": "Noemi", "favorite_food": "Almejas a la marinera", "neighborhood": "O Bertón"},
    {"id": 14, "name": "Óscar", "favorite_food": "Mejillones al vapor", "neighborhood": "A Graña"},
    {"id": 15, "name": "Antía", "favorite_food": "Filloas", "neighborhood": "Mandiá"},
    {"id": 16, "name": "Fina", "favorite_food": "Sardinas asadas", "neighborhood": "Covas"}
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
