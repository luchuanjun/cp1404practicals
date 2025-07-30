from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}" if name else "Hello"

@app.route('/convert/<celsius>')
def convert(celsius):
    fahrenheit = float(celsius) * 9 / 5 + 32
    return f"{celsius}°C is {fahrenheit:.2f}°F"

if __name__ == '__main__':
    app.run(debug=True)