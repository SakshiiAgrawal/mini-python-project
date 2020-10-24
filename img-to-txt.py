import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert():
    img = Image.open('4.jpg')
    text = pytesseract.image_to_string(img)
    print(text)

convert()
