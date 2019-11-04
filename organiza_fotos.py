import os
from datetime import datetime
from PIL import Image
import shutil

def pasta_para_fotos(file):
    data = data_foto_tirada(file)
    return data.strftime(f'%Y/{data.strftime("%Y-%m-%d")}')

def data_foto_tirada(file):
    foto = Image.open(file)
    info = foto._getexif()
    if 36867 in info:
        data = info[36867]
        data = datetime.strptime(data, '%Y:%m:%d %H:%M:%S')
    else:
        data = datetime.fromtimestamp(os.path.getmtime(file))
    return data

def mover_fotos(file):
    novaPasta = pasta_para_fotos(file)
    if not os.path.exists(novaPasta):
        os.makedirs(novaPasta)
    shutil.move(file, novaPasta + '/' + file)

print(mover_fotos('foto_exemplo.jpg'))
