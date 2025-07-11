print("welcome to my computer quiz!")
playing=input("do you want to play?")
if(playing.lower()=="yes"):
    print("okay! lets play:")
    score=0
else:
    quit()

answer=input("what cpu is stand for?:")
if(answer.lower()=="centeral processing unit"):
    print("correct")
    score=score+1
else:
    print("incorrect")

answer=input("what does gpu stand for?:")
if(answer.lower()=="grapical processing unit"):
    print("correct")
    score+=1
else:
    print("incorrect")
answer=input("whhat does ram stand for?:")
if(answer.lower()=="random access memory"):
    print("correct")
    score+=1
else:
    print("incorrect")
answer=input("what does ai stand for")
if(answer.lower()=="artificial intelligence:"):
    print("correct")
    score+=1
else:
    print("incorrect")

print("you got"+str(score)+"question correct")
print("you got"+str((score/4)*100)+" % correct")
    

