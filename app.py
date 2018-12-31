from flask import Flask, render_template,redirect



app = Flask(__name__)


@app.route("/") # router
def home(): # view function
    c = {
        "name": "Aquaman",
        "company": "DC Comics",
        "image": "https://i.pinimg.com/originals/00/ac/e1/00ace1e2c5b61444976f3c84f2fb00e2.jpg",
        "abilities": ["Speed","Strength","Reflexs","Underwater","Telepathy"],
    }
    
    return render_template("home.html",
                           character = c) # respone




@app.route("/c4e")
def c4e():
    return "Code for everyone 24"

@app.route("/hi/<name>")

def say_hi(name):
    
    return "Hi " + name

@app.route("/add/<int:number1>/<int:number2>")
def add(number1,number2):
    s = number1 + number2
    return   str(s)


if __name__ == "__main__":  #chi co mot con chinh
    app.run(debug=True)


