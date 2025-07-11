import random
import time
 
operators=['+',"-","*","/"]
max_operand=12
min_operand=3
total_problem=4

def generate_problem():
    left=random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    operator=random.choice(operators)

    expr=exp = f"{left} {operator} {right}"


    answer=eval(expr)
    return exp,answer
worng=0
input("press to start")
print("----------------------")
start_time=time.time()
for i in range(total_problem):
    expr,answer=generate_problem()
    while True:
        guess=input("user enter your answer for problem :"+ str(i+1) +":"+ expr + "=")
        if guess==str(answer):
            break
        elif guess.lower() == "exit":
                print("Exiting the quiz. Goodbye!")
                exit()
        else:
            worng+=1
print("-----------------------")
end_time=time.time()
total_time=round(end_time - start_time,2)
print("nice work man",total_time,"second")
print("mistake made",worng)