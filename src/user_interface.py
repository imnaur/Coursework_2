from typing import List

from src.hh import HH
from src.json_storage import JsonVacancyStorage
from src.vacancies import Vacancy


def display_top_vacancies(vacancies: List[Vacancy], n: int) -> None:
    """
    Показать топ N вакансий по зарплате
    """
    sorted_vacancies = sorted(vacancies, reverse=True)
    for vac in sorted_vacancies[:n]:
        print(vac)


def search_vacancies_by_keyword(vacancies: List[Vacancy], keyword: str) -> List[Vacancy]:
    """
    Найти вакансии по ключевому слову в описании
    """
    return [v for v in vacancies if keyword.lower() in (v.short_description or "").lower()]


def collect_vacancies(hh: HH, query: str, storage: JsonVacancyStorage) -> List[Vacancy]:
    """
    Получить вакансии с hh.ru и сохранить их в хранилище
    """
    raw_vacancies = hh.load_vacancies(query)
    vacancies: List[Vacancy] = []

    for vac_data in raw_vacancies:
        vac = Vacancy(
            vacancies_name=vac_data["name"],
            vacancies_url=vac_data["alternate_url"],
            salary=vac_data["salary"]["from"] if vac_data.get("salary") else None,
            short_description=vac_data["snippet"]["requirement"] if vac_data.get("snippet") else "",
        )
        vacancies.append(vac)
        storage.add_vacancy(vac)

    return vacancies


def user_interaction() -> None:
    """
    Основной интерфейс взаимодействия с пользователем
    """
    storage = JsonVacancyStorage()
    hh = HH(storage)

    print("Поиск вакансий на hh.ru")
    search_query = input("Введите поисковый запрос: ").strip()
    vacancies = collect_vacancies(hh, search_query, storage)

    print(f"Найдено вакансий: {len(vacancies)}")

    while True:
        print("\nВыберите действие:")
        print("1 — Показать топ N вакансий по зарплате")
        print("2 — Найти вакансии по ключевому слову в описании")
        print("0 — Выход")

        choice = input("Ваш выбор: ").strip()
        if choice == "1":
            try:
                n = int(input("Введите количество вакансий: ").strip())
                display_top_vacancies(vacancies, n)
            except ValueError:
                print("Введите корректное число")
        elif choice == "2":
            keyword = input("Введите ключевое слово для поиска: ").strip()
            found = search_vacancies_by_keyword(vacancies, keyword)
            if found:
                for vac in found:
                    print(vac)
            else:
                print("Вакансии не найдены")
        elif choice == "0":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор, попробуйте снова")
