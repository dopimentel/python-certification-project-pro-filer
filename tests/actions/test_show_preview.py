from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview(capsys, base_context):
    show_preview(base_context)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Found 7 files and 2 directories\n"
        "First 5 files: ["
        "'/path/to/file.sql', '/path/to/file.txt', '/path/to/file2.txt', "
        "'/path/to/FILE.txt', '/path/to/FILE2.TXT']\n"
        "First 5 directories: ['/path', '/to']\n"
    )
    assert captured.err == ""
