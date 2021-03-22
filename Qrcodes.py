# Generate
import pyqrcode

url = pyqrcode.create("https://the-morpheus.de", error='H')
url.png("audio/qrcode.png", module_color=(0, 255, 0, 255), background=(0, 0, 0, 255), scale=10)

# Decode
from PIL import Image
from pyzbar.pyzbar import decode

data = decode(Image.open("audio/qrcode.png"))
print(data)
