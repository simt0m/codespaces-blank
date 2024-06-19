import pytest
from data import items_list
from main import find_item_by_id, add_new_item_to_list, borrow_item


@pytest.fixture  # Decorator fixture
def mock_item():
    return {
        'ID': '11',
        'Type': 'Headset',
        'Model': 'item_model',
        'Features': 'item_features',
        'Rate': 0.0,
        'RateCount': 0,
        'Status': 'Available',
        'User': 'n/a',
        'User email': 'n/a',
        'Due by': 'n/a',
        'Cost': 50.0,
        'Short description': 'item_short_description'
    }


def test_find_item_by_id():
    assert find_item_by_id("1") == items_list[0]
    assert find_item_by_id("fdsfs") == None
    assert find_item_by_id(1) == None
    assert isinstance(find_item_by_id("5"), dict)


def test_add_new_item_to_list(mock_item):
    old_length = len(items_list)
    add_new_item_to_list(items_list, mock_item)
    new_length = len(items_list)
    assert (old_length + 1) == new_length


def test_borrow_item(mock_item, monkeypatch):
    # Mock inputs for name and email
    def mock_input(prompt):
        if prompt.lower() == "please enter your name: ":
            return "Thomas Smith"
        elif prompt.lower() == "please enter your email address: ":
            return "tsmith@gmail.com"
  
    monkeypatch.setattr('builtins.input', mock_input)
    borrow_item(mock_item)

    assert mock_item["Status"] == "Being used"
    assert mock_item["User"] == "Thomas Smith"
    assert mock_item["User email"] == "tsmith@gmail.com"
    assert mock_item["Due by"] != "n/a"