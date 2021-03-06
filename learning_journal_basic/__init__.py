"""This is the init file for the pyramid server."""
from pyramid.config import Configurator


def main(global_config, **settings):
    """The function returns a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    # config.include('.models')
    config.include(".routes")
    config.include(".views")
    config.scan()
    return config.make_wsgi_app()
