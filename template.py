numbers = int(raw_input())

total_test_cases = 1

while numbers != 0:

    count = 0
    animals = {}
    animals_seen = []
    count_animals = []
    while count < numbers:
        animal = raw_input()

        if len(animal) < 6:
            animal = animal.lower()
        else:
            animal = animal.split()
            animal = animal[len(animal)-1].lower()

        if animal not in animals_seen:
            animals[animal] = 1
            animals_seen.append(animal)
        else:
            animals[animal] +=1

        count += 1

    final_answer = []
    for animal,count in animals.iteritems():
        test = [animal,count]
        final_answer.append(test)

    print("List " + str(total_test_cases) + ":")
    for animal in sorted(final_answer):
        print(animal[0] + " " + "| " + str(animal[1]))
    numbers = int(raw_input())
    total_test_cases+=1
