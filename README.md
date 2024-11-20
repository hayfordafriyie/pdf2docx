---

# PDF to DOCX Converter Web App

This project is a simple web application that allows users to upload PDF files, which are then processed and converted to DOCX format. The application is built using **Flask** and includes a minimal front-end with HTML and CSS to provide an easy-to-use interface for file uploads.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Configuration](#configuration)
- [License](#license)

---

## Features

- Upload a PDF file from your local system.
- Convert the uploaded PDF file into DOCX format.
- Clean and responsive design with a fixed background image.
- Built using **Flask** for Python backend.
- **CSS** styling for the front-end to ensure a user-friendly experience.

---

## Prerequisites

Before you begin, ensure that you have met the following requirements:

- Python 3.6 or higher
- **Flask** library installed
- A text editor or IDE for editing the code (e.g., Visual Studio Code, PyCharm, etc.)

---

## Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the repository (or download the project files)

You can clone the project repository using the following command:
```bash
git clone https://github.com/yourusername/pdf-to-docx-converter.git
cd pdf-to-docx-converter
```

Alternatively, download the project files as a ZIP and extract them to a directory.

### 2. Set up a virtual environment (Optional but recommended)

It's good practice to set up a virtual environment for your project to manage dependencies. Run the following commands:

```bash
python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows
```

### 3. Install required dependencies

Ensure you have **Flask** installed. If it’s not installed yet, run the following command to install it:

```bash
pip install flask
```

### 4. Install additional libraries for PDF to DOCX conversion (Optional)

If you want to process the uploaded PDF to DOCX (e.g., use a library like `pdf2docx`), you can install it using the following command:

```bash
pip install pdf2docx
```

---

## Usage

### 1. Running the Flask app

To run the Flask app, navigate to the project directory and execute the following command:

```bash
python app.py
```

Flask will start the development server, and you can access the web app by opening your browser and visiting the following URL:

```
http://127.0.0.1:5000/
```

### 2. Uploading a PDF File

Once the app is running:

1. Go to the URL `http://127.0.0.1:5000/` in your web browser.
2. You will see a form asking you to upload a PDF file.
3. Choose a PDF file from your local system and click the **"Convert PDF to DOCX"** button.
4. The file will be uploaded to the server, and you’ll receive a success message (or error if something goes wrong).

The uploaded PDF will be stored in the `uploads` folder in your project directory.

### 3. File Processing (Conversion)

Currently, the app only handles file uploads. You can extend the `upload_file` route to add PDF-to-DOCX conversion using libraries like `pdf2docx`. Example conversion:

```python
from pdf2docx import Converter

def convert_pdf_to_docx(pdf_file_path, docx_file_path):
    cv = Converter(pdf_file_path)
    cv.convert(docx_file_path, start=0, end=None)
    cv.close()
```

---

## Folder Structure

Here is an overview of the project structure:

```
your_project/
│
├── app.py                # Main Python file with Flask application logic
├── templates/            # Folder containing HTML files
│   └── index.html        # HTML file for the upload form
├── static/               # Folder containing static assets (e.g., CSS, images)
│   └── styles.css        # External CSS file for styling
├── uploads/              # Folder to store uploaded files (e.g., PDFs)
└── venv/                 # (Optional) Virtual environment folder (if used)
```

- **app.py**: Contains the main application code to handle routes and file uploads.
- **templates/**: Contains the HTML templates for the front end of the app.
- **static/**: Contains static files like stylesheets and images.
- **uploads/**: The folder where uploaded PDF files are stored temporarily.

---

## Configuration

You can configure the following parameters for your Flask app:

- **UPLOAD_FOLDER**: This is the directory where uploaded files will be stored. The default is set to a folder called `uploads`. You can change the directory path to another location if needed.

```python
UPLOAD_FOLDER = 'uploads'
```

- **Flask debug mode**: By default, Flask is in debug mode for easier development. You can disable it in production environments by setting `app.debug = False`.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Additional Notes

- This project uses **Flask**, a micro-framework for Python. It's easy to extend the application with additional features (like PDF-to-DOCX conversion or even serving a front-end built with frameworks like React).
- **Security**: Make sure to implement proper file handling and validation before deploying the app to production (e.g., checking file types, file size, etc.).
- **Error Handling**: Improve the user experience by adding more error messages when files fail to upload or are of the wrong type.

---

Feel free to modify and extend this application according to your requirements. If you encounter any issues, feel free to reach out or create an issue in the project’s GitHub repository.

--- 

