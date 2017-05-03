from bottle import static_file
import settings

from bottle import re
from routes.web import Route

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


import routes.files
import routes.errors

