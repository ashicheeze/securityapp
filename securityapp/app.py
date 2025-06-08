import json
from datetime import datetime
from pathlib import Path
from typing import Dict

from flask import Flask, jsonify, request

from .qr_utils import generate_qr

app = Flask(__name__)
DATA_FILE = Path("purchases.json")


def load_purchases() -> Dict:
    if DATA_FILE.exists():
        with DATA_FILE.open() as f:
            return json.load(f)
    return {}


def save_purchases(data: Dict) -> None:
    with DATA_FILE.open("w") as f:
        json.dump(data, f, indent=2)


@app.route("/qr/<user_id>")
def qr(user_id):
    """Return base64 QR code for a user."""
    try:
        code = generate_qr(user_id)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 500
    return jsonify({"user_id": user_id, "qr": code})


@app.route("/purchase", methods=["POST"])
def purchase():
    """Record a purchase given user_id and item."""
    payload = request.get_json(force=True)
    user_id = payload.get("user_id")
    item = payload.get("item")
    if not user_id or not item:
        return jsonify({"error": "user_id and item are required"}), 400

    data = load_purchases()
    data.setdefault(user_id, []).append({
        "item": item,
        "ts": datetime.utcnow().isoformat() + "Z"
    })
    save_purchases(data)
    return jsonify({"status": "recorded"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
