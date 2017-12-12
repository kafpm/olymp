from itertools import permutations

vowels = ['А', 'О', 'И', 'Е', 'Ё', 'Э', 'Ы', 'У', 'Ю', 'Я']
consonants = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
in_word = ['С', 'А', 'Т', 'У', 'Р', 'Н']

count = 0
for permutation in permutations(in_word):
    out_word = [symbol for symbol in permutation if symbol in vowels]
    flag = (sorted(out_word) == out_word)
    if flag:
        count += 1

print(count)