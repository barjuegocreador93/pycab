import os,sys,os.path
import resources.fileDownloader as fileDownloader
import zipfile


def pathexist(path):
	return os.path.exists(path)
	
	
def required(package,url,path):
	
	rq_path=path+'/'+package
	if not pathexist(rq_path):
		os.mkdir(rq_path)
		aurl=url.split ('/')
		filename=aurl[len(aurl)-1]
		filepath=rq_path+'/'+filename
		dw = fileDownloader.DownloadFile(url,filepath)
		dw.download()
		
		afile=filename . split  ('.')
		extl=afile [len (afile)-1]
		
		if extl =='zip':
			
			
			zf=zipfile.ZipFile(rq_path+'/'+filename, "r")
			for i in zf.namelist():
				zf.extract(i, path=rq_path)
				
		print(filename+' was download')
				
		
def modcmd(arg):
  os.system(sys.executable+" "+sys.prefix+"/bin/"+arg)

		
def pipinstall(module):
	if pathexist(sys.prefix+'/bin/pip'):
		modcmd('pip install '+module)
		return True
	return False
	