import collections
import json

from flask import request, Blueprint
from flask_restful import Resource

from app.planet.models import Planet

bp = Blueprint('api', __name__)


class ApiResource(Resource):
    @bp.route('/api/planets/')
    def get(self):
        """ Returns a list of planets """

        rows = Planet.query.with_entities(Planet.name, Planet.climate, Planet.population)

        # filters
        climate = request.args.get('climate', None)
        name = request.args.get('name', None)

        sort = request.args.get('sort', None)

        planets = list()
        if climate:
            planets = rows.filter_by(climate=climate)
        if name:
            planets = rows.filter_by(name=name)
        if sort:
            sort_by = sort.split(' ')[0]
            sort_type = sort.split(' ')[1]
            sort = sort_by + '.' + sort_type + '()'
            planets = rows.order_by(sort)

        objects_list = []
        for planet in planets:
            d = collections.OrderedDict()
            d['name'] = planet[0]
            d['climate'] = planet[1]
            d['population'] = planet[2]
            objects_list.append(d)

        planets = json.dumps(objects_list)

        return {
            'planets': planets
        }
