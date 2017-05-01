import resources.packages as File

if File.pipinstall('bottle'):
	if File.pipinstall('fileDownloader.py'):

		print('basiclas installed')

else: print ('You have to install PIP')