from src.functions import get_data_path

def test_get_data_path():
    data_path = get_data_path()
    assert data_path.is_dir()
    assert data_path.name == 'data'
    assert data_path.parts[-2:] == ('pdf_extraction', 'data')