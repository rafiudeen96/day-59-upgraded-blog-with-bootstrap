import requests
from flask import Flask,render_template
import requests

app= Flask(__name__)

all_posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()

@app.route("/")
def home():
    return render_template("index.html",all_posts=all_posts)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:id>")
def post(id):
    return render_template("post.html",all_posts=all_posts,id=id)


if __name__ == "__main__":
    app.run(debug=True)