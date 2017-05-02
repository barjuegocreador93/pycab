import resources.requires as Rq
from resources.roots import PUBLIC_ROOT

def requires():
    Rq.required('bootstrap','https://github.com/twbs/bootstrap/releases/download/v3.3.7/bootstrap-3.3.7-dist.zip',PUBLIC_ROOT)
    Rq.required('jquery','https://code.jquery.com/jquery-3.2.1.js',PUBLIC_ROOT)
    #more requires here
    #Rq.required(name,url,path)
    print('All requires were installs')