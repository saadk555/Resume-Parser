from audioop import reverse
import ocr
import glob
import os
import platform
from pathlib import Path
import shutil
import pytesseract
from pdf2image import convert_from_path
from PIL import Image


def mainf(filename):

    all_files = []

    if platform.system() == "Windows":

        pytesseract.pytesseract.tesseract_cmd = (r"D:\\Tesseract-OCR\\tesseract.exe")


    pe_path = Path(r"C:\\Program Files\\poppler-0.68.0\bin")
            
    find_word = ''

    inpath = r"D:\python_workspaces\python_ocr_MS\cv-man_flask-version\UPLOAD_FOLDER\\"
    file = inpath + filename


    PDF_file = Path(fr"{file}")
    print(PDF_file)
    final = ocr.main(PDF_file)
    return final


    

   








