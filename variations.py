#!/usr/bin/env python

message = input("Enter a message: ")
print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Capitalized:", message.capitalize())
print("Title case:", message.title())

words = message.split()
print("Words:", words)
sorted_words = sorted(words)
print("Alphabetic first word:", sorted_words[0])
print("Alphabetic last word:", sorted_words[-1])