import pytesseract
from PIL import Image
import os

UPLOAD_DIR = "app/static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_and_ocr(file):
    image_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(image_path, "wb") as f:
        f.write(file.file.read())

    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text.strip()
