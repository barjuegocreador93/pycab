'''
@autor Camilo Barbosa 

@ref github barjuegocreador93

'''

from resources.packages import pathexist
import os
import fileDownloader



import zipfile


def required(package, url, path):
    rq_path = path + '/' + package
    if not pathexist(rq_path):
        os.mkdir(rq_path)
        aurl = url.split('/')
        filename = aurl[len(aurl) - 1]
        filepath = rq_path + '/' + filename
        dw = fileDownloader.DownloadFile(url, filepath)
        dw.download()

        afile = filename.split('.')
        extl = afile[len(afile) - 1]

        if extl == 'zip':

            zf = zipfile.ZipFile(rq_path + '/' + filename, "r")
            for i in zf.namelist():
                zf.extract(i, path=rq_path)

        print(filename + ' was download')
