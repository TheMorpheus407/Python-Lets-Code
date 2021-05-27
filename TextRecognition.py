#Get tesseract from here: https://github.com/UB-Mannheim/tesseract/wiki

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
import matplotlib.pyplot as plt
from PIL import Image

image = cv2.imread("files/1984_image.PNG")
#image = Image.open("files/1984_image.PNG")

string = pytesseract.image_to_string(image)
print(string)