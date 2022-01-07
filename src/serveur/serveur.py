from flask import Flask
from flask_cors import CORS
from flask import jsonify
from flask import request

ProductDB = [
    {
        'id': '0',
        'name': 'ordinateur',
        'price': '1000'
    },
    {
        'id': '1',
        'name': 'table',
        'price': '20'
    },
    {
        'id': '2',
        'name': 'chaise',
        'price': '10'
    },
    {
        'id': '3',
        'name': 'ventilateur',
        'price': '15'
    }
]

app = Flask(__name__)
CORS(app)


@app.route("/test", methods=["GET"])  # @aap.route("/route", methods=["POST"])
def home():
    print("ui serveur")
    return "hello_world"


@app.route("/product/getProducts", methods=["GET"])
def getAllProducts():
    return jsonify({"products ": ProductDB})


@app.route("/product/details/<name>", methods=["GET"])
def getProductDetails(name):
    product = [prod for prod in ProductDB if (prod['name'] == name)]
    return jsonify({"product ": product})


@app.route("/product/add", methods=["POST"])
def addProduct():
    ProductDB.append(request.json)
    return jsonify({"products ": ProductDB})


@app.route("/product/delete/<name>", methods=["DELETE"])
def deleteProduct(name):
    product = [prod for prod in ProductDB if (prod['name'] == name)]
    if (len(product) > 0):
        ProductDB.remove(product[0])
    return jsonify({"products ": ProductDB})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # host="0.0.0.0", port=80)
