from wine import Wine
from beer import Beer
from market import Market
from datetime import datetime


def date(date_str):
    return datetime.strptime(date_str, '%d.%m.%Y')


if __name__ == '__main__':
    beers = [Beer('Weissbier', date('01.01.2023')),
             Beer('ale', date('01.02.2023')),
             Beer('Stout', date('01.03.2023')),
             Beer('lager', date('01.04.2023')),
             Beer(None, date('01.04.2023')),
             Beer(None, date('01.05.2023'))]
    wines = [Wine('Tempranillo',  date('01.01.2023')),
             Wine('Sauvignon blanc',  date('01.02.2023')),
             Wine('Carmenere',  date('01.04.2023')),
             Wine(None,  date('01.05.2023')),
             Wine('Wine', None),
             Wine(None, None)]
    market = Market(beers=beers, wines=wines)

    print(market.has_drink_with_title('lager'))
    print(market.has_drink_with_title('Lager'))
    print(market.has_drink_with_title(None))
    print(market.get_drinks_sorted_by_title())
    print(market.get_drinks_by_production_date(
        from_date=date('01.02.2023'), to_date=date('01.03.2023')))
    print(market.get_drinks_by_production_date(from_date=date('01.04.2023')))
    print(market.get_drinks_by_production_date(to_date=date('01.01.2022')))
    print(market.get_drinks_by_production_date())


    market = Market(beers=[Beer('Beer' + str(i), i) for i in range(500_000)])
    market.get_drinks_sorted_by_title()
