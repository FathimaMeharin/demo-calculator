def count_vowel(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in text:
        if char in vowels:
            count = count+1
            print(count)
    return count
name=("meharin")
count_vowel(name)

