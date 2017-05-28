import resources.packages as File


if File.pipinstall('bottle'):
	if File.pipinstall('fileDownloader.py') and File.pipinstall('sqlalchemy') and File.pipinstall('oauth2'):

		print('basiclas installed')

else: print ('You have to install PIP')