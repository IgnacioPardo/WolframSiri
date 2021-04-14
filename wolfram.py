import wolframalpha
import os

app_id = os.getenv("app_id")

def wolfram(msg):
	client = wolframalpha.Client(app_id)
	res = client.query(msg)
	print(res)
	return next(res.results).text
