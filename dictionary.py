#people = {
#'Matthew': '16',
#'Cate': '11',
#'Bea': '15',
#'Helena': '16'
#}
#print(people)


collection = []

while True:
    survey = {
    'name': input("What is your name?"),
    'age': input("How old are you"),
    'location': input("Where are you from?"),
    'animal': input("What is your spirit animal"),
    'edit': input("Would you like to edit your answers? This will delete all answers")
    }

    print(survey['name'])
    print(survey['age'])
    print(survey['location'])
    print(survey['animal'])
    print(survey['edit'])
    collection.append(survey)
    if survey['edit'] == 'yes':
        answer = False
    if survey['edit'] == 'no':
        continue
    print(collection)
    continue

rocket = open("allanswers.json", "r")
olddata = json.load(rocket)
list_of_answers.extend(olddata)
rocket.close()

rocket = open("allanswers.json", "w")
rocket.write('[\n')

index = 0
for i in list_of_answers:
    if(index < len(list_of_answers)-1):
        json.dump(i, rocket)
        rocket.write(',\n')
    else:
        json.dump(i, rocket)
        rocket.write('\n')
        index = index + 1

rocket.write(']')
rocket.close()
