Birth_year=int(input('Please enter your birth year: '))
def Birth_rate_calculator(Birth_year):
    if 1955<=Birth_year<=1968:
        return('Roger Moore')
    if 1969<=Birth_year<=1976:
        return('Timothy Dalton')
    if 1977<=Birth_year<=1983:
        return('Pierce Brosnan')
    if 1984<=Birth_year<=2003:
        return('Daniel Craig')
    else:
        return('no actor')


# Example
print('I was born in 2004 and my favorate James Bond actor is', Birth_rate_calculator(2004))
# output: I was born in 2004 and my favorate James Bond actor is no actor, because James Bond does not exist in my era