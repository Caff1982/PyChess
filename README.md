# PyChess

A chess game written in Python with AI. Uses mini-max algorithm with alpha-beta pruning to get best move. Can play as human vs human or human vs AI.

## Prerequisites and Installing

Requires Python 3 and pygame to run. 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pygame.

```bash
pip install pygame
```

After installing the prerequisites and cloning this repo the  program can then be run using:

```bash
python main.py
```
## Description

The default search depth for the AI is 3 (Medium difficulty). This can be adjusted on the start menu although increasing the search depth will take longer to get the best move. The game can be played against AI or human using the start menu to select.

The AI uses a mini-max algorithm to search for the best move. It also uses alpha-beta pruning to get the optimal move quicker. 

For the evaluation function the AI uses piece values and also piece-tables. This improves the performance and also makes the AI play more 'human'.

## Todo

En passant, stalemate, 50 move rule.

## Contributing
Any Issues or Pull Requests are always welcome. 

## License
[MIT](https://choosealicense.com/licenses/mit/)