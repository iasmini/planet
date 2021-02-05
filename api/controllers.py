from flask import request, Blueprint, current_app
from flask_restful import Resource
from sqlalchemy.sql import text

from app.planet.models import Planet

bp = Blueprint('api', __name__)


class ApiResource(Resource):
    @bp.route('/api/planets/')
    def get(self):
        """ Returns a list of planets """
        # filters
        climate = request.args.get('climate', None)
        name = request.args.get('name', None)

        sort = request.args.get('sort', None)

        page = request.args.get('page', None, type=int)

        if page and page < 0:
            message = 'Página {page} não existe. Página mínima 1.'.format(page=page)
            return {"status_code": 400, "response": message}

        filters = ''
        if climate:
            filters = "climate='" + climate + "'"

        if name:
            if filters:
                filters += " AND "
            filters += "name LIKE '%" + name + "%'"

        if filters:
            rows = Planet.query.filter(text(filters))

            if sort:
                rows = rows.order_by(text(sort))
        else:
            if sort:
                rows = Planet.query.order_by(text(sort)).all()
            else:
                rows = Planet.query

        planets = list()
        # exibe somente resultados de acordo com a pagina informada na url
        if page:
            rows = rows.paginate(page, current_app.config['ITEMS_PER_PAGE'], False)
            for row in rows.items:
                planets.append(row.to_dict())
        else:
            for row in rows:
                planets.append(row.to_dict())

        response = dict()
        response['status_code'] = 200

        response['response'] = dict()

        if page:
            response['response']['page'] = page
            response['response']['items_per_page'] = current_app.config['ITEMS_PER_PAGE']

        response['response']['results'] = planets

        return response
