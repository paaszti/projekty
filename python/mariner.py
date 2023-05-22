print("Let's start a Mariner the game! ")
amount_players = int(input("How many of players: "))
users_answers_dict = {}
for i in range(int(amount_players)):
    name = str(input("Name: "))
    number = int(input("Give me a number: "))
    users_answers_dict.update({name: number})
sum_of_numbers = sum(users_answers_dict.values())
rest = (sum_of_numbers%amount_players)
list = []
for i in users_answers_dict.keys():
    list.append(i)
print(f"Player {list[rest]} won in the mariner game!")