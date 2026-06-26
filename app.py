from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "mensaje": "API base de TecnoMarket funcionando correctamente"
    }), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)