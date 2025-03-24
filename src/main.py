"""
Main script to ingest all files in the input folder
"""

from src.functions import read_pdf, get_files_in_folder, extract_file_names


def main():
    # Get the list of files in the input and output folders
    files_in_input = get_files_in_folder('input')
    files_in_output = get_files_in_folder('output')
    files_ingested = []
    for output_file in files_in_output:
        files_ingested.extend(extract_file_names(output_file))
    print(f'Files ingested: {files_ingested}')
    # Get the list of files to process
    files_to_process = list(set(files_in_input) - set(files_in_output))
    print(f'Files to process: {files_to_process}')
    # Process the files
    file_names = []
    full_contents = []
    for pdf_file in files_to_process:
        print(f'Processing {pdf_file}')
        full_contents = read_pdf(pdf_file)
        file_names.append(pdf_file)
        full_contents.append(full_contents)
    # Build the DataFrame
    df = build_dataframe(file_names, full_contents)
    # Save the DataFrame
    output_file_name = 'output.csv'
    output_file_path = get_data_path().joinpath('output', output_file_name)
    df.to_csv(output_file_path, index=False)
    df.to_csv('data/output/output.csv', index=False)
        print(full_contents)
