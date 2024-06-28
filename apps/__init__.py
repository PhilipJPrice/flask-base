#from flask import Flask

#def create_app(config):
#    app = Flask(__name__)
#    app.config.from_object(config)
#    return app

from flask import Flask

app = Flask(__name__)

from apps import routes
