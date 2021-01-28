import collections
import json

from flask import request, Blueprint, current_app, url_for
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

        page = request.args.get('page', 1, type=int)

        if climate:
            rows = rows.filter_by(climate=climate)
        if name:
            rows = rows.filter_by(name=name)
        if sort:
            sort_by = sort.split(' ')[0]
            sort_type = sort.split(' ')[1]
            sort = sort_by + '.' + sort_type + '()'
            rows = rows.order_by(sort)

        pages = rows.paginate(page, current_app.config['ITEMS_PER_PAGE'], False)
        # rows = list(rows)

        next_url = url_for('planets', page=pages.next_num) if pages.has_next else None
        prev_url = url_for('planets', page=pages.prev_num) if pages.has_prev else None

        planets = list()
        for row in rows:
            d = collections.OrderedDict()
            d['next_url'] = next_url
            d['prev_url'] = prev_url
            d['name'] = row[0]
            d['climate'] = row[1]
            d['population'] = row[2]
            planets.append(d)

        planets = json.dumps(planets)

        return planets
