numbers = [5,2,5,2,2]
for x_count in numbers:
    print ('x'*x_count)
    
#these 2 are the same outputs

for x_count in numbers:
    output =''
    for count in range(x_count):
        output+='x'
    print (output)