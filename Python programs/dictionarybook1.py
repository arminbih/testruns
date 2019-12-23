birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# Program will keep asking for a name then show the birthday for that name.
while True:
    print ('Enter a name (blank to quit)')
    name = input()
    if name == '':
        break
# If name is not in birthdays program asks for a birthday for that name to add to birthdays
# Press enter to return to input of name    
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?(Enter to change name)')
        bday = input()
        if bday == '':
            continue
        birthdays[name] = bday
        print('Birthday database updated.')
    


        


        