from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scraper

app=Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

@app.route("/")
def index():
    data = mongo.db.mars_data.find_one()
    return render_template("index.html", data=data)

@app.route('/scrape')
def scrape():
    data=mongo.db.mars_data
    scraped_data=mars_scraper.scraper()
    data.update({},scraped_data,upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)