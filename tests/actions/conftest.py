from datetime import date
import os
import pytest
from pro_filer.entities import Context


@pytest.fixture
def base_context() -> Context:
    return {
        "base_path": "any",
        "all_dirs": ["/path", "/to"],
        "all_files": [
            "/path/to/file.sql",
            "/path/to/file.txt",
            "/path/to/file2.txt",
            "/path/to/FILE.txt",
            "/path/to/FILE2.TXT",
            "/path/to/something.txt",
            "/path-to/file.txt",
        ],
    }


@pytest.fixture
def existing_file(tmp_path):
    file_path = tmp_path / "file.txt"
    file_path.touch()
    file_path.write_text("Hello, world!")
    return str(file_path)


@pytest.fixture
def non_existing_file():
    return "some/non/existing/file.txt"


@pytest.fixture
def file_with_no_extension(tmp_path):
    file_path = tmp_path / "file"
    file_path.touch()
    return str(file_path)


@pytest.fixture
def get_file_details():
    def _get_file_details(file_path):
        last_modified = date.fromtimestamp(os.path.getmtime(str(file_path)))
        size = os.path.getsize(str(file_path))
        file_name = str(file_path).split("/")[-1]
        _, file_extension = os.path.splitext(file_name)

        return file_name, size, last_modified, file_extension

    return _get_file_details


@pytest.fixture
def mock_context(existing_file, file_with_no_extension):
    return {
        "all_files": [
            existing_file,
            existing_file,
            file_with_no_extension,
        ]
    }
