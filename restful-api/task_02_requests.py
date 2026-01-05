#!/usr/bin/python3
"""
Task 02 - Requests:
Fetch posts from JSONPlaceholder and either print titles or save to CSV.
"""
import csv
import requests


API_URL = "https://jsonplaceholder.typicode.com/posts"
CSV_FILENAME = "posts.csv"


def fetch_and_print_posts():
    """
    Fetch all posts and print the response status code and all post titles.
    """
    response = requests.get(API_URL, timeout=10)
    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        return

    posts = response.json()
    for post in posts:
        title = post.get("title", "")
        print(title)


def fetch_and_save_posts():
    """
    Fetch all posts and save id, title, body to a CSV file named posts.csv.
    """
    response = requests.get(API_URL, timeout=10)

    if response.status_code != 200:
        return

    posts = response.json()

    rows = [
        {
            "id": post.get("id"),
            "title": post.get("title", ""),
            "body": post.get("body", ""),
        }
        for post in posts
    ]

    fieldnames = ["id", "title", "body"]
    with open(CSV_FILENAME, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
