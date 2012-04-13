from flask import Flask, render_template, request, url_for
from werkzeug import SharedDataMiddleware
import os

app = Flask(__name__)

app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
	'/': os.path.join(os.path.dirname(__file__), 'static')
})


@app.route("/", methods=['POST','GET'])
def index():
	if request.method == 'POST':
		return render_template('index.html', data=request.form)
	else:
		return render_template('index.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
