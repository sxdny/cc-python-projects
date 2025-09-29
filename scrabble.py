letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
          3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

players_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': [
    'EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}


def score_word(word):
    point_total = 0
    for letter in word:
        letter = letter.upper()
        point_total += letter_to_points.get(letter, 0)
    return point_total

def play_word(player, word):
    players_to_words[player].append(word.upper())
    updated_list = update_point_totals()
    print(updated_list)


letter_to_points = {letter: point for letter, point in zip(letters, points)}

letter_to_points[" "] = 0

#print(letter_to_points)

brownie_points = score_word("Brownie")
#print(brownie_points)

def update_point_totals() -> dict:
    players_to_points = {}
    
    for player, words in players_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        players_to_points[player] = player_points

    return players_to_points

play_word('player1', 'car')
play_word('player1', 'HOTEL')
