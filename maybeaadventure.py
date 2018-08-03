print("Welcome to your story! Along the story, you will be presented with choices that will decide you fate! Your ultimate goal is to return home! Decide wisely! Let's begin!")
print("You find yourself in a dark room with 2 doors. The first door presents you with the future, the second is the past!")
door_choice=input("Which door do you want to choose? 1=Door 1 or 2=Door 2 ")
if door_choice=="1":
  print("Great, you are in the future! You meet a scientist that gives you a mission of helping him save the world!")
  choice_one=input("What do you want to do? 1=Accept or 2=Decline")
  if choice_one=="1":
    print("""___________SUCCESS____________
    You helped the scientist to save the world! In gratitude, the scientist builds a time machine and sends you home!""")
  else:
    print("""___________GAME OVER_______________
    Too bad! You declined the scientist's offer and now you are stuck in the future!""")
else:
  print("Great, you are in the past! You are now the general of the Canadian Army! Canada is at war with the United States! If you win the war, you will be given a chance to go back home!")
  war_choice=input("Do you want to invade the United States, or do you want to stay and protect Canada? 1=Invade or 2=Protect")
  if war_choice=="1":
    print("""___________GAME OVER_______________
    The American army is too large! You are killed along with your army!""")
  else:
    print("""___________SUCCESS____________
    Great! You protected Canada and defeated the United States! You find a time machine and go back home! """)
