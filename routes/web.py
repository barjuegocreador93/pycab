
from resources.routes import Route,RouteGroup

import controllers.controller as App

Route.get('/')(App.home)


