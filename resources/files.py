import os,sys,os.path
import resources.fileDownloader as fileDownloader
import zipfile


def pathexist(path):
	return os.path.exists(path)
	
	
def required(filename,extl,url,path):
	
	rq_path=path+'/'+filename
	if not pathexist(rq_path):
		os.mkdir(rq_path)
		filepath=rq_path+'/'+filename
		dw = fileDownloader.DownloadFile(url,rq_path+'/'+filename+extl)
		dw.download()
		
		
		
		if extl =='.zip':
			
			
			zf=zipfile.ZipFile(rq_path+'/'+filename+extl, "r")
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
	