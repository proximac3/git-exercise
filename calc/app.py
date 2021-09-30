# Put your app in here.
from flask import Flask, request
app = Flask(__name__)



def add(a, b):
    """Add a and b."""
    return a + b

def sub(a, b):
    """Substract b from a."""
    return a - b

def mult(a, b):
    """Multiply a and b."""
    return a * b

def div(a, b):
    """Divide a by b."""
    return a / b

# diction holding keys to access and call functions
operands = {
    'add' :add,
    'sub': sub,
    'mult': mult,
    'div': div
}

# calcultor form
@app.route('/calculate')
def calculator():
    return"""
    <h1> Simple calculator </h1>
    <form method='Post'>
        <input type='text' placeHolder='Enter Number' name='number1'> </input> 
        <select name='operator'>
            <option Value='add'> + </option> 
            <option Value='sub'> - </option> 
            <option Value='mult'> * </option> 
            <option Value='div'> / </option> 
        </select>
        <input type='text' placeHolder='Enter Number' name ='number2'> </input>
        <button> Submit </button>
    </form>
    """


@app.route('/calculate', methods=['POST'])
def addition():
    number_one = request.form['number1']
    number_two = request.form['number2']
    perform = request.form['operator']

    result = operands[f'{perform}'](int(number_one), int(number_two))

    return f"<h1> The result of your operation is: {result}</h1>"