# --- Define your functions below! ---
def time():
     while True:
            answer = input("(How are you?)")
            if answer == "good":
                good()
            if answer == "bad":
                bad()
            else:
                print ("ok")
            break
def good():
    print("Yay!")
def bad():
    print("that sucks")

def question():
    while True:
        answer = input("(Do you like talking?)")
        print("I like talking. That is my only function in life")
        break

def yes():
    print("Yay! I'm not lonley anymore!")
def no():
    print("You don't want to be friends? Your loss.")

def friend():
    while True:
        answer = input("(Do you want to be friends?)")
        if answer == "yes":
            yes()
        if answer == "no":
            no()
        else:
            print("thats cool")
        break
def end():
    print(".....Thanks for a conversation! Bye!.....")

def jokeyes():
    print("What do mermaids wash their tails with?")
    jokeanswer()

def jokeno():
    print("You don't like jokes?")
def joke():
    answer = input("(Do you want to hear a joke?)")
    if answer == "yes":
        jokeyes()
    elif answer == "no":
        jokeno()
    else:
        jokeyes()


def jokeanswer():
    print("Tide")

def funnyyes():
    print("If some one says words can't physically hurt you then throw a dictionary at them.")

def funny():
    answer = input("(Do you want to here something funny?)")
    if answer == "yes":
        funnyyes()
    elif answer == "no":
        print("ok..... :(")
    else:
        funnyyes()





# --- Put your main program below! ---
def main():
    while True:
        print("Welcome to a chat with a bot!")
        answer = input("(Tell me a fun fact) ")
        print("That's cool!")
        time()
        question()
        friend()
        joke()
        funny()
        end()
        break
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()





# def say_hello(name):
#     print("Hi" + name)
#
# def main():
#     user = "Michelle"
#     say_hello(user)
#
# if _name_ == "_main_":
#     main()





#def add_five(number):
#    print (number + 5)

#def main():
#    add_five(5)


#main()
