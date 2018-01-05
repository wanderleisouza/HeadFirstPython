vowels = {'a', 'e', 'i', 'o', 'u'}
word = input("type a word:").lower()
counter = {}

for c in word:
    if c in vowels:
        counter.setdefault(c, 0)
        counter[c] = counter[c] + 1

for k, v in sorted(counter.items()):
    print(k, 'was found', v, 'time(s)')
