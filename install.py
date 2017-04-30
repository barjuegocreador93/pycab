import resources.files as File
from settings import ROOT

if File.pipinstall('bottle'):

	File.required('bootstrap','.zip','https://github.com/twbs/bootstrap/releases/download/v3.3.7/bootstrap-3.3.7-dist.zip',ROOT +'/public')
	
	File.required('jquery','.js','https://code.jquery.com/jquery-3.2.1.js',ROOT+'/public')
	