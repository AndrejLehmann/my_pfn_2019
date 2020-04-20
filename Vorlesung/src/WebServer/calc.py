from flask import Flask

app = Flask(__name__)

@app.route('/<expression>')
def calc(expression):
  result = eval(expression)
  return '{}={}'.format(expression, result)
