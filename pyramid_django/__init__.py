import os
import sys
from django.core.wsgi import get_wsgi_application
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
   
    django_project = settings['django.project']
    django_settings = settings['django.settings']
    
    django_project = os.path.abspath(django_project)
    sys.path.insert(0, django_project)
    config = Configurator(settings=settings)
    config.scan(django_settings)
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings)
    django_application = get_wsgi_application()
    
    class LegacyView(object):
        def __init__(self, app):
            self.app = app
        def __call__(self, request):
            return request.get_response(self.app)

    django_view = LegacyView(django_application)
    config.add_notfound_view(django_view)
    return config.make_wsgi_app()
