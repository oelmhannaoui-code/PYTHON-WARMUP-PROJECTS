# DICE BATTLE ``

import random

player_hp = 100
enemy_hp = 100



def welcome():
    print("Welcome to DICE vs!")
    print("ROLL DICE or KISS the MICE!")

def play_game():
        global player_hp,enemy_hp
        input('press enter to roll... ')
        attack = random.randint(1, 6)
        cpu_attack = random.randint(1, 6)
        if attack > cpu_attack:
         damage = attack - cpu_attack
         enemy_hp -= damage
         print(f'You rolled {attack} !')
         print(f'Enemy rolled {cpu_attack} !')
         print(f'You Landed {damage} damage!')
         print('__________________')
         print(f'YOUR HP: {player_hp}')
         print(f'ENEMY HP: {enemy_hp}')
        elif cpu_attack > attack:
         damage = cpu_attack - attack
         player_hp -= damage
         print(f'You rolled {attack} !')
         print(f'Enemy rolled {cpu_attack} !')
         print(f'Enemy landed {damage} damage!')
         print('__________________')
         print(f'YOUR HP : {player_hp}')
         print(f'ENEMY HP : {enemy_hp}')
        else :
         print('DRAW !')


welcome()

while player_hp > 0  and enemy_hp > 0:
    play_game()

if player_hp <= 0 and enemy_hp <=0:
    print("NO WAY!  DRAW :S ")

elif player_hp <=0:
    print("YOU LOSE")

else:
    print("YOU WIN!")
