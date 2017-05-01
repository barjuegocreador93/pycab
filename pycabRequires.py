import resources.requires as Rq
from settings import ROOT

Rq.required('bootstrap','https://github.com/twbs/bootstrap/releases/download/v3.3.7/bootstrap-3.3.7-dist.zip',ROOT +'/public')
Rq.required('jquery','https://code.jquery.com/jquery-3.2.1.js',ROOT+'/public')
print('All requires were installs')