import platform
from pathlib import Path
from tempfile import TemporaryDirectory
from flask import jsonify
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import json
import openai
import ast
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


	for image_file in image_file_list:
		text = str(((pytesseract.image_to_string(Image.open(image_file)))))
		#text = text.replace("-\n", "") 

		final_text += text

		# Define OpenAI API key 
		openai.api_key = "<your-api>"

		# Set up the model and prompt
		model_engine = "text-davinci-003"
		prompt = final_text + "Please give me the all the data with respective headings as keys. Only dictionary format"

		# Generate a response
		completion = openai.Completion.create(
			engine=model_engine,
			prompt=prompt,
			max_tokens=2048,
			n=1,
			stop=None,
			temperature=0.5,
		)

		response = completion.choices[0].text

		final_resp = ' '.join(response.split('\n')).strip()
		result = ast.literal_eval(re.search('({.+})', final_resp).group(0))

	return jsonify(result)



if __name__ == "__main__":
	main()
