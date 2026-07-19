from flask import Blueprint, render_template

blueprint = Blueprint('blueprint', __name__, static_folder='static', template_folder='templates')

# Cache will be injected by main.py
cache = None

def init_cache(cache_instance):
    """Initialize cache from main.py"""
    global cache
    cache = cache_instance

@blueprint.route('/')
def home():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='home')
        def _cached():
            return render_template("home.html")
        return _cached()
    return render_template("home.html")

@blueprint.route('/sources')
def references():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='references')
        def _cached():
            return render_template("resources.html")
        return _cached()
    return render_template("resources.html")

@blueprint.route('/formulations')
def formulations():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='formulations')
        def _cached():
            return render_template("formulations.html")
        return _cached()
    return render_template("formulations.html")

@blueprint.route('/theodicies')
def theodicies():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='theodicies')
        def _cached():
            return render_template("theodicies.html")
        return _cached()
    return render_template("theodicies.html")

@blueprint.route('/biblical')
def biblical():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='biblical')
        def _cached():
            return render_template("biblical.html")
        return _cached()
    return render_template("biblical.html")
