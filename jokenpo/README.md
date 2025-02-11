# Rock, Paper, Scissors Game

This repository contains a Python implementation of the classic "Rock, Paper, Scissors" game, allowing the user to play against the computer. The game continues until the user decides to exit.

## Description

The script allows the user to choose between Rock, Paper, or Scissors, and the computer generates a random move. The game determines the winner, keeps track of victories, ties, and displays the current status after each round.

## Code Structure

- **main()**: The entry point of the game loop, handles menu display and user interaction.
- **Players(Enum)**: Enum to differentiate between user and machine players.
- **show_menu()**: Displays the game menu.
- **end_game()**: Prints the exit message and clears the terminal.
- **show_animation()**: Displays a "Jo-Ken-Po" animation.
- **clear_terminal()**: Clears the terminal screen.
- **process_move(machine_move, user_move)**: Determines the outcome of a round and updates the game status.
- **set_victory(winner)**: Updates the victory count and shows the winner message.

## Game Options

```bash
*********************************************************
************************ MENU ***************************
*                                                       *
*   OPÇÕES                                              *
*   0 - JOGAR PEDRA                                     *
*   1 - JOGAR PAPEL                                     *
*   2 - JOGAR TESOURA                                   *
*   Outro - SAIR                                        *
 *                                                     *
  *****************************************************
```

## Expected Output

The output varies based on the moves chosen by the player and the machine. A typical round could look like this:

```bash
MÁQUINA JOGA -> PAPEL
E USER JOGA -> TESOURA
USER VENCEU !!!
*************************************************
*                STATUS DO GAME                 *
    VITORIAS DA MAQUINA: 0
    VITORIAS DO USER: 1
    EMPATES: 0
 *                                             *
  *********************************************
```

## How to Run

1. Ensure you have [Python](https://www.python.org/downloads/) installed.
2. Clone this repository:
   ```bash
   git clone <REPOSITORY_URL>
   cd <REPOSITORY_FOLDER>
   ```
3. Run the script:
   ```bash
   python3 rock_paper_scissors.py
   ```

## Possible Future Improvements
- Enhance animations and user feedback.
- Implement a graphical interface for a better user experience.
- Include support for more game variations.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request with suggestions for improvements.

