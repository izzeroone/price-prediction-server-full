# %%
import shutil
import os
import sys
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), file)

if __name__ == '__main__':
    zip_folder = os.path.realpath('../result/prediction')
    static_folder = os.path.realpath('../static-file')
    print(zip_folder)
    print(static_folder)
    zip_file_name = os.path.join(static_folder, 'prediction.zip')
    open(zip_file_name, 'a').close()
    zipf = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
    zipdir(zip_folder, zipf)
    zipf.close()
# %%
