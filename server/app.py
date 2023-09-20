#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    display = ""
    for line in range(0, parameter):
        display += f'{line}\n'

    return display

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    
    if operation == "div":
        a = num1/num2
    elif operation == "-":
        a = num1-num2
    elif operation == "+":
        a = num1 + num2
    elif operation == "*":
        a = num1 *num2
    elif operation == "%":
        a = num1 % num2
    return f'{a}'