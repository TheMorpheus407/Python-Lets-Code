#Generate
import pyqrcode
url = pyqrcode.create("https://the-morpheus.de", error='H')
url.png("audio/qrcode.png", scale=5)

#Decode
from PIL import Image
from pyzbar.pyzbar import decode
data = decode(Image.open("audio/qrcode.png"))
print(data)