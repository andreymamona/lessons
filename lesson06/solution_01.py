# Напишите программу, которая принимает текст и выводит два слова: наиболее часто
# встречающееся и самое длинное, в идеале не использовать библиотечные функции.

text_sample = ('Дана база данных (в виде текстового файла) о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой запись вида Покупатель, Товар, Количество, Стоимость,где Покупатель - имя покупателя (строка без пробелов), товар - название товара (строка без пробелов), количество - количество приобретенных единиц товара. a. Создайте список и выведите на экран всех покупателей, а для каждого покупателя подсчитайте общее количество приобретенных им товаров и их стоимость. b. Создайте список и выведите на экран все товары, а для каждого товара подсчитайте общее количество приобретенных и их стоимость. ')

text_sample = text_sample.casefold()
new_text = str()
word = str()
longest_word = [None, 0]
quantity_of_using = {}
most_used_word = [0, 0]
for l in range(len(text_sample)):
    if text_sample[l].isalpha() or text_sample[l] == ' ':
        word += text_sample[l]
        word_len = int(len(word) - 1)
        if text_sample[l] == ' ':
            word = word[0:-1]
            if word_len > int(longest_word[1]):
                longest_word = [word, word_len]
            if word not in quantity_of_using.keys():
                quantity_of_using[word] = 1
            else:
                quantity_of_using[word] = quantity_of_using[word] + 1
            #print(f'{key} {value}' for key, value in quantity_of_using.items())
            #print(longest_word)
            #print(word)
            #print(word_len)
            word = str()
            word_len = 0

for key, value in quantity_of_using.items():
    if int(quantity_of_using[key]) > most_used_word[1]:
        most_used_word = key, value

print(f'Самое длинное слово: {longest_word}')
print(f'Самое частое слово: {most_used_word}')
#print(new_text)
