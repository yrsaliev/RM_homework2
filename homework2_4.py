## -*- coding: utf-8 -*-

print "Написать программу которое находит введенное слово в строке которое также вводится"\
"пользователем в интерактивном режиме"

string = raw_input("Введите предложение:")

list = " ".join(string.split()) #removes all extra whitespaces

list = list.split(' ') #creates list of words, separated by whitespace

search_word = raw_input("Введите слово для поиска:")

word_count = 0

for word in list:

    if search_word == word:
        word_count +=1

if word_count>0:
    print "Слово найдено, количество совпадений:", word_count

else:
    print "Совпадений не найдено"