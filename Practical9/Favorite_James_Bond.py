def Birth_rate_calculator(Birth_year):
    if 1955<=Birth_year<=1968:
        print('Favorite James Bond actor is Roger Moore')
    if 1969<=Birth_year<=1976:
        print('Favorite James Bond actor is Timothy Dalton')
    if 1977<=Birth_year<=1983:
        print('Favorite James Bond actor is Pierce Brosnan')
    if 1984<=Birth_year<=2003:
        print('Favorite James Bond actor is Daniel Craig')
    else:
        print('There is no James Bond actor when the individual turn to 18')
Birth_year=int(input('Please enter your birth year: '))
Birth_rate_calculator(Birth_year)