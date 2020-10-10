from flask import Flask, request 
from operations import add, sub, mult, div 

app = Flask(__name__)

@app.route('/add')
def add_func():
  """ Add a and b. """
  #print(request.args)
  a = int(request.args.get('a'))
  b = int(request.args.get('b'))
  result = add(a,b)
  return str(result)

@app.route('/sub')
def sub_func():
  """ Sub b from a. """
  a = int(request.args.get('a'))
  b = int(request.args.get('b'))
  result = sub(b,a)
  return str(result)


@app.route('/mult')
def mult_func():
  """ Multiply a and b."""
  a = int(request.args.get('a'))
  b = int(request.args.get('b'))
  result = mult(a,b)
  return str(result)
  

@app.route('/div')
def div_func():
  """ Divide a by b."""
  a = int(request.args.get('a'))
  b = int(request.args.get('b'))
  result = div(a,b)
  return str(result)


# Part Two
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
