#!/usr/bin/python3
"""
Task 03 - Files:
Read products from JSON or CSV based on query param `source`
and optionally filter by `id`, then render in a shared template.
"""
import csv
import json
import os
from flask import Flask, render_template, request

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "products.json")
CSV_PATH = os.path.join(BASE_DIR, "products.csv")


def read_products_json(path=JSON_PATH):
    """Return list of product dicts from a JSON file. [] on error."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        return []


def read_products_csv(path=CSV_PATH):
    """Return list of product dicts from a CSV file. [] on error."""
    products = []
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Normalize fields
                products.append(
                    {
                        "id": int(row.get("id")) if row.get("id") else None,
                        "name": row.get("name", ""),
                        "category": row.get("category", ""),
                        "price": float(row.get("price")) if row.get("price") else None,
                    }
                )
        return products
    except (OSError, ValueError, TypeError):
        return []


@app.route("/products", methods=["GET"])
def products():
    source = request.args.get("source", "")
    id_param = request.args.get("id", None)

    error = None
    products_list = []

    if source == "json":
        products_list = read_products_json()
    elif source == "csv":
        products_list = read_products_csv()
    else:
        error = "Wrong source"

    # Filter by id if provided and source was valid
    if error is None and id_param is not None:
        try:
            wanted_id = int(id_param)
            filtered = [p for p in products_list if p.get("id") == wanted_id]
            if not filtered:
                error = "Product not found"
                products_list = []
            else:
                products_list = filtered
        except ValueError:
            # id not an int => treat as not found
            error = "Product not found"
            products_list = []

    return render_template("product_display.html", products=products_list, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
