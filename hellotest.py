from flask import Flask, render_template
app = Flask(__name__)



@app.route("/John")
def John():
    return "Hello Pachara Sukthai."


if __name__ == '__main__':
    #app.dbbug = True
    app.run(host='0.0.0.0', port=80)