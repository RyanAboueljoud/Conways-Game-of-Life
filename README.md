# Conway's Game of Life
Python Implementation of John Conways "Game of Life"

### Rules of the Game:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

### Usage:
* First, install requirements using: `pip install -r requirements.txt`
* Game can be started with custom parameters using command line arguments
* Valid arguments include:

  -h: Help <br />
  -s: Set manual seed <br />
  -x: Set gameboard width <br />
  -y: set gamboard height <br />
  -c: Set grid cell size <br />
  
### References:
* https://beltoforion.de/en/game_of_life/
* https://beltoforion.de/en/recreational_mathematics/game_of_life.php
* https://github.com/beltoforion/recreational_mathematics_with_python
* https://www.pygame.org/docs/
* https://www.geeksforgeeks.org/command-line-arguments-in-python/
* https://github.com/dwyl/english-words
