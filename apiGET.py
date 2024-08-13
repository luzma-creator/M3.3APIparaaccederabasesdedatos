from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# Configuración de la base de datos
def get_db_connection():
    return pymysql.connect(
        host='195.179.238.58',           # Cambia esto por tu host
        user='u927419088_admin',        # Cambia esto por tu usuario
        password='#Admin12345#', # Cambia esto por tu contraseña
        database='u927419088_testing_sql', # Cambia esto por el nombre de tu base de datos
        cursorclass=pymysql.cursors.DictCursor  # Para obtener los resultados como diccionarios
    )

# Ruta para la página principal
@app.route('/', methods=['GET'])
def home():
    return "Bienvenido a la API de Cursos. Ve a /api/cursos para ver los cursos disponibles."

# Ruta para obtener los registros de la tabla "Curso"
@app.route('/api/cursos', methods=['GET'])
def get_cursos():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM curso"
            cursor.execute(sql)
            cursos = cursor.fetchall()
        return jsonify(cursos)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        connection.close()

@app.route('/api/cursos/<int:curso_id>', methods=['GET'])
def get_curso(curso_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM curso WHERE idCurso = %s"
            cursor.execute(sql, (curso_id,))
            cursos = cursor.fetchone()
        return jsonify(cursos)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        connection.close()







# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)