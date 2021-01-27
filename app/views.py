import collections
import json
import logging
import requests

from flask import Blueprint, render_template, redirect, flash, url_for

from db.db import init_db, get_db, get_db_cursor

bp = Blueprint('planet', __name__)


@bp.route('/')
def index():
    return render_template('planet/index.html')


@bp.route('/init-db/')
def initialize_db():
    init_db()

    db = get_db()

    error_message = None
    urls = get_all_urls('http://swapi.dev/api/planets/')
    for url in urls:
        response = requests.get(url)
        planet = response.json()

        try:
            planet['population'] = 'null' if planet['population'] == 'unknown' else planet['population']
            sql = """insert into planet (name, rotation_period, orbital_period, diameter, climate, gravity,
                       terrain, surface_water, population) values ('{name}', '{rotation_period}', '{orbital_period}',
                       '{diameter}', '{climate}', '{gravity}', '{terrain}', '{surface_water}', {population});""".format(
                name=planet['name'], rotation_period=planet['rotation_period'], orbital_period=planet['orbital_period'],
                diameter=planet['diameter'], climate=planet['climate'], gravity=planet['gravity'],
                terrain=planet['terrain'], surface_water=planet['surface_water'], population=planet['population'])
            db.execute(sql)
            db.commit()
        except Exception as e:
            logging.info(e)
            error_message = "Erro ao salvar o planeta {name}. Erro: {planet}".format(name=planet['name'], planet=planet)
            flash(error_message)
            break

    if not error_message:
        flash("Planetas salvos com sucesso.")

    return redirect(url_for("index"))


@bp.route('/planets/')
def get_planets():
    cursor = get_db_cursor()
    query = "SELECT name, climate, population FROM planet ORDER BY name DESC"
    cursor.execute(query)
    rows = cursor.fetchall()

    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['name'] = row[0]
        d['climate'] = row[1]
        d['population'] = row[2]
        objects_list.append(d)
    planets = json.dumps(objects_list)

    return render_template('planet/planets.html', planets=planets)


def get_all_urls(url):
    urls = []
    has_next = True
    while has_next:
        response = requests.get(url)
        json_data = json.loads(response.content)
        for resource in json_data['results']:
            urls.append(resource['url'])
        if bool(json_data['next']):
            url = json_data['next']
        else:
            has_next = False
    return urls
