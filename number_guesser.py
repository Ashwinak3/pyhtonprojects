import random
top_of_range=input("type a number:")
if(top_of_range.isdigit()):
    top_of_range=int(top_of_range)
    if(top_of_range<=0):
        print("please type a number larger than 0 next time")
        quit()
else:
    print("please type a number next time")
    quit()


random_number=random.randint(0,top_of_range)
#print(random_number)

guesses=0
while True:
    guesses+=1
    user_guess=input("make a guess")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please enter a number next time") 
        continue
    if user_guess==random_number:
        print('you goy it')
        break
    elif user_guess>random_number:
        print("you are above the number")
    

    else:
        print("you were below the number!")
print("you got it "+str(guesses)+"guesses")


