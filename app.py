from flask import Flask, render_template # type: ignore

app = Flask(__name__, static_folder='static')


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("aboutus.html")

@app.route("/sigin")
def sigin():
    return render_template("sigin.html")

if __name__== "__main__":
    app.run(debug=True)



    