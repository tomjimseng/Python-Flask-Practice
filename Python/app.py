from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        "name": "My Wonderful Store",
        "items": [
            {
            "name": "My Item",
            "price" : 15.99
            }
        ]

    }
]

#POST  - used to recieve data
#GET - used to send data back only

#POST /store data: {name:}
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        return jsonify({"message": "store not found"})

#GET /store
@app.route("/store")
def get_all_stores():
    return jsonify({"stores": stores})

#POST /store/<string:name>/item{name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def get_item_name(name):
    request.data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request.data['name'],
                'price': request.data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
        return jsonify({"message": "store not found"})

#GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jasonify(store['item'])
        return jsonify({"message": "store not found"})

app.run(port=5000)