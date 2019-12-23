numbers = [1,2,4,6,8,10,20,100,88,1983,193884,182,8585,182,20,1,2,4,1000]
maxN= numbers[0]
for l_number in numbers:
    if l_number > maxN:
        maxN = l_number
print (maxN) 

print (max(numbers))   #same

uniques = []
for duplicate in numbers:
    if duplicate not in uniques:
        uniques.append(duplicate)
print (uniques)
        
