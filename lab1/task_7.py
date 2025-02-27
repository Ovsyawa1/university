
from random import randint


## Задание №7 ##

def dice_game(players_count: int, players_names: list[str]):
    
    if players_count != len(players_names):
        raise Exception("You've inputted wrond data!")
    
    players_score = []
    
    for i in range(players_count):
        dice_value = randint(1, 6)
        players_score.append(dice_value)
        print(
            f"Игрок: {players_names[i]} \nВыбросил: {players_score[i]}\n"
        )
    
    max_dice_value = max(players_score)
    print("Победители:")
    
    for i in range(len(players_score)):
        if players_score[i] == max_dice_value:
            print(f"{players_names[i]}")
    
    
        
dice_game(5, ["Artem", "Oleg", "Vova", "Andrew", "Kirill"])