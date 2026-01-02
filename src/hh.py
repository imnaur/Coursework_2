from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    """Aбстрактный метод для работы с API"""

    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self, keyword: str):
        """Загрузка вакансий по ключевому слову"""
        pass


class HH(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self, file_worker):
        self._url = "https://api.hh.ru/vacancies"
        self._headers = {"User-Agent": "HH-User-Agent"}
        self._params = {"text": "", "page": 0, "per_page": 100}
        self._vacancies = []
        super().__init__(file_worker)

    def _connect(self, params: dict) -> dict:
        """Приватный метод для подключения к API hh.ru"""
        response = requests.get(self._url, params=params, headers=self._headers)
        if response.status_code == 200:
            return response.json()
        return {}

    def load_vacancies(self, keyword: str):
        """Функция на загрузку вакансий"""
        self._params["text"] = keyword
        self._params["page"] = 0
        self._vacancies.clear()

        while self._params["page"] < 20:
            data = self._connect(self._params)  # <-- здесь теперь приватный метод
            vacancies = data.get("items", [])

            if not vacancies:
                break
            self._vacancies.extend(vacancies)
            self._params["page"] += 1

        return self._vacancies
