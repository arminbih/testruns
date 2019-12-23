customer = {
    "name":"john smith",
    "age": "30",
    "is verified": True
}
customer ["birthdate"] = "jan.28.1991" # adds to dictionary
#print (customer["Name"])

print (customer.get("birthdate")) #no error when key does not exist

picnicItems = {'apples': 5, 'cups': 2}
print (f"I am bringing {picnicItems.get('cups')} cups ")
picnicItems.setdefault('fruit', 'grapes')
print (picnicItems)

