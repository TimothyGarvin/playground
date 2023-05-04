from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def base():
    return "main page"

@app.route("/play/<int:num>/<string:color>")
def play(num, color):
    return render_template("index.html", num=num, color=color)

if __name__ == "__main__":
    app.run(debug=True)