
print ("Welcome to My Quiz")

score=0


play = input ("Do you want to play? \n")
if play != "yes":
    quit()

answer = input("1. What does RAM stands for? ")
if answer.lower() == "random access memory":
    print ("correct!")
    score+= 1
else:
    print ( "incorrect")

answer = input("2. Who is the first president of the Philippines? ")
if answer.upper() == "EMILIO AGUINALDO":
    print ("correct!")
    score+= 1
else:
    print ( "incorrect")

answer = input("3. Who is the first president of the Philippines? ")
if answer.lower() == "Emilio Aguinaldo":
    print ("correct!")
    score+= 1
else:
    print ( "incorrect")


answer = input("4. Who killed Magellan? ")
if answer.lower() == "Lapu-Lapu":
    print ("correct!")
    score+= 1
else:
    print ( "incorrect")


answer = input("5. Who is the founder of KKK? ")
if answer.lower() == "Andres Bonifacio":
    print ("correct!")
    score+= 1
else:
    print ( "incorrect")



print ("Total Score = " + str(score))