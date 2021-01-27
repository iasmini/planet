import collections
from flask import Blueprint, render_template, flash, redirect, url_for
import json
import logging
import requests

from app import db
from app.planet.models import Planet

planet_bp = Blueprint('planet', __name__)


@planet_bp.route('/')
def index():
    return render_template('./planet/index.html')


@planet_bp.route('/init-db/')
def populate_db():
    initialize_db()

    error_message = None
    urls = get_all_urls('http://swapi.dev/api/planets/')
    for url in urls:
        response = requests.get(url)
        planet = response.json()

        try:
            planet['population'] = None if planet['population'] == 'unknown' else planet['population']
            new_planet = Planet(name=planet['name'],
                                rotation_period=planet['rotation_period'],
                                orbital_period=planet['orbital_period'],
                                diameter=planet['diameter'],
                                climate=planet['climate'],
                                gravity=planet['gravity'],
                                terrain=planet['terrain'],
                                surface_water=planet['surface_water'],
                                population=planet['population'])

            db.session.add(new_planet)
            db.session.commit()
        except Exception as e:
            logging.info(e)
            error_message = "Erro ao salvar o planeta {name}. Erro: {planet}".format(name=planet['name'], planet=planet)
            flash(error_message)
            break

    if not error_message:
        flash("Planetas salvos com sucesso.")

    return redirect(url_for("index"))


@planet_bp.route('/planets/')
def get_planets():
    rows = Planet.query.with_entities(Planet.name, Planet.climate, Planet.population)

    objects_list = list()
    for row in rows:
        d = collections.OrderedDict()
        d['name'] = row[0]
        d['climate'] = row[1]
        d['population'] = row[2]
        objects_list.append(d)
    planets = json.dumps(objects_list)

    return render_template('./planet/planets.html', planets=planets)


def initialize_db():
    db.drop_all()
    db.create_all()


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
