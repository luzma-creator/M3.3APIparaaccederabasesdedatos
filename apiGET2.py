from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos MySQL
def get_db_connection():
    conn = mysql.connector.connect(
        host='195.179.238.58',
        user='u927419088_admin',
        password='#Admin12345#',
        database='u927419088_testing_sql'
    )
    return conn

@app.route('/actualizar', methods=['GET'])
def actualizar_registro():
    try:
        # Parámetros esperados: id, columna, valor
        id_registro = request.args.get('id')
        columna = request.args.get('columna')
        nuevo_valor = request.args.get('valor')

        if not id_registro or not columna or not nuevo_valor:
            return jsonify({"error": "Faltan parámetros"}), 400

        # Conectar a la base de datos
        conn = get_db_connection()
        cursor = conn.cursor()

        # Construir la consulta SQL
        consulta_sql = f"UPDATE datos_usuario SET {columna} = %s WHERE id = %s"
        valores = (nuevo_valor, id_registro)

        # Ejecutar la consulta
        cursor.execute(consulta_sql, valores)
        conn.commit()

        # Verificar si se actualizó alguna fila
        if cursor.rowcount == 0:
            return jsonify({"error": "No se encontró el registro con el id especificado"}), 404

        # Cerrar la conexión
        cursor.close()
        conn.close()

        return jsonify({"mensaje": "Registro actualizado exitosamente"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)