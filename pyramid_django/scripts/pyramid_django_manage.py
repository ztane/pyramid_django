import os
import sys

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars
from itertools import takewhile

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value, [var2=value] django management commands\n'
          '(example: "%s development.ini check")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)

    config_uri = argv[1]
    setup_logging(config_uri)

    var_strings = list(takewhile(lambda x: '=' in x, argv[2:]))
    options = parse_vars(var_strings)
    settings = get_appsettings(config_uri, options=options)

    del argv[1:2 + len(var_strings)]
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings['django.settings'])
    sys.path.insert(0, settings['django.project'])
    sys.argv[0] = os.path.join(settings['django.project'], 'manage.py')

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
 
