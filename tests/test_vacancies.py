from src.vacancies import Vacancy


def test_vacancy_salary_validation():
    """Тест на правильную валидацию"""
    vac1 = Vacancy("Python dev", "http://hh.ru/1", None, "test")
    assert vac1.salary == 0

    # зарплата пустая строка → 0
    vac2 = Vacancy("Python dev", "http://hh.ru/2", "", "test")
    assert vac2.salary == 0

    # зарплата строкой с пробелами → преобразуется в int
    vac3 = Vacancy("Python dev", "http://hh.ru/3", "100 000", "test")
    assert vac3.salary == 100000

    # зарплата числом → сохраняется как int
    vac4 = Vacancy("Python dev", "http://hh.ru/4", 120000, "test")
    assert vac4.salary == 120000


def test_vacancy_str_method():
    """Тест на правильную валидацию"""
    vac = Vacancy("Python dev", "http://hh.ru/1", 100000, "test")
    assert str(vac) == "Python dev | 100000 Руб. | http://hh.ru/1"

    vac_no_salary = Vacancy("Python dev", "http://hh.ru/2", None, "test")
    assert str(vac_no_salary) == "Python dev | Зарплата не указана | http://hh.ru/2"


def test_vacancy_comparison():
    """Тест на правильную валидацию"""
    vac_low = Vacancy("Junior", "http://hh.ru/1", 50000, "test")
    vac_high = Vacancy("Senior", "http://hh.ru/2", 150000, "test")
    vac_equal = Vacancy("Mid", "http://hh.ru/3", 50000, "test")

    assert vac_low < vac_high
    assert vac_low <= vac_high
    assert vac_high > vac_low
    assert vac_high >= vac_low
    assert vac_low == vac_equal
    assert vac_low <= vac_equal
    assert vac_low >= vac_equal
