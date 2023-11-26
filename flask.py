from flask import Flask, render_template

app = Flask(__name__)

# Temperature conversion function
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Hello World route
@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

# Greet route with optional name parameter
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"<h1>Hello {name}</h1>"

# Celsius to Fahrenheit conversion route
@app.route('/convert/<celsius_str>')
def convert_celsius_to_fahrenheit(celsius_str):
    try:
        celsius = float(celsius_str)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return render_template('conversion_result.html', celsius=celsius, fahrenheit=fahrenheit)
    except ValueError:
        return "Invalid input. Please enter a valid numeric value for Celsius."

if __name__ == '__main__':
    app.run()
