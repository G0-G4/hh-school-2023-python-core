from timer import time_it

class Market:
    def __init__(self, wines: list = [], beers: list = []) -> None:
        self.store = {drink.title.lower() : drink for drink in wines + beers}

    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title.lower() in self.store

    @time_it
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        return list(sorted(self.store.values(), key = lambda x: x.title))

    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        return list(filter(lambda x: from_date <= x.production_date <= to_date, self.store.values()))
