cat_names = []
while True:
    name = input(f"Enter the name of the cat {len(cat_names) + 1 } or enter to stop: ")
    if name == "":
        break
    
    #list concatenation
    cat_names += [name]
    
print ("The cat names are: ")
for name in cat_names:
    print (name)