from typing import Optional, Union


class Vacancy:
    """Класс для хранения информации о вакансии"""

    __slots__ = ("vacancies_name", "vacancies_url", "salary", "short_description")

    def __init__(
        self, vacancies_name: str, vacancies_url: str, salary: Optional[Union[int, str]], short_description: str
    ):
        self.vacancies_name = vacancies_name
        self.vacancies_url = vacancies_url
        self.salary = self._validate_salary(salary)
        self.short_description = short_description

    def _validate_salary(self, salary: Optional[Union[int, str]]) -> int:
        """Приватный метод для валидации зарплаты"""
        if salary is None or salary == "":
            return 0
        if isinstance(salary, str):
            try:
                return int(salary.replace(" ", "").replace(",", ""))
            except ValueError:
                return 0
        return int(salary)

    def __str__(self) -> str:
        """Возвращает строковое представление вакансии"""
        salary_str = f"{self.salary} Руб." if self.salary > 0 else "Зарплата не указана"
        return f"{self.vacancies_name} | {salary_str} | {self.vacancies_url}"

    def __lt__(self, other: object) -> bool:
        """Сравнение вакансий по зарплате для оператора <"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __le__(self, other: object) -> bool:
        """Сравнение вакансий по зарплате для оператора <="""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary <= other.salary

    def __eq__(self, other: object) -> bool:
        """Сравнение вакансий по зарплате для оператора =="""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __gt__(self, other: object) -> bool:
        """Сравнение вакансий по зарплате для оператора >"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary > other.salary

    def __ge__(self, other: object) -> bool:
        """Сравнение вакансий по зарплате для оператора >="""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary >= other.salary
