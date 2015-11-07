## -*- coding: utf-8 -*-

string = "Написать программу поиска самого длинного слова в строке разделенной пробелами"
print string #for testing purpose
list = string.split(" ")

max=0

for word in list:

    if len(word)>max:
        max=len(word)
        longest_word = word

print longest_word