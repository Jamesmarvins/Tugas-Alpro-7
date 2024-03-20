def is_anagram(word1, word2):
    return sorted(word1.lower().replace(" ", "")) == sorted(word2.lower().replace(" ", ""))

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if is_anagram(kata1, kata2):
    print(f"{kata1} dan {kata2} adalah anagram.")
else:
    print(f"{kata1} dan {kata2} bukan anagram.")