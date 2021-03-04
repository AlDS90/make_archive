import zipfile


def zip_(path: str, z_path: str):
    z_file = zipfile.ZipFile(z_path, 'w')
    z_file.write(path)
    z_file.close()


zip_('1.txt', 'archive.zip')
