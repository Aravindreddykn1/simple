# backend/ocr.py
import easyocr
import pytesseract
from PIL import Image

reader = easyocr.Reader(['en'])

def extract_text(image_path):
    text_easy = reader.readtext(image_path, detail=0)
    text_tesseract = pytesseract.image_to_string(Image.open(image_path))
    return {"easyocr": text_easy, "tesseract": text_tesseract}
