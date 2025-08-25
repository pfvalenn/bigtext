from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_text():
    text = "escribí acá"
    return render_template('index.html', text = text)


if __name__ == '__main__':
    app.run(debug=True)

