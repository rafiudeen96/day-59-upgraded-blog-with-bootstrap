from flask import Flask,render_template,request
import requests
import smtplib

app = Flask(__name__)

all_posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()

@app.route("/")
def home():
    return render_template("index.html",all_posts=all_posts)

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # ---------------------------------- SMTP SECTION ------------------------------------------- #
        owners_email = "rafiudeen96@gmail.com"
        owners_password = "lnklflelzzwpajas"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=owners_email,password=owners_password)
            connection.sendmail(from_addr=owners_email,to_addrs=owners_email,
                                msg=f"Subject:{name}\n\nThis message is from: {email}\n{message}\n\n Contact Info:{phone}")

        # --------------------------------- SMTP SECTION ----------------------------------------------#

        return render_template("contact.html",name=name,message_sent=True)

    else:
        return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:id>")
def post(id):
    return render_template("post.html",all_posts=all_posts,id=id)


if __name__ == "__main__":
    app.run(debug=True)