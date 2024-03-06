from datetime import date
import os
from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details_existing_file(capsys, tmp_path):
    file = tmp_path / "file.txt"
    file.touch()
    file.write_text("Hello, world!")

    last_modified = date.fromtimestamp(os.path.getmtime(str(file)))
    size = os.path.getsize(str(file))

    context = {"base_path": str(file)}

    show_details(context)

    captured = capsys.readouterr()
    expected_output = (
        f"File name: file.txt\n"
        f"File size in bytes: {size}\n"
        f"File type: file\n"
        f"File extension: .txt\n"
        f"Last modified date: {last_modified}\n"
    )
    assert captured.out == expected_output
    assert captured.err == ""
