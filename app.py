from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("cool.html")

if __name__ == '__main__':
    app.run(debug=True)

