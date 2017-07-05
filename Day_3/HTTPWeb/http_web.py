import requests
""" 
    This application is written in Python 3.6.1.
    It uses the requests library by Kenneth Reitz available at https://github.com/kennethreitz/requests. 
    This library can also be installed via command line by running the command: python -m pip install requests
    The application consumes an API which returns currency rates as obtained from http://api.fixer.io/latest
"""

resp = requests.get('http://api.fixer.io/latest')
if resp.status_code != 200:
    raise requests.HTTPError('http://api.fixer.io/latest: ' + str(resp.status_code))
result = resp.json()
rates = {}
rates = result['rates']
print('This Application lets you find out the foreign exchange rates of \n' + ', '.join(rates.keys()) + '\n' +
      'against the ' + str(result['base']) + ' on ' + str(result['date']) + ' by consuming an API at ' +
      'http://api.fixer.io/latest')


def get_currency():
    currency = input("Enter a currency to find out its exchange rate:\n")
    if currency:
        validate_currency(currency)
    else:
        get_currency()


def validate_currency(currency):
    if currency in rates.keys():
        print('The exchange rate is 1 ' + str(result['base']) + ' = ' + str(rates[currency]) + ' ' + str(currency))
        other = input("Would you like to look for another one? Enter 'Y' for Yes or 'N' for No: \n")
        if other and other == "Y":
            get_currency()
    else:
        print('Currency not found!')
        get_currency()

get_currency()

