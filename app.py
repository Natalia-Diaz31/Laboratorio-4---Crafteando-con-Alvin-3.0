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

if __name__ == "__main__":
    app.run(debug=True, port=5000)
