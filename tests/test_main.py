from src.main import main
from unittest.mock import patch
import pandas as pd

# mock the pd.to_csv function
@patch('pandas.DataFrame.to_csv')
def test_main(mock_to_csv):
    "this test checks if the main function writes the DataFrame to a CSV file"
    main()
    mock_to_csv.assert_called_once()

# def test_main():
#     "this test simply checks if the main function runs without errors"
#     main()