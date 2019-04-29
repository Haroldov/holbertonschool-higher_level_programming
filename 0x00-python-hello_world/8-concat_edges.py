#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = "{0:s}{1:s}{2:s}".format(str[38:66], str[-23:-17], str[:6])
print(str)
