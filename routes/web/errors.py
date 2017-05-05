import settings

from resources.routes import Route

if not settings.HOST_DEBUG:
    def error(rq):
        return "page not found!"

    Route.error(404)(error)