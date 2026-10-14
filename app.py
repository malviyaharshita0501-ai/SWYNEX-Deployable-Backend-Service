from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
items = [
    {"id": 1, "name": "Laptop", "description": "Sample electronic item"},
    {"id": 2, "name": "Keyboard", "description": "Sample computer accessory"},
    {"id": 3, "name": "Mouse", "description": "Wireless computer mouse"},
    {"id": 4, "name": "Monitor", "description": "Full HD computer monitor"},
    {"id": 5, "name": "Headphones", "description": "Audio headphones"},
]

# Home endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to SWYNEX Deployable Backend Service",
        "status": "running"
    }), 200

# Health check endpoint
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

# Get all items
@app.route("/api/items", methods=["GET"])
def get_items():
    return jsonify({
        "count": len(items),
        "items": items,
    }), 200

# Get a single item by ID
@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)

    if item is None:
     
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item), 200

# Create a new item
@app.route("/api/items", methods=["POST"])
def create_item():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be valid JSON"}), 400

    name = data.get("name")
    description = data.get("description", "")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Name is required"}), 400

    if not isinstance(description, str):
        return jsonify({"error": "Description must be a string"}), 400

    new_id = max((item["id"] for item in items), default=0) + 1

    new_item = {
        "id": new_id,
        "name": name.strip(),
        "description": description.strip(),
    }

    items.append(new_item)

    return jsonify(new_item), 201

# Update an existing item
@app.route("/api/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be valid JSON"}), 400

    item = next((i for i in items if i["id"] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    name = data.get("name", item["name"])
    description = data.get("description", item["description"])

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Name must be a non-empty string"}), 400

    if not isinstance(description, str):
        return jsonify({"error": "Description must be a string"}), 400

    item["name"] = name.strip()
    item["description"] = description.strip()

    return jsonify(item), 200

# Delete an item
@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    items.remove(item)

    return jsonify({
        "message": "Item deleted successfully",
        "id": item_id,
    }), 200

# Run the application
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

