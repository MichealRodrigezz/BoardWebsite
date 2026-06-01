from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/timetable")
def timetable():
    return render_template("timetable.html")

@app.route("/subjects")
def subjects():
    return render_template("subjects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/topper")
def topper():
    return render_template("topper.html")

@app.route("/motivation")
def motivation():
    return render_template("motivation.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]

        return f"Registration Successful! Welcome {name}"

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
