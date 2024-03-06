import os
from unittest.mock import patch
from pro_filer.actions.main_actions import show_disk_usage  # NOQA


def test_show_disk_usage(capsys, mock_context):
    with patch(
        "pro_filer.actions.main_actions._get_printable_file_path"
    ) as mock_get_printable_file_path:
        # Configuração do mock para _get_printable_file_path
        mock_get_printable_file_path.return_value = "file.txt".ljust(70)

        # Chama a função que será testada
        show_disk_usage(mock_context)

        # Captura a saída do teste
        captured = capsys.readouterr()

        # Calcula o total_size esperado usando a mesma
        # lógica que a função original

        mock_sum = sum(
            os.path.getsize(file) for file in mock_context["all_files"]
        )
        expected_output = ""
        for file_path in sorted(
            mock_context["all_files"], key=os.path.getsize, reverse=True
        ):
            file_size = os.path.getsize(file_path)
            expected_output += (
                f"'{mock_get_printable_file_path.return_value}':"
                f" {file_size} ({int(file_size / mock_sum * 100)}%)\n"
            )
        expected_output = (
            expected_output + "Total size: " + str(mock_sum) + "\n"
        )

        assert captured.out == expected_output
