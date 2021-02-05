import json
import logging
import requests

from functools import reduce
from urllib.parse import urljoin

from flask import Blueprint, render_template, flash, redirect, url_for, current_app

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
    base_url = current_app.config['BASE_URL']

    try:
        url = reduce(urljoin, [base_url, "/api/planets/"])
        response = requests.get(url)
    except Exception as e:
        flash("Erro ao listar os planetas. Erro: {}".format(e))
        return redirect(url_for("index"))
    else:
        if response.json()['status_code'] == 200:
            planets = response.json()
            return render_template('./planet/planets.html', planets=json.dumps(planets['response']['results']))
        else:
            flash(response.json()['message'])
            return redirect(url_for("index"))


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
