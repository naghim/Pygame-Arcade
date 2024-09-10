# Pygame Arcade

Welcome to the Pygame Arcade! 🐍🎮 This repository is a collection of experimental Pygame projects and game prototypes, created as a way to explore game development concepts using the Pygame library. Each project builds on the skills learned in previous ones, gradually introducing more complex features, game mechanics, and visual effects.

I chose these projects as part of a self-guided learning curve in game development, gradually progressing from simpler concepts to more advanced techniques. Each project introduces new topics, and by tackling them step by step, I was able to build a solid foundation in game programming. If you're looking to follow a similar path, this collection of projects is a great starting point! Feel free to explore them in any order, depending on what you want to learn. Each project's _Learning focus_ segment will help you identify what concepts you can master, so you can easily switch between projects based on what interests you most.

Happy coding and learning! 🎉

## 👾 Projects

1. [**Game of Life**](GameOfLife)

   - This is an implementation of Conway's Game of Life, a cellular automaton where cells evolve based on simple rules. This project was a great introduction to understanding the core game loop and handling user inputs. Through this, I learned how to update the game state based on time (generations in Game of Life) and player interactions like pausing, clearing, and clicking.
   - Controls:
     - `Space`: Pause and resume the animation.
     - `Backspace`: Clear the canvas, removing all active cells.
     - `Left-click with mouse`: Draw active cells. If the simulation is running, it will pause when you click on the canvas.
   - Learning focus:
     - Basic game loop structure and timing.
     - Handling user inputs with keyboard and mouse events.
     - Drawing simple graphics and managing a grid-based system.

2. [**2048**](2048) - WIP

   - This project is a recreation of the popular sliding tile puzzle game 2048. While building this, I learned about working with fonts, displaying numbers, and reusing pre-rendered assets like tiles. I also explored the concept of separating the game logic (e.g., merging numbers, checking win conditions) from the rendering loop to ensure the game runs smoothly.
   - Controls:
     - `Arrow keys`: Move the tiles in the desired direction.
     - `Space`: Restart the game after a round.
   - Learning focus:
     - Implementing a smooth sliding effect for the tiles.
     - Using fonts for displaying numbers on tiles.
     - Reusing pre-rendered tiles for efficient rendering.
     - Separation of game logic and animation loop for better performance and maintainability.

3. [**Snake**](Snek) - WIP

   - This is a recreation of the classic Snake game, but with an added twist of cool explosion effects when the snake eats a fruit (...or rather a save point from Undertale ✨). Through this project, I learned about implementing particle effects and working with complex game objects (such as the segmented body of the snake). The snake's body segments and smooth movement posed new challenges in keeping track of object states and handling game-over scenarios.
   - Controls:
     - `Arrow keys`: Move the snake in the desired direction.
     - `Space`: Restart the game any time.
   - Learning focus:
     - Managing complex objects (like the snake's growing body), animations (sparkly food).
     - Adding particle effects (like explosions) for visual feedback.
     - Handling game-over states and smooth restarts.

## 🎯 Getting Started

Dependencies:

- Python 3.x
- Pygame

To run any of the projects, follow these steps:

**1. Clone the repository:**

```bash
git clone https://github.com/naghim/pygame-arcade.git
```

**2. Navigate to the project directory:**

```bash
cd pygame-arcade/project-name
```

**3. Install the required dependencies:**

```bash
pip install -r requirements.txt
```

**4. Run the game:**

```bash
python main.py
```
