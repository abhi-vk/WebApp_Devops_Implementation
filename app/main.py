from pathlib import Path

from flask import Flask, jsonify, send_from_directory

STATIC_DIR = Path(__file__).resolve().parent / "static"

app = Flask(
    __name__,
    static_folder=str(STATIC_DIR),
    static_url_path="/static",
)

ITEMS = {
    1: {"id": 1, "name": "sample-item", "description": "A sample catalog item."},
    2: {"id": 2, "name": "devops", "description": "Ready for the DevOps journey."},
}


@app.get("/")
def read_root():
    return send_from_directory(STATIC_DIR, "index.html")


@app.get("/health")
def health_check():
    return jsonify({"status": "ok"})


@app.get("/api/v1/items")
def list_items():
    return jsonify(list(ITEMS.values()))


@app.get("/api/v1/items/<int:item_id>")
def get_item(item_id):
    item = ITEMS.get(item_id)
    if item is None:
        return jsonify({"detail": "Item not found"}), 404
    return jsonify(item)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
