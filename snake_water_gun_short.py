import random
'''  
1 for snake 
2 for water
3 for gun

'''
computer = random.choice([1,0,-1])
you = input("enter your choice")
youDict ={"s":1,"w":0,"g":-1}
reverseDict ={1:"snake",0:"water",-1:"gun"}

younum = youDict[you]
print(f"you choose {reverseDict[younum]} and computer choose {reverseDict[computer]}")
if(computer==younum):
    print("draw")

elif((computer-younum)==-1 or (computer-younum==2)):
        print("you lose")
else:
    print("you won")        
# Short implementation of Snake–Water–Gun game
# Focuses on concise logic
