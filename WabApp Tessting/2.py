from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <html>
        <head>
            <title>Mast Webpage</title>
        </head>
        <body style="background-color:#f0f8ff; text-align:center;">
            <h1 style="color:#2e8b57;">Hello, bro! 👋</h1>
            <p>This is my <b>first</b> Mast Webpage app 🚀</p>
            <a href="/about">About Me</a>
        </body>
    </html>
    """
    return render_template_string(html)

@app.route('/about')
def about():
    html = """
    <html>
        <head>
            <title>About - Mast Webpage</title>
        </head>
        <body style="background-color:#fae4e1; text-align:center;">
            <h2>About Me</h2>
            <p>Yeh ek demo Flask app hai, banaya gaya hai <b>masti</b> ke liye! 😎</p>
            <a href="/">Back to Home</a>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)