from timer import time_it


class Market:
    def __init__(self, wines: list = [], beers: list = []) -> None:
        self.no_names = []
        self.store = {}
        for drink in wines + beers:
            if drink.title is not None:
                self.store[drink.title] = drink
            else:
                self.no_names.append(drink)

    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        if title is not None:
            return title in self.store
        return len(self.no_names) != None

    @time_it
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        return list(sorted(self.store.values(), key = lambda drink: drink.title)) + self.no_names

    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        res = list(self.store.values()) + self.no_names
        if from_date:
            res = list(filter(lambda drink: drink.production_date is not None and from_date <= drink.production_date, res))
        if to_date:
            res = list(filter(lambda drink: drink.production_date is not None and drink.production_date <= to_date, res))
        return res
