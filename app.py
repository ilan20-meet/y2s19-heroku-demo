from flask import Flask, render_tempate, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_tempate("cool.html")

if __name__ == '__main__':
    app.run(debug=True)

