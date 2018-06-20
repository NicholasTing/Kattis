import itertools

# word = raw_input()

    # word = set(list(word))
    # print(word)
count = 7
answer = 0
final = 1

while answer < count:
    final += count * final
    answer += 1

print(final)
# for i in itertools.permutations(word):
#     count += 1
#
# print(count)
