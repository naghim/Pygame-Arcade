import pygame

class GameOfLife(object):
    FPS = 20
    WIDTH = 800
    HEIGHT = 600
    OUTLINE_COLOR = (100, 100, 100)
    OUTLINE_THICKNESS = 1
    BACKGROUND_COLOR = (25, 25, 25)
    CELL_SIZE = 10
    ROW_COUNT = 60
    COL_COUNT = 80
    WHITE = (235, 235, 235)

    def __init__(self):
        pygame.init()

        self.CELLS = [[0 for _ in range(self.ROW_COUNT)] for _ in range(self.COL_COUNT)]
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Game of Life")

        self.run()
    
    def draw_grid(self):
        for row in range(self.ROW_COUNT):
            y = row * self.CELL_SIZE
            pygame.draw.line(self.window, self.OUTLINE_COLOR, (0, y), (self.WIDTH, y), self.OUTLINE_THICKNESS)

            for col in range(self.COL_COUNT):
                x = col * self.CELL_SIZE
                pygame.draw.line(self.window, self.OUTLINE_COLOR, (x, 0), (x, self.HEIGHT), self.OUTLINE_THICKNESS)

    def update(self):
        for row in range(self.ROW_COUNT):
            for col in range(self.COL_COUNT):
                if self.CELLS[col][row] == 1:
                    pygame.draw.rect(self.window, self.WHITE, (col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))

        self.draw_grid()

    def count_neighbors(self, row, col):
        neighbors = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue

                if 0 <= col + i < self.COL_COUNT and 0 <= row + j < self.ROW_COUNT:
                    neighbors += self.CELLS[col + i][row + j]
        
        return neighbors

    def evolve(self):
        new_cells = [[0 for _ in range(self.ROW_COUNT)] for _ in range(self.COL_COUNT)]

        for row in range(self.ROW_COUNT):
            for col in range(self.COL_COUNT):
                neighbors = self.count_neighbors(row, col)
                new_cell = neighbors == 3 or (self.CELLS[col][row] == 1 and neighbors == 2)
                new_cells[col][row] = 1 if new_cell else 0

        self.CELLS = new_cells
        self.update()

    def run(self):
        clock = pygame.time.Clock()
        self.window.fill(self.BACKGROUND_COLOR)

        run = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    run = not run
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    run = False
                    self.window.fill(self.BACKGROUND_COLOR)
                    self.draw_grid()
                    pygame.display.update()
                    self.CELLS = [[0 for _ in range(self.ROW_COUNT)] for _ in range(self.COL_COUNT)]

                if pygame.mouse.get_pressed()[0]:
                    run = False
                    x, y = pygame.mouse.get_pos()
                    x //= 10
                    y //= 10
                    self.CELLS[x][y] = 1
                    self.update()
                    pygame.display.update()
                    
            if run:
                self.window.fill(self.BACKGROUND_COLOR)
                self.evolve()
                pygame.display.update()

            pygame.display.update()
            clock.tick(self.FPS)

if __name__ == "__main__":
    gol = GameOfLife()
