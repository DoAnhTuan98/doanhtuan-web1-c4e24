from flask import Flask,render_template
app = Flask(__name__)
@app.route("/bmi/<int:w>/<int:h>")
def BMI(w,h):
    bmi = w/(h/100*h/100)
    return render_template("BMI.html",bmi= bmi)

if __name__ == "__main__":
    app.run(debug=True)