import filecmp
import itertools
import pytest
from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


def test_find_duplicate_no_existing_file(base_context):
    with pytest.raises(ValueError) as excinfo:
        find_duplicate_files(base_context)
    assert "All files must exist" in str(excinfo.value)


def test_find_duplicate_files(mock_context):
    duplicate_files = []
    for file1, file2 in itertools.combinations(mock_context["all_files"], 2):
        try:
            if filecmp.cmp(file1, file2, shallow=False):
                duplicate_files.append((file1, file2))

        except FileNotFoundError:
            continue
    assert find_duplicate_files(mock_context) == duplicate_files
