# importing the libraries
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def default_home():
    return render_template('Page1.html')

@app.route('/water')
def default_homewater():
    return render_template('Page2.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)