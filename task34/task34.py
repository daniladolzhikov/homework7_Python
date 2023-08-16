# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их 
# придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число 
# слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может 
# состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы 
# отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с 
# клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке
# *Пример:*

#     **Ввод:**  пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

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


poem_input = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem_input)
print(result)