from pathlib import Path

from src.json_storage import JsonVacancyStorage
from src.vacancies import Vacancy


def dummy_vacancy(name="Python dev", url="http://hh.ru/1", salary=100000, desc="test"):
    """Функция на простую проверку сохранения, удаления файла"""
    return Vacancy(vacancies_name=name, vacancies_url=url, salary=salary, short_description=desc)


TEST_FILE = Path("data/test.json")


# Перед тестами удаляем старый тестовый файл
def setup_module(module):
    if TEST_FILE.exists():
        TEST_FILE.unlink()


# После тестов удаляем тестовый файл
def teardown_module(module):
    if TEST_FILE.exists():
        TEST_FILE.unlink()


def test_add_and_get_vacancy():
    """Тест на сохранение файла"""
    storage = JsonVacancyStorage("filename=test.json")
    storage.save_file([])
    vac = dummy_vacancy()
    storage.add_vacancy(vac)

    data = storage.get_vacancies()
    assert len(data) == 1
    assert data[0]["vacancies_name"] == "Python dev"
    assert data[0]["salary"] == 100000


def test_delete_vacancy():
    """Тест на удаление файла"""
    storage = JsonVacancyStorage("test.json")
    storage.save_file([])
    vac = dummy_vacancy()
    storage.add_vacancy(vac)
    data = storage.get_vacancies()
    assert len(data) == 1

    storage.delete_vacancy(vac)
    data = storage.get_vacancies()
    assert len(data) == 0
