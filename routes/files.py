from resources.roots import PUBLIC_ROOT
from bottle import static_file
from resources.routes import Route

'''files - routes'''


def pub(filename):
    return static_file(filename, root=PUBLIC_ROOT)


Route.get('/public/:filename')(pub)


def pub(filename, dirname):
    return static_file(filename, root=PUBLIC_ROOT + dirname)


Route.get('/public/:dirname/:filename')(pub)


def pub(filename, dirname, framework):
    return static_file(filename, root=PUBLIC_ROOT + framework + "/" + dirname)


Route.get('/public/:framework/:dirname/:filename')(pub)


def pub(filename, dirname, framework, required):
    return static_file(filename, root=PUBLIC_ROOT + required + "/" + framework + "/" + dirname)


Route.get('/public/:required/:framework/:dirname/:filename')(pub)
