from flask import Flask, request, jsonify, send_from_directory
from pdf2docx_converter import convert_pdf_to_docx
import os
from collections.abc import Iterable


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'backend/output/'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and file.filename.endswith('.pdf'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        output_path = os.path.splitext(file_path)[0] + '.docx'
        try:
            convert_pdf_to_docx(file_path, output_path)
            return send_from_directory(app.config['UPLOAD_FOLDER'], os.path.basename(output_path), as_attachment=True)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True)
