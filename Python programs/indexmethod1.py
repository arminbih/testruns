
# Methods are when you put "." after data type.
spam = ['one', 'two', 'three', 'four' ]
spam.append('plolo')
print (spam.index('plolo'))
print (spam)

spam.insert (1, "koki")
print (spam.index ("koki"))
print (spam)

spam.remove ('one')
print (spam)

spam.sort ()
print (spam)

spam.sort (reverse = True)
print (spam)

spam.insert (2, "Rooki")
spam.sort ()
print (spam)

spam.sort(key=str.lower)
print (spam)

spem = list("And" "I" "would" "walk" "one" "hundred" "miles" "and")
print (spem)
