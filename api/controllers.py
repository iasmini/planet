from flask import request, Blueprint
from flask_restful import Resource
from sqlalchemy.sql import text

from app.planet.models import Planet

bp = Blueprint('api', __name__)


class ApiResource(Resource):
    @bp.route('/api/planets/')
    def get(self):
        """ Returns a list of planets """
        rows = Planet.query.order_by(Planet.name).all()

        # filters
        climate = request.args.get('climate', None)
        name = request.args.get('name', None)

        sort = request.args.get('sort', None)

        filters = None
        if climate:
            filters = "climate='" + climate + "'"
        if name:
            if filters:
                filters += " AND "
            filters += "name='" + name + "'"
        if filters:
            rows = Planet.query.filter(text(filters))

        if sort:
            rows = rows.order_by(text(sort))

        planets = list()
        for row in rows:
            planets.append(row.to_dict())

        return planets
