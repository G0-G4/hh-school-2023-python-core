from wine import Wine
from beer import Beer
from market import Market

if __name__ == '__main__':
    beers = [Beer('Weissbier', 1), Beer('Ale', 2), Beer('Stout', 3), Beer('lager', 4)]
    wines = [Wine('Tempranillo', 1), Wine('Sauvignon blanc', 2), Wine('Carmenere', 4)]
    market = Market(beers=beers, wines=wines)

    assert(market.has_drink_with_title('Lager'))
    assert(not market.has_drink_with_title('Lagger'))
    assert([x.title for x in market.get_drinks_sorted_by_title()] ==
          ['Ale', 'Carmenere', 'Sauvignon blanc', 'Stout', 'Tempranillo', 'Weissbier', 'lager'])
    assert(market.get_drinks_by_production_date(from_date=6, to_date=6) == [])
    assert(set([x.title for x in market.get_drinks_by_production_date(from_date=1, to_date=3)]) ==
          set(['Weissbier', 'Tempranillo', 'Ale', 'Sauvignon blanc', 'Stout']))
    
    market = Market(beers=[Beer('Beer' + str(i), i) for i in range(500_000)])
    market.get_drinks_sorted_by_title()
