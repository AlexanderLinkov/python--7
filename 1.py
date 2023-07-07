d = ['а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я']
s = list(input("Введите строку: ").split(' '))

def count_alpha(n):
    count = 0
    for i in n:
        if i in d:
            count += 1
    return count

z = set()
for j in range(len(s)):
    z.add(count_alpha(s[j]))

if len(z) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')