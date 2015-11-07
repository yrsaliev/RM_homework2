## -*- coding: utf-8 -*-

string = "Написать. программу+ поиска. самого-короткого слова? который, " \
         "выделяется/ знаком> который<             пользователь; вводит: в= интерактивном; режиме"

print string #for testing purpose

list = " ".join(string.split()) #removes all extra whitespaces

list = list.split(' ') #creates list of words, separated by whitespace

symbol = raw_input("Введите символ разделяющий слово: ")
length = 100
shortest = ""
new_list = []

if symbol == " ":
    for word in list:  #searches for shortest word

        if len(word) < length:
            shortest =word

else:

    for word in list: #searches for all words, that end with inputed symbol and adds them to new list

        if word.endswith(symbol):
            new_list.append(word)




    for word in new_list:  #searches for shortest word
        if len(word) < length:
            shortest =word[:-1] #slices the word so that last symbol is deleted

print shortest #prints out shortest word minus last character (symbol that a word separated with)
