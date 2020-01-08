from server import app
from flask import render_template
import time
from io import BytesIO
import zipfile
from flask.helpers import send_file
import os

@app.route('/prediction')
def zip_prediction():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    fileName = "prediction.zip".format(timestr)
    memory_file = BytesIO()
    file_path = './../result/prediction'
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
          for root, dirs, files in os.walk(file_path):
                    for file in files:
                              zipf.write(os.path.join(root, file), file)
    memory_file.seek(0)
    return send_file(memory_file,
                     attachment_filename=fileName,
                     as_attachment=True)


