import pytesseract
import cv2
from PIL import Image
import numpy as np
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ensures consistent language detection
DetectorFactory.seed = 0

# 🧠 Detect the language of given text
def detect_language(text):
    try:
        return detect(text)
    except LangDetectException:
        return "unknown"

# 🧹 Preprocess the image
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

# 🧾 Extract text from image + detect language
def extract_text(image_path):
    img = preprocess_image(image_path)
    pil_img = Image.fromarray(img)

    # OCR with multi-language support (adjust as needed)
    text = pytesseract.image_to_string(pil_img, lang=(
    'eng+hin+tam+kan+tel+ben+guj+mal+urd+nep+fra+deu+ita+spa+por+rus+ara+jpn+chi_sim+kor' ))

    # Detect language of the extracted text
    language = detect_language(text)
    print(language)
    return text, language  # Return both text and language
