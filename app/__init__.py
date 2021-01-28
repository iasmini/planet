from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_restful import Api

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

# ATENCAO: tem que ser importado nessa ordem senao exibe o erro abaixo:
# ImportError: cannot import name 'db' from partially initialized module 'app'
# (most likely due to a circular import) (/opt/portfolio/planet/app/__init__.py)
from app.planet.controllers import planet_bp
from api.controllers import ApiResource

app.register_blueprint(planet_bp)

app.add_url_rule('/', endpoint='index')
app.add_url_rule('/init-db/', endpoint='init-db')
app.add_url_rule('/planets/', endpoint='planets')

api = Api(app)
api.add_resource(ApiResource, '/api/planets/', endpoint='planets')
