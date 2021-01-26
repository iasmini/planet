from flask import Blueprint, render_template, redirect, flash, url_for

from db.db import init_db

bp = Blueprint('planet', __name__)


@bp.route('/')
def index():
    return render_template('planet/index.html')


@bp.route('/init-db/')
def initialize_db():
    init_db()
    flash("Banco de dados inicializado.")
    return redirect(url_for("index"))
