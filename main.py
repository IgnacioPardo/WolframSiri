from flask import Flask, request
from gevent.pywsgi import WSGIServer
from threading import Thread
import codecs

from wolfram import *


def run():
	#Flask built in deploy for development (lazy loading)
	#app.run(host='0.0.0.0', port=8081)

	#WSGIServer deploy for production.
	WSGIServer(('', 8081), app).serve_forever()


def keep_alive():
	t = Thread(target=run)
	t.start()


app = Flask(__name__)


@app.route('/')
def main():
	return codecs.open("index.html", "r", "utf-8").read()


@app.route('/siri', methods=['GET'])
def siri():
	msg = request.args.get('msg')
	if '\n' in msg:
		msg = msg.replace('\n', '')

	try:
		return str(wolfram(msg))
	except Exception as e:
		print(e)
		return "error 500"


if __name__ == '__main__':
	keep_alive()
