
#Функция capwords () переводит в верхний регистр первую букву каждого слова в строке.

import string
s = 'The quick brown fox jumped over the lazy dog.'


print(s)
print(string.capwords(s))

#The Quick Brown Fox Jumped Over The Lazy Dog.


import string 
   
values = {'name':'Гор', 'firstname':'ооо', 'phd': 'Высшее'}
t = string.Template(""" 

Имя: $name
Фамилие : $firstname
Оброзование: ${phd} Образованние


"""
)
print(t.substitute(values))


#s = """
#Имя: %(name)
#Фамилие : %(firstname)
#Оброзование: %(phd) Образованние
#
#"""
#
#print(s % values)

s ="""
Имя: {name}
Фамилие : {firstname}
Оброзование: {phd} Образованние


"""
print(s.format(**values))



    
 
