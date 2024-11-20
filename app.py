from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import PyPDF2
import os
from docx import Document
from pdf2image import convert_from_path
import pytesseract

app = Flask(__name__)


UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
ALLOWED_EXTENSIONS = {'pdf'}


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER


os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_pdf_text(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page_text = page.extract_text()
            
            if page_text:
                text += f"Page {page_num + 1}:\n{page_text}\n\n"  
            else:
                
                print(f"No text found in page {page_num + 1}, using OCR.")
                images = convert_from_path(pdf_path, first_page=page_num + 1, last_page=page_num + 1)
                page_text = pytesseract.image_to_string(images[0])
                text += f"Page {page_num + 1} (OCR):\n{page_text}\n\n"
    return text


def convert_to_docx(text, output_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/upload', methods=['POST'])
def upload_file():
   
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    
    
    if file.filename == '':
        return 'No selected file', 400
    
   
    if file and allowed_file(file.filename):
        
        filename = secure_filename(file.filename)
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(pdf_path)
        
        
        text = extract_pdf_text(pdf_path)
        
        
        docx_filename = filename.rsplit('.', 1)[0] + '.docx'
        docx_path = os.path.join(app.config['OUTPUT_FOLDER'], docx_filename)
        
      
        convert_to_docx(text, docx_path)
        
      
        return send_file(docx_path, as_attachment=True)

    return 'Invalid file type. Please upload a PDF.', 400

if __name__ == '__main__':
    app.run(debug=True) 
