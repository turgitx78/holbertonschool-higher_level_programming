#!/usr/bin/python3
"""
Task 04 - DB:
Display products from JSON, CSV, or SQLite (products.db) based on query param `source`
and optionally filter by `id`. Uses the same product_display.html template.
"""
import csv
import json
import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "products.json")
CSV_PATH = os.path.join(BASE_DIR, "products.csv")
DB_PATH = os.path.join(BASE_DIR, "products.db")


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


def read_products_sql(path=DB_PATH):
    """Return list of product dicts from SQLite database. [] on DB error."""
    products = []
    try:
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        cur.execute("SELECT id, name, category, price FROM Products")
        for pid, name, category, price in cur.fetchall():
            products.append(
                {"id": pid, "name": name, "category": category, "price": price}
            )
        conn.close()
        return products
    except sqlite3.Error:
        return []


@app.route("/products", methods=["GET"])
def products():
    source = request.args.get("source", "")
    id_param = request.args.get("id")

    error = None
    products_list = []

    if source == "json":
        products_list = read_products_json()
    elif source == "csv":
        products_list = read_products_csv()
    elif source == "sql":
        products_list = read_products_sql()
        # If DB returns nothing, it could be empty DB or error.
        # Task says "handle DB-related errors"; we surface a generic message only
        # when DB file exists but fetch returns empty and id isn't specifically requested.
        if not products_list and not os.path.exists(DB_PATH):
            error = "Database error"
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
            error = "Product not found"
            products_list = []

    return render_template("product_display.html", products=products_list, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
