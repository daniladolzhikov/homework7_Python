def count_vowels(word):
    vowels = "аеёиоуыэюя"
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count


def check_rhythm(poem):
    phrases = poem.split()
    vowel_counts = [count_vowels(phrase.replace('-', '')) for phrase in phrases]

    if all(count == vowel_counts[0] for count in vowel_counts):
        return "Парам пам-пам"
    else:
        return "Пам парам"
