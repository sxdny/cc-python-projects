# 23-09-2025

from datetime import datetime

birthday = datetime(2004, 8, 8) # nos crea un datetime object
print(birthday.weekday()) # output 6 --> sábado

print(datetime.now())

# tambien se pueden hacer restas (solo)

# ver en los python docs los formatos de fechas
parsed_date = datetime.strptime('Jan 31, 2014', '%b %d, %Y') 
print(parsed_date)

# formatea de objeto a string, para que se vea más bonito
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)