import requests
from flask import Flask, render_template, request
# from bs4 import BeautifulSoup

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")

iban=request.get(new)
print(iban)

@app.route("/")
def hoem():
  choice = request.args.get('order_by')
  return render_template("index.html", order_by=choice)

@app.route("/<username>")
def detail(username):
  return f"Hello {username} how are you?"

app.run(host="0.0.0.0")