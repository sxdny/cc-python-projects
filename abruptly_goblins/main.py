def add_gamer(gamer: dict, gamers_list: list):
    if ('name' in gamer.keys() and 'availability' in gamer.keys()):
        gamers_list.append(gamer)


def build_daily_frequency_table() -> dict:
    return {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}


def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day_available in gamer["availability"]:
            available_frequency[day_available] += 1
            

def find_best_night(availability_table):
    best_night_value = max(availability_table.values())
    for day, value in availability_table.items():
        if best_night_value == value:
            return day


def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(
            f"Hello, {gamer}! Today {day} you can play your favourite game: {game}!")


def available_on_night(gamers_list, day) -> list:
    list = []
    for gamer in gamers_list:
        if day in gamer["availability"]:
            list.append(gamer["name"])
    return list

gamers = []

kimberly = {'name': 'Kimberly Jones', 'availability': ['Tuesday', 'Saturday']}
add_gamer(kimberly, gamers)

# notebook.p11
add_gamer({'name': 'Thomas Nelson', 'availability': [
          "Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joyce Sellers', 'availability': [
          "Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'Michelle Reyes', 'availability': [
          "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Stephen Adams', 'availability': [
          "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': [
          "Monday", "Thursday"]}, gamers)
add_gamer({'name': 'Latasha Bryan', 'availability': [
          "Monday", "Sunday"]}, gamers)
add_gamer({'name': 'Crystal Brewer', 'availability': [
          "Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'James Barnes Jr.', 'availability': [
          "Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Michel Trujillo', 'availability': [
          "Monday", "Tuesday", "Wednesday"]}, gamers)

print(gamers)

count_availability = build_daily_frequency_table()
print(count_availability)

calculate_availability(gamers, count_availability)
print(count_availability)

game_night = find_best_night(count_availability)
print(game_night)

attending_game_night = available_on_night(gamers, "Thursday")
print(attending_game_night)

send_email(attending_game_night, game_night, "Abruptly Goblins")

unable_to_attend_best_night = []

for gamer in gamers:
    if not gamer["name"] in attending_game_night:
        unable_to_attend_best_night.append(gamer)

print(unable_to_attend_best_night)

second_night_availability = build_daily_frequency_table()

calculate_availability(unable_to_attend_best_night, second_night_availability)
print(second_night_availability)

second_night = find_best_night(second_night_availability)
print(second_night)

available_second_game_night = available_on_night(gamers, second_night)
print(available_second_game_night)

send_email(available_second_game_night, second_night, "Abruptly Goblins")

