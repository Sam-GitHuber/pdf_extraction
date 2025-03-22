"""
Module for getting text from PDF files
"""
import pathlib
import pymupdf
import pandas as pd

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

def extract_file_names(output_file_name: str) -> list[str]:
    """
    Extract file names from a DataFrame
    """
    data_path = get_data_path()
    output_file_path = data_path.joinpath('output', output_file_name)
    df = pd.read_csv(output_file_path
                     , usecols=['file_name'])
    return df['file_name'].tolist()


def build_dataframe(file_names: list[str], contents: list) -> pd.DataFrame:
    """
    Build a DataFrame from a list of file names and content
    """
    return pd.DataFrame({'file_name': file_names, 'contents': contents})
