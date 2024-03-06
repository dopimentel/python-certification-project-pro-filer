import os
from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details_existing_file(capsys, existing_file, get_file_details):
    file_name, size, last_modified, file_extension = get_file_details(
        existing_file
    )

    context = {"base_path": existing_file}

    file_type = "directory" if os.path.isdir(existing_file) else "file"

    show_details(context)

    captured = capsys.readouterr()
    expected_output = (
        f"File name: {file_name}\n"
        f"File size in bytes: {size}\n"
        f"File type: {file_type}\n"
        f"File extension: {file_extension or '[no extension]'}\n"
        f"Last modified date: {last_modified}\n"
    )
    assert captured.out == expected_output
    assert captured.err == ""


def test_show_details_non_existing_file(capsys, non_existing_file):
    context = {"base_path": non_existing_file}

    show_details(context)

    captured = capsys.readouterr()
    assert captured.out == "File 'file.txt' does not exist\n"
    assert captured.err == ""


def test_show_details_file_with_no_extension(
    capsys, file_with_no_extension, get_file_details
):
    file_name, size, last_modified, file_extension = get_file_details(
        file_with_no_extension
    )

    context = {"base_path": file_with_no_extension}

    show_details(context)
    file_type = (
        "directory" if os.path.isdir(file_with_no_extension) else "file"
    )
    captured = capsys.readouterr()
    expected_output = (
        f"File name: {file_name}\n"
        f"File size in bytes: {size}\n"
        f"File type: {file_type}\n"
        f"File extension: {file_extension or '[no extension]'}\n"
        f"Last modified date: {last_modified}\n"
    )
    assert captured.out == expected_output
    assert captured.err == ""
