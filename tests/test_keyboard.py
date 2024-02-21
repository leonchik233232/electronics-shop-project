import pytest

from src.Keyboard import Keyboard

def test_instantiate_from_csv_valid():
    file_path = BASE_DIR.joinpath('src', 'items.csv')

    with open(file_path, 'r') as f:
        keyboard = Keyboard.instantiate_from_csv(f)

    assert len(keyboard.items) == 3

def test_instantiate_from_csv_invalid():
    invalid_file_path = BASE_DIR.joinpath('src', 'items_error.csv')

    if os.path.exists(invalid_file_path):
        with open(invalid_file_path, 'r') as f:
            with pytest.raises(InstantiateCSVError):
                Keyboard.instantiate_from_csv(f)
    else:
        with pytest.raises(FileNotFoundError):
            Keyboard.instantiate_from_csv(invalid_file_path)