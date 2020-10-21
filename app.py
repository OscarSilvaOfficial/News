from flask import *
from backend.api import *

app = Flask(__name__)

@app.route('/')
def index():
    resp = getApiResponse()
    return render_template('index.html', response=resp)

app.run(debug=True)