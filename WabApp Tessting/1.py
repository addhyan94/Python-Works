from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, bro! This is my first Webpage app .'

if __name__ == '__main__':
    app.run(debug=True)