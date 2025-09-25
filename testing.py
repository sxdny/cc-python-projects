# Testing file ;)

# from datetime import datetime

# # Hora en formato de 24 horas
# hora_24 = 15

# # Convertir a formato de 12 horas
# hora_12 = datetime.strptime(f"{hora_24}", "%H").strftime('%-I%p')

# print(hora_12)  # Salida: 03 PM

items = {'pancakes': 7.50, 'waffles': 5.50, 'burguer': 11.00}

for key, value in items.items():
    print(key, value)



def calculate_total(purchased_items):
    items_eq = [value for key, value in items.items() if key in purchased_items]
    print(sum(items_eq))
        

calculate_total(['waffles', 'pancakes'])
