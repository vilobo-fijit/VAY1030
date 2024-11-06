massage = input("Give my sentence: ")
massage = massage.lower().replace(",","").replace(" ","") #A man, a plan, a canal, Panama
if massage == massage[::-1]:
    print("It is a polyndrome")
else:
    print("You are dolbaeb!")
