"""
Main script to ingest all files in the input folder
"""
import pandas as pd
from src.functions import read_pdf, get_files_in_folder, get_data_path


def main():
    # Get the list of files in the input and output folders
    files_in_input = get_files_in_folder('input')
    
    file_names = []
    file_contents = []
    for file in files_in_input:
        print(file)
        # Read the text from the PDF file
        text = read_pdf(file)
        print(text)
        file_names.append(file)
        file_contents.append(text)
    pdf_df = pd.DataFrame({'file_name': file_names, 'full_contents': file_contents})
    pdf_df.to_csv(get_data_path().joinpath('output', 'results.csv'), index=False)

