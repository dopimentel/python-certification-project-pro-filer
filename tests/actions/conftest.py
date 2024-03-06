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
