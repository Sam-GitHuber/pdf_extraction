import pathlib

def get_data_path():
    return pathlib.Path(__file__).parent.parent.joinpath('data')