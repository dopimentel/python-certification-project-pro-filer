from datetime import date
import os
from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details_existing_file(capsys, tmp_path):
    file = tmp_path / "file.txt"
    file.touch()
    file.write_text("Hello, world!")

    last_modified = date.fromtimestamp(os.path.getmtime(str(file)))
    size = os.path.getsize(str(file))
    file_name = str(file).split("/")[-1]
    _, file_extension = os.path.splitext(file_name)

    context = {"base_path": str(file)}

    show_details(context)

    captured = capsys.readouterr()
    expected_output = (
        f"File name: {file_name}\n"
        f"File size in bytes: {size}\n"
        f"File type: {'directory' if os.path.isdir(str(file)) else 'file'}\n"
        f"File extension: {file_extension or '[no extension]'}\n"
        f"Last modified date: {last_modified}\n"
    )
    assert captured.out == expected_output
    assert captured.err == ""


def test_show_details_non_existing_file(capsys):
    file = "some/non/existing/file.txt"

    context = {"base_path": file}

    show_details(context)

    captured = capsys.readouterr()
    assert captured.out == "File 'file.txt' does not exist\n"
    assert captured.err == ""

def test_show_details_file_with_no_extension(capsys, tmp_path):
    file = tmp_path / "file"
    file.touch()

    last_modified = date.fromtimestamp(os.path.getmtime(str(file)))
    size = os.path.getsize(str(file))
    file_name = str(file).split("/")[-1]
    _, file_extension = os.path.splitext(file_name)

    context = {"base_path": str(file)}

    show_details(context)

    captured = capsys.readouterr()
    expected_output = (
        f"File name: {file_name}\n"
        f"File size in bytes: {size}\n"
        f"File type: {'directory' if os.path.isdir(str(file)) else 'file'}\n"
        f"File extension: {file_extension or '[no extension]'}\n"
        f"Last modified date: {last_modified}\n"
    )
    assert captured.out == expected_output
    assert captured.err == ""