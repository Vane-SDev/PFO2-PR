from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
DB_FILE = 'tareas.db'

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                contrasena TEXT NOT NULL
            )
        ''')
        conn.commit()

init_db()

@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    
    if not datos or 'usuario' not in datos or 'contraseña' not in datos:
        return jsonify({"error": "Faltan datos requeridos"}), 400
        
    usuario = datos['usuario']
    contrasena_plana = datos['contraseña']
    contrasena_hash = generate_password_hash(contrasena_plana)
    
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)', (usuario, contrasena_hash))
            conn.commit()
        return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "El usuario ya existe"}), 409

@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    
    if not datos or 'usuario' not in datos or 'contraseña' not in datos:
        return jsonify({"error": "Faltan datos requeridos"}), 400
        
    usuario = datos['usuario']
    contrasena_plana = datos['contraseña']
    
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT contrasena FROM usuarios WHERE usuario = ?', (usuario,))
        resultado = cursor.fetchone()
        
    if resultado and check_password_hash(resultado[0], contrasena_plana):
        return jsonify({"mensaje": "Login exitoso"}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

@app.route('/tareas', methods=['GET'])
def tareas():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Gestión de Tareas</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <h1>Bienvenido al Sistema de Gestión de Tareas</h1>
        <p>Has accedido correctamente al sistema.</p>
    </body>
    </html>
    """
    return html_content, 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)