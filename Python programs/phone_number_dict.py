phone = input("Phone: ")
diggits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    #"9": "nine"
}
output = ""
for ch in phone:
    output += diggits_mapping.get(ch, ",only up to number 9!") + " "
print (output)