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
    prediction_folder = os.path.realpath('../result/prediction')
    history_folder = os.path.realpath('../result/history')
    static_folder = os.path.realpath('../static-file')

    prediction_file_name = os.path.join(static_folder, 'prediction.zip')
    # Create empty file
    open(prediction_file_name, 'w').close()

    zipf = zipfile.ZipFile(prediction_file_name, 'w', zipfile.ZIP_DEFLATED)
    zipdir(prediction_folder, zipf)
    zipf.close()

    history_file_name = os.path.join(static_folder, 'history.zip')
    # Create empty file
    open(history_file_name, 'w').close()

    zipf2 = zipfile.ZipFile(history_file_name, 'w', zipfile.ZIP_DEFLATED)
    zipdir(history_folder, zipf2)
    zipf2.close()
# %%
