import random

ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")

    answer = ["It is certain", "Outlook good", "You may rely on it", 
              "Ask again later", "Concentrate and ask again", "Reply hazy, try again", 
              "My reply is no", "My sources say no"]

    if question == "":
        ans = False
          
    else:
        print (answer[random.randint(0,7)])

