import requests
from flask import Flask, render_template, request
# from bs4 import BeautifulSoup

# os.system("clear")

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
# allNews = {}
# order_by = "popular"

def getNews(url):
  data = requests.get(url).json() #, params={data: value}, timeout=5)
  print(data['hits'])
  # print(data["hits"].text)
  return data['hits']

@app.route("/")
def home():
  choice = request.args.get('order_by')
  if choice not in db:
    if choice == "new":
      allNews = getNews(new)
    elif choice == "popular":
      allNews = getNews(popular)
    db[choice] = allNews
  allNews = db[choice]
  return render_template("index.html", order_by = choice, allNews = allNews)
  # if choice == "new":
  #   return render_template("index.html", order_by = "new", allNews = getNews(new))
  # else: # order_by == "popular":
  #   return render_template("index.html", order_by = "popular", allNews = getNews(popular))

@app.route("/<id>")
def detail(id):
  detailData = requests.get(make_detail_url(id))
  news = detailData.json()
  return render_template("detail.html", news=news)

app.run(host="0.0.0.0")