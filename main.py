import zipfile
import os


def zip_(path: str, z_path: str):
    z_file = zipfile.ZipFile(z_path, 'w')
    if os.path.isfile(path):
        z_file.write(path)
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                z_file.write(root + os.sep + file)
    z_file.close()


zip_('archive_folder', 'archive.zip')
