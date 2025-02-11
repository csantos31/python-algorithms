
from random import randint
from time import sleep
from enum import Enum

options = ['PEDRA', 'PAPEL', 'TESOURA']
user_victories = 0
machine_victories = 0
tie = 0

class Players(Enum):
    MACHINE="MAQUINA"
    USER="USER"

    @classmethod
    def showWinnerMessage(self, player):
        print(f'{player.value} VENCEU !!!')

def main():
    while True:
        show_menu()
        user_input = input()
        clear_terminal()
        if not user_input.isdigit() or int(user_input) not in [0, 1, 2]:
            end_game()
            break
        else:
            machine_move = randint(0,2)
            show_animation()
            
            process_move(machine_move, int(user_input))


def show_menu():
    print(
''' 
*********************************************************
************************ MENU ***************************
*                                                       *
*   OPÇÕES                                              *
*   0 - JOGAR PEDRA                                     *
*   1 - JOGAR PAPEL                                     *
*   2 - JOGAR TESOURA                                   *
*   Outro - SAIR                                *
 *                                                     *
  *****************************************************
''')

def end_game():
    print(
''' 
*********************************************************
*               OBRIGADA POR PARTICIPAR                 *
 *                       bye bye                       *
  *****************************************************
''')
    sleep(2)
    clear_terminal()

def show_animation():
    print(f'\t\033[32mJO\033[m')
    sleep(0.5)
    print(f'\t\t\033[30mKEN\033[m')
    sleep(0.5)
    print(f'\t\t\t\033[31mPO\033[m')
    sleep(0.5)
    
def clear_terminal():
    print(chr(27) + "[2J")

def process_move(machine_move, user_move):
    print(f'MÁQUINA JOGA -> {options[machine_move]}')
    print(f'E USER JOGA -> {options[user_move]}')

    if(options[machine_move] == options[user_move]):
        global tie
        tie += 1
    else:
        if(machine_move == 0 and user_move == 1 ): #máquina escolheu PEDRA e user escolheu PAPEL
            set_victory(Players.USER)
        elif(machine_move == 0 and user_move == 2 ): #máquina escolheu PEDRA e user escolheu TESOURA
            set_victory(Players.MACHINE)
        elif(machine_move == 1 and user_move == 0 ): #máquina escolheu PAPEL e user escolheu PEDRA
            set_victory(Players.MACHINE)
        elif(machine_move == 1 and user_move == 2 ): #máquina escolheu PAPEL e user escolheu TESOURA
            set_victory(Players.USER)
        elif(machine_move == 2 and user_move == 0 ): #máquina escolheu TESOURA e user escolheu PEDRA
            set_victory(Players.USER)
        elif(machine_move == 2 and user_move == 1 ): #máquina escolheu TESOURA e user escolheu PAPEL
            set_victory(Players.MACHINE)

    print(f'''
*************************************************
*                STATUS DO GAME                 *
    VITORIAS DA MAQUINA: {machine_victories}
    VITORIAS DO USER: {user_victories}
    EMPATES: {tie}
 *                                             *
  *********************************************
''', end='')

def set_victory(winner):
    if(winner == Players.USER):
        global user_victories 
        user_victories += 1
        Players.showWinnerMessage(Players.USER)
    elif (winner == Players.MACHINE):
        global machine_victories
        machine_victories += 1
        Players.showWinnerMessage(Players.MACHINE)


main()