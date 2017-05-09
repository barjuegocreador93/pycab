from bottle import re

from routes.web.web import Route


def list_filter(config):
    ''' Matches a comma separated list of numbers. '''
    delimiter = config or ','
    regexp = r'\d+(%s\d)*' % re.escape(delimiter)

    def to_python(match):
        return map(int, match.split(delimiter))

    def to_url(numbers):
        return delimiter.join(map(str, numbers))

    return regexp, to_python, to_url

Route.router.add_filter('list', list_filter)



import resources.oauth2.settings

import routes.web.files
import routes.web.errors