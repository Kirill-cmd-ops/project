from flask import Blueprint, render_template

views_router = Blueprint("views", __name__)


@views_router.get('/form')
def form():
    return render_template('form.html')


@views_router.get('/info')
def info():
    return render_template('info.html')
