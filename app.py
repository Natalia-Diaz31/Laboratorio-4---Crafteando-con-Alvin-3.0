from flask import Flask, jsonify

app = Flask(__name__)

productos = [
    {
        "codigo": 201,
        "nombre": "Teclado mecánico RGB",
        "precio": 45.00,
        "stock": 12
    },
    {
        "codigo": 202,
        "nombre": "Mouse inalámbrico",
        "precio": 18.50,
        "stock": 25
    },
    {
        "codigo": 203,
        "nombre": "Monitor LED 24\"",
        "precio": 165.00,
        "stock": 8
    }
]

siguiente_codigo = 204

@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "mensaje": "API base de TecnoMarket funcionando correctamente"
    }), 200

@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify(productos), 200


@app.route("/productos/<int:codigo>", methods=["GET"])
def obtener_producto(codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return jsonify(producto), 200

    return jsonify({
        "error": "Producto no encontrado",
        "mensaje": f"No existe un producto con el código {codigo}"
    }), 404
@app.route("/productos", methods=["POST"])
def registrar_producto():
    global siguiente_codigo

    datos = request.get_json(silent=True)

    if datos is None:
        return jsonify({
            "error": "Solicitud inválida",
            "mensaje": "Debes enviar la información en formato JSON"
        }), 400

    if "nombre" not in datos or "precio" not in datos or "stock" not in datos:
        return jsonify({
            "error": "Datos incompletos",
            "mensaje": "Debes enviar nombre, precio y stock"
        }), 400

    nombre = datos["nombre"]

    if nombre == "":
        return jsonify({
            "error": "Nombre inválido",
            "mensaje": "El nombre del producto no puede estar vacío"
        }), 400

    try:
        precio = float(datos["precio"])
        stock = int(datos["stock"])
    except ValueError:
        return jsonify({
            "error": "Tipo de dato inválido",
            "mensaje": "El precio debe ser numérico y el stock debe ser entero"
        }), 400

    if precio < 0:
        return jsonify({
            "error": "Precio inválido",
            "mensaje": "El precio no puede ser negativo"
        }), 400

    if stock < 0:
        return jsonify({
            "error": "Stock inválido",
            "mensaje": "El stock no puede ser negativo"
        }), 400

    nuevo_producto = {
        "codigo": siguiente_codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    productos.append(nuevo_producto)
    siguiente_codigo += 1

    return jsonify(nuevo_producto), 201
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)
