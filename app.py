from flask import Flask
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


app = Flask(__name__)

@app.route('/')
def hello():
    #logging.info('Request made to the root endpoint.')
    print('Request made to the root endpoint.')
    return 'Hello World!! \n Available paths: /warn | /err | /count'

@app.route('/warn')
def line1():
    #logging.warning('Here is a test warning')
    print('Here is a test warning')
    return 'Warning written to logs..'

@app.route('/err')
def line2():
    #logging.error('Oh no you have an error sadge :(')
    print('Oh no you have an error sadge :(')
    return 'Error written to logs..'

@app.route('/count')
def line3():
    for i in range(10):
        logging.info('INFO: %s', i)
    return 'Info written to logs..'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
