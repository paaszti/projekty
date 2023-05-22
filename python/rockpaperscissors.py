rps={'rock':1, 'paper':2, 'scissors':3}
print("Type 'paper' 'rock' 'scissors'")
player1=str(input("Player 1: "))
player2=str(input("Player 2: "))
choice_1=int((rps[player1]))
choice_2=int((rps[player2]))
sum=choice_2+choice_1
while True:##pętla wykonuje się w nieskończoność
    if choice_2==choice_1:
        print("It's draw")
        break
    if sum==3:
        print("Paper win")
        break
    elif sum==4:
        print("Rock win")
        break
    elif sum==5:
        print("Scissors win")
        break