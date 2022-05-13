import os
import tarfile
import zipfile


def untargz(targz_file, remove_flag=False):
    path = os.path.dirname(targz_file)
    targz = tarfile.open(targz_file)
    targz.extractall(path=path)
    targz.close()
    if remove_flag:
        os.remove(targz_file)


def unzip(zip_file, remove_flag=False):
    path = os.path.dirname(zip_file)
    zip_file = zipfile.ZipFile(zip_file)
    zip_file.extractall(path=path)
    zip_file.close()
    if remove_flag:
        os.remove(zip_file)
