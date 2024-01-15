class Drink():
    def __init__(self, title=None, production_date=None) -> None:
        self.title = title
        self.production_date = production_date

    def __str__(self):
        return str(self.title) + ' ' + str(self.production_date)
    
    def __repr__(self):
        return str(self)