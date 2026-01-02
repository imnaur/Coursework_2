import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from src.storage import VacancyStorage
from src.vacancies import Vacancy


class JsonVacancyStorage(VacancyStorage):
    """Класс для хранения вакансий в JSON формате"""

    def __init__(self, filename: str = "vacancies.json") -> None:
        self._data_dir: Path = Path("data")
        self._data_dir.mkdir(exist_ok=True)
        self._file_path: Path = self._data_dir / filename

    def load_file(self) -> List[Dict[str, Any]]:
        """Загрузка данных из JSON-файла"""
        if not self._file_path.exists():
            return []
        with open(self._file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_file(self, data: List[Dict[str, Any]]) -> None:
        """Сохранение данных в JSON-файл"""
        with open(self._file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавление вакансии в JSON (без дубликатов)"""
        data: List[Dict[str, Any]] = self.load_file()
        vacancy_dict: Dict[str, Any] = {
            "vacancies_name": vacancy.vacancies_name,
            "vacancies_url": vacancy.vacancies_url,
            "salary": vacancy.salary,
            "short_description": vacancy.short_description,
        }

        # Проверка на дубликаты
        if not any(
            v["vacancies_name"] == vacancy.vacancies_name and v["vacancies_url"] == vacancy.vacancies_url for v in data
        ):
            data.append(vacancy_dict)
            self.save_file(data)

    def get_vacancies(self, criteria: Optional[Dict[str, int]] = None) -> List[Dict[str, Any]]:
        """Получить вакансии по критериям (salary_min, salary_max)"""
        data: List[Dict[str, Any]] = self.load_file()
        if criteria is None:
            return data

        filtered: List[Dict[str, Any]] = []
        for vacancy in data:
            if "salary_min" in criteria and vacancy["salary"] < criteria["salary_min"]:
                continue
            if "salary_max" in criteria and vacancy["salary"] > criteria["salary_max"]:
                continue
            filtered.append(vacancy)
        return filtered

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удалить вакансию из JSON"""
        data: List[Dict[str, Any]] = self.load_file()
        data = [
            v
            for v in data
            if not (v["vacancies_name"] == vacancy.vacancies_name and v["vacancies_url"] == vacancy.vacancies_url)
        ]
        self.save_file(data)
