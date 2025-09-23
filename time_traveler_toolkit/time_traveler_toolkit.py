from datetime import datetime as dt
from decimal import Decimal as dc
from random import randint, choice
from custom_module import generate_time_travel_message

current_date = dt.now()
formated_current_date = dt.strftime(current_date, '%a %d, %B %Y - %H:%M')

base_cost = dc("10000.00")

target_year = randint(2000, 2030)

destinations = ["San Francisco", "Japan", "Barcelona"]
random_destination = choice(destinations)

diff_years = abs(current_date.year - target_year)

cost = base_cost * dc(diff_years)

generate_time_travel_message(target_year, random_destination, cost)
