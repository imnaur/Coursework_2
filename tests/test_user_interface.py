from unittest.mock import patch

from src.hh import HH
from src.user_interface import user_interaction


@patch("builtins.input", side_effect=["python", "1", "2", "0"])
@patch("builtins.print")
@patch.object(
    HH,
    "load_vacancies",
    return_value=[
        {
            "name": "Python dev",
            "alternate_url": "http://hh.ru/1",
            "salary": {"from": 100000},
            "snippet": {"requirement": "test"},
        }
    ],
)
@patch("src.user_interface.JsonVacancyStorage.add_vacancy")
def test_user_interface(mock_add, mock_load, mock_print, mock_input):
    """Тест на корректный вывод принта"""
    user_interaction()

    # Проверяем, что функция что-то выводила
    printed_texts = [call.args[0] for call in mock_print.call_args_list]
    assert any("Найдено вакансий" in text for text in printed_texts)
