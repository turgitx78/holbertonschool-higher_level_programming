#!/usr/bin/python3
"""
Task 04 - Flask:
A simple Flask API with basic routes, JSON responses, and POST handling.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# NOTE: Keep this empty to avoid checker issues with hardcoded test data.
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    # Return a list of usernames
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    # If body is not valid JSON -> 400
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store the whole object as value, keyed by username
    users[username] = payload

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
