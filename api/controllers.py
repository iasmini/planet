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
        # page = request.args.get('page', 1, type=int)

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
                rows = Planet.query.all()

        planets = list()
        for row in rows:
            planets.append(row.to_dict())

        # exibe somente resultados de acordo com a pagina informada na url
        if page:
            planets = get_paginated_planets(planets, '/planets', page=page)

            return planets
        else:
            return {"status_code": 200, "response": planets}


def get_paginated_planets(results, url, page):
    count = len(results)

    if count == 0:
        message = 'Não foram encontrados planetas de acordo com os parâmetros informados.'
        return {"status_code": 400, "response": message}

    page = int(page)
    items_per_page = int(current_app.config['ITEMS_PER_PAGE'])
    max_page = int(count / items_per_page)
    if max_page == 0:
        max_page = 1

    if page < 0:
        message = 'Página {page} não existe. Página mínima 1.'.format(page=page)
        return {"status_code": 400, "response": message}

    if page > max_page:
        message = 'Página {page} não existe. Página máxima de acordo com os parâmetros informados: {max_page}.'.format(
            page=page, max_page=max_page)
        return {"status_code": 400, "response": message}

    obj = dict()
    obj['page'] = page
    obj['items_per_page'] = items_per_page
    obj['count'] = count

    # gera previous url
    if page == 1:
        obj['previous'] = ''
    else:
        previous_page = page - 1
        obj['previous'] = url + '?page={}'.format(previous_page)

    # gera next url
    if page == max_page:
        obj['next'] = ''
    else:
        next_page = page + 1
        obj['next'] = url + '?page={}'.format(next_page)

    # seleciona os resultados de acordo com limite inicial e final
    obj['results'] = results[(page * items_per_page - items_per_page):(page * items_per_page)]

    return {"status_code": 200, "response": obj}
