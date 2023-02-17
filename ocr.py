import platform
from pathlib import Path
from tempfile import TemporaryDirectory
from flask import jsonify
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import re




if platform.system() == "Windows":
	pytesseract.pytesseract.tesseract_cmd = (r"D:\\Tesseract-OCR\\tesseract.exe")
 

pe_path = Path(r"C:\\Program Files\\poppler-0.68.0\bin")
		

def main(PDF_file):

	image_file_list = []
	final_text = ""

	if platform.system() == "Windows":
		pdf_pages = convert_from_path(
			PDF_file, 500, poppler_path=pe_path
		)
	else:
		pdf_pages = convert_from_path(PDF_file, 500)


	for page_enumeration, page in enumerate(pdf_pages, start=1):
		filename = f"D:\python_workspaces\{page_enumeration}.jpg"
		page.save(filename, "JPEG")
		image_file_list.append(filename)

#change this one
	for image_file in image_file_list:
		text = str(((pytesseract.image_to_string(Image.open(image_file)))))
		#text = text.replace("-\n", "")
		final_text += text
		Edu = re.search(r'(EDUCATION|Education:?)[\n|\n\n]([\w\W]*)[\n+\w:?]\n+',text)
		Skills = re.search(r'(SKILLS|Skills:?)[\n|\n\n]([\w\W]*)[\n+\w:?]\n+',text)
		Dic = {"Education": str(Edu.group(2)), 'Skills': str(Skills.group(2)) } 
	return jsonify(Dic)

if __name__ == "__main__":
	main()
