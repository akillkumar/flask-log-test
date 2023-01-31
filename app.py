from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print('Request made to the root endpoint.')
    return 'Hello World!'

@app.route('/warn')
def line1():
    print('WARN: here is a test warning')
    return 'Warning written to logs..'

@app.route('/err')
def line2():
    print('ERR: Oh no you have an error sadge :(')
    return 'Error written to logs..'

@app.route('/info')
def line3():
    print('INFO: Good log')
    return 'Default written to logs..'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
