from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

@app.route('/convert/<celsius>')
def convert_temperature(celsius):
    fahrenheit = celsius_to_fahrenheit(float(celsius))
    return f"{celsius}°C is {fahrenheit:.1f}°F"
