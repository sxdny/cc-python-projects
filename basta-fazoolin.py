from datetime import datetime


def int_to_hour_12(int):
    return datetime.strptime(
        str(int), "%H").strftime('%-I%p')


def hour_12_to_int(str):
    return datetime.strptime(str, "%I%p").hour

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return (f"Address: {self.address}")

    def available_menus(self, time):
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                print(menu)


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        start_time_formatted = int_to_hour_12(self.start_time)
        end_time_formatted = int_to_hour_12(self.end_time)

        return f"{self.name} menu available from {start_time_formatted} to {end_time_formatted}"

    # 1 panckake, 1 home fries, 1 coffe
    def calculate_bill(self, purchased_items):
        items_to_sum = [value for key,
                        value in self.items.items() if key in purchased_items]
        print(f"Total of the bill: ${sum(items_to_sum)}")


brunch_menu_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_menu_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner_menu_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids_menu_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

arepas_menu_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}



brunch = Menu("Brunch", brunch_menu_items, 11, 16)
early_bird = Menu("Early Bird", early_bird_menu_items, 15, 18)
dinner = Menu("Dinner", dinner_menu_items, 17, 23)
kids = Menu("Kids Menu", kids_menu_items, 11, 21)
arepas_menu = Menu("Arepas Menu", arepas_menu_items, 10, 20)

flagship_store = Franchise('1232 West End Road', [
                           brunch, early_bird, dinner, kids])
new_installment = Franchise('12 East Mulberry Street', [
                            brunch, early_bird, dinner, kids])
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

print(brunch)
brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
print(early_bird)
early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])

flagship_store.available_menus(22)

basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
take_a_arepa = Business("Take a' Arepa", [arepas_place])
