#!/usr/bin/python3
"""
Task 02 - Logic:
Read items from items.json and render them using Jinja loops/conditionals.
"""
import json
import os
from flask import Flask, render_template

app = Flask(__name__)


def load_items():
    """Load items list from items.json (returns [] on any issue)."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "items.json")

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        items = data.get("items", [])
        return items if isinstance(items, list) else []
    except (OSError, json.JSONDecodeError, AttributeError):
        return []


@app.route("/items", methods=["GET"])
def items_page():
    items = load_items()
    return render_template("items.html", items=items)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
