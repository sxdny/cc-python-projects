# Testing file ;)

def contains(big_string, little_string) -> bool:
  if little_string in big_string:
    return True
  else:
    return False


def common_letters(string_one, string_two) -> list:
  list_common = []
  for char in string_one:
    if char in string_two and not char in list_common:
      list_common.append(char)
  return list_common
