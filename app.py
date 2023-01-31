from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/')
def hello():
    logging.info('Request made to the root endpoint.')
    return 'Hello World!'

@app.route('/warn')
def line1():
    logging.info('WARN: here is a test warning')
    return 'Warning written to logs..'

@app.route('/err')
def line2():
    logging.info('ERR: Oh no you have an error sadge :(')
    return 'Error written to logs..'

@app.route('/log')
def line3():
    logging.info('Good log')
    return 'Default written to logs..'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
