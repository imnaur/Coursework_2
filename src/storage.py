from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from src.vacancies import Vacancy  # чтобы типизировать аргументы


class VacancyStorage(ABC):
    """
    Абстрактный класс-коннектор для хранения вакансий.
    Задаёт методы, которые обязательно нужно реализовать.
    """

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавить вакансию в хранилище"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Получить вакансии по критериям."""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удалить вакансию с хранилища"""
        pass
