# Classe para fazer a manipulação de imagens:
from PIL import Image
import os

local = os.getcwd()
os.chdir("./image")


name = 'lena4.jpg'

# Carregar um imagem a partir do disco:
imagexxx = Image.open("./"+name)

"""
print(imagexxx.format)
print(imagexxx.mode)
print(imagexxx.size)
"""
imagenew =imagexxx.transpose(Image.ROTATE_90)
imagenew.save("./"+name)
imagenew.show()
imagexxx.close()

"""
PIL.Image.FLIP_LEFT_RIGHT
PIL.Image.FLIP_TOP_BOTTOM
PIL.Image.ROTATE_90 #Vira sempre pra esquerda
PIL.Image.ROTATE_180
PIL.Image.ROTATE_270
PIL.Image.TRANSPOSE or PIL.Image.TRANSVERSE.
"""


