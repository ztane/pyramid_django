import os
import sys
from pyramid_django.handlers import get_django_view
from pyramid_django.request import PyramidDjangoRequest

from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
   
    django_project = settings['django.project']
    django_settings = settings['django.settings']
    
    django_project = os.path.abspath(django_project)
    sys.path.insert(0, django_project)

    config = Configurator(settings=settings, request_factory=PyramidDjangoRequest)
    # config.scan(django_settings.rpartition('.')[0])
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings)
    django_view = get_django_view()
    config.add_notfound_view(django_view)
    return config.make_wsgi_app()
