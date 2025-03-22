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

def get_files_in_folder(folder_name: str):
    """
    Get the list of files in a folder
    """
    data_path = get_data_path()
    folder_path = data_path.joinpath(folder_name)
    return sorted([file.name for file in folder_path.iterdir() if file.is_file()])

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
