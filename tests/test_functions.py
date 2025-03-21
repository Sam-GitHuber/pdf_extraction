from src.functions import get_data_path, read_pdf

def test_get_data_path():
    data_path = get_data_path()
    assert data_path.is_dir()
    assert data_path.name == 'data'
    assert data_path.parts[-2:] == ('pdf_extraction', 'data')

def test_read_pdf_simple():
    result = read_pdf("minimal-document.pdf")
    assert 'Lorem ipsum dolor sit amet' in result

