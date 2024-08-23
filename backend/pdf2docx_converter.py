# from pdf2docx import Converter

# # Define the path to your PDF and output DOCX files
# pdf_path = './input.pdf'
# docx_path = './output.docx'

# # Instantiate the Converter with the path to the PDF file
# try:
#     cv = Converter(pdf_path)
#     # Convert the PDF to DOCX
#     cv.convert(docx_path, start=0, end=None)
#     cv.close()
#     print("Conversion successful!")
# except FileNotFoundError:
#     print(f"Error: The file '{pdf_path}' does not exist.")
# except Exception as e:
#     print(f"An error occurred: {e}")


# from pdf2docx import Converter
# import os

# # Get the absolute path of the current directory
# current_directory = os.path.dirname(os.path.abspath(__file__))

# # Build paths relative to the current directory
# pdf_path = os.path.join(current_directory, 'input.pdf')
# docx_path = os.path.join(current_directory, 'output.docx')

# print(f"PDF Path: {pdf_path}")  # Debugging line
# print(f"DOCX Path: {docx_path}")  # Debugging line

# import os
# from pdf2docx import Converter

# # Get the absolute path of the current directory
# current_directory = os.path.dirname(os.path.abspath(__file__))

# # Build paths relative to the current directory
# pdf_path = os.path.join(current_directory, 'input.pdf')
# docx_path = os.path.join(current_directory, 'output.docx')

# try:
#     cv = Converter(pdf_path)
#     cv.convert(docx_path, start=0, end=None)
#     cv.close()
#     print("Conversion successful!")
# except FileNotFoundError:
#     print(f"Error: The file '{pdf_path}' does not exist.")
# except Exception as e:
#     print(f"An error occurred: {e}")





# from pdf2docx import Converter

# # Use the absolute path to ensure the file is found
# pdf_path = '/Users/saurabhsingh/Desktop/saas/pdfword/backend/DemandLoanLetter.pdf'
# docx_path = '/Users/saurabhsingh/Desktop/saas/pdfword/backend/output.docx'

# try:
#     cv = Converter(pdf_path)
#     cv.convert(docx_path, start=0, end=None)
#     cv.close()
#     print("Conversion successful!")
# except FileNotFoundError:
#     print(f"Error: The file '{pdf_path}' does not exist.")
# except Exception as e:
#     print(f"An error occurred: {e}")

from pdf2docx import Converter

def convert_pdf_to_docx(pdf_path, docx_path):
    try:
        cv = Converter(pdf_path)
        cv.convert(docx_path, start=0, end=None)
        cv.close()
    except Exception as e:
        raise RuntimeError(f"An error occurred during conversion: {e}")
