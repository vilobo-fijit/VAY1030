massage = input("write something: ")
vowels = "AEYUIOaeyuio"
consonants = "QWRTPSDFGHJKLZXCVBNMqwrtpsdfghjklzxcvbnm"
vowels_count = 0
consonants_count = 0
for char in massage:
    if char in vowels:
        vowels_count += 1
    elif char in consonants:
        consonants_count += 1
print(f"vowels - {vowels_count}\nconsonants - {consonants_count}")

