from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    connection = mysql.connector.connect(
        host='195.179.238.58',  # Cambia esto por tu host
        user='u927419088_admin',  # Cambia esto por tu usuario
        password='#Admin12345#',  # Cambia esto por tu contraseña
        database='u927419088_testing_sql'  # Cambia esto por el nombre de tu base de datos
    )
    return connection


@app.route('/cursos', methods=['GET'])
def get_cursos():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM Curso"
    cursor.execute(query)
    cursos = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(cursos)


if __name__ == '__main__':
    app.run(debug=True)
