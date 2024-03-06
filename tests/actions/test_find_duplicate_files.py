import pytest
from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


def test_find_duplicate_no_existing_file(base_context):
    with pytest.raises(ValueError) as excinfo:
        find_duplicate_files(base_context)
    assert "All files must exist" in str(excinfo.value)
