from drink import Drink


class Wine(Drink):
    def __init__(self, title=None, production_date=None) -> None:
        super().__init__(title, production_date)
