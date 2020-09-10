# room.py
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/room')
def blog():
    return "My Home Page With a Room"


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8081)
