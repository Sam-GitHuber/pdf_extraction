"""
Module for getting text from PDF files
"""
import pathlib
import pymupdf

def get_data_path():
    """
    Get the path to the data directory
    """
    return pathlib.Path(__file__).parent.parent.joinpath('data')

def read_pdf(file_name: str):
    """
    Read text from a PDF file
    """
    data_path = get_data_path()
    input_pdf_path = data_path.joinpath('input', file_name)

    output_text = ''
    with pymupdf.open(input_pdf_path) as document:
        for page in document:
            output_text += page.get_text()
    return output_text
