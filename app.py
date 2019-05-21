from flask import Flask, redirect
from flask import Response, request
import rq_dashboard
from decouple import config

def check_auth(username, password):
    """This function is called to check if a username password combination is valid."""
    return username == app.config.get("RQ_DASHBOARD_USERNAME") and \
           password == app.config.get("RQ_DASHBOARD_PASSWORD")

def authenticate():
    """Sends a 401 response that enables basic auth."""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

def basic_auth():
    """Ensure basic authorization."""
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()



app = Flask(__name__)
app.config.from_object(rq_dashboard.default_settings)
app.config['REDIS_URL'] = config('REDIS_URL', 'localhost')
app.config['RQ_DASHBOARD_USERNAME'] = config('RQ_DASHBOARD_USERNAME', '')
app.config['RQ_DASHBOARD_PASSWORD'] = config('RQ_DASHBOARD_PASSWORD', '')

#rq_dashboard.blueprint.before_request(basic_auth)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")


@app.route('/')
def hello_world():
    return redirect("/rq")


if __name__ == '__main__':
    app.run()
