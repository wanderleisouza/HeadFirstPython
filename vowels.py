vowels = ['a', 'e', 'i', 'o', 'u']
data = input("digite a palavra:").lower()
found = []

for i in data:
    if i in vowels:
        found.append(i)

print(len(found), "vogais encontradas", found)