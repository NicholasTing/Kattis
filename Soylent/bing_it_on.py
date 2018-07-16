total_cases = int(input())

dict_of_words = {}

while total_cases != 0:
    word = input()
    checked = 0
    for i in range(len(word)):

        if not checked:
            if word in dict_of_words.keys():
                print(dict_of_words[word[:i+1]])

            else:
                print(0)

            checked = 1

        if word[:i+1] not in dict_of_words:

            dict_of_words[word[:i+1]] = 1
        else:
            dict_of_words[word[:i+1]] += 1



    total_cases -= 1
