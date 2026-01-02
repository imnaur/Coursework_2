from unittest.mock import Mock, patch

from src.hh import HH


class DummyFileWork:
    pass


@patch("src.hh.requests.get")
def test_load_vacancies(mock_get):
    """Тест на ответ API через Mock"""
    first_responce = Mock()
    first_responce.status_code = 200
    first_responce.json.return_value = {
        "items": [{"id": 1, "name": "Python developer"}, {"id": 2, "name": "Backend developer"}]
    }
    second_response = Mock()
    second_response.status_code = 200
    second_response.json.return_value = {"items": []}
    mock_get.side_effect = [first_responce, second_response]
    hh = HH(DummyFileWork())
    vacancies = hh.load_vacancies("python")

    assert len(vacancies) == 2
    assert vacancies[0]["name"] == "Python developer"
    assert vacancies[1]["name"] == "Backend developer"
