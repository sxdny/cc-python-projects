# some improvements would be ok but it's just a simple project
import random

name = "Sidney"
question = ""
answer = ""

random_number = random.randint(1,9) # inclusive 1 and 9

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

# Check if the user provided a question
if question == "":
  print("You need to provide a question...")
else:
  # Check if name is not empty
  if name == "":
    print("Question: " + question)
  else:
    print(name + " asks " + question)
  print("Magic 8-Ball's answer: " +  answer)
