from flask import Flask,render_template,redirect



app = Flask(__name__)

@app.route("/")
def home():
    return("HELLO")

@app.route("/about-me/")
def about():
    aboutme = {
        "name": "Tuan",
        "work": "Sinh vien",
        "school": "Bach Khoa",
        "hobbies": "xem phim",

    }
    return render_template("about-me.html",Aboutme = aboutme)
@app.route("/school")
def school():
    return redirect("http://techkids.vn")
if __name__ == "__main__":
    app.run(debug=True)

