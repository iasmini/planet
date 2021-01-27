import collections
import json

from flask import request, Blueprint
from flask_restful import Resource

from db.db import get_db_cursor

bp = Blueprint('api', __name__)


class Planet(Resource):
    def __init__(self):
        self.cursor = get_db_cursor()

    @bp.route('/api/planets/')
    def get(self):
        """ Returns a list of planets """

        # filters
        climate = request.args.get('climate', None)
        name = request.args.get('name', None)

        sort = request.args.get('sort', None)

        query = "SELECT name, climate, population FROM planet WHERE 1=1"
        if climate:
            query += " AND climate = '{}'".format(climate)
        if name:
            query += " AND name LIKE '%{}%'".format(name)
        if sort:
            query += " ORDER BY {}".format(sort)
        res = self.cursor.execute(query)
        rows = res.fetchall()

        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['name'] = row[0]
            d['climate'] = row[1]
            d['population'] = row[2]
            objects_list.append(d)

        planets = json.dumps(objects_list)

        return {
            'planets': planets
        }
