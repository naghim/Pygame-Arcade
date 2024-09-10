import pygame
import random 
import math

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(2, 4)
        self.color = (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))
        self.lifetime = random.uniform(0.5, 1.5)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(50, 200)  # pixels per second
        self.vx = math.cos(self.angle) * self.speed
        self.vy = math.sin(self.angle) * self.speed

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.lifetime -= dt

    def draw(self, window):
        if self.lifetime > 0:
            print("Drawing particle on coordinates: ", self.x, self.y)
            pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)

class Explosion(object):
    def __init__(self, x, y, num_particles):
        self.particles = [Particle(x, y) for _ in range(num_particles)]

    def update(self, dt):
        for particle in self.particles:
            particle.update(dt)
        self.particles = [p for p in self.particles if p.lifetime > 0]

    def draw(self, window):
        for particle in self.particles:
            particle.draw(window)

class Food(object):
    def __init__(self, window, cell_size):
        self.window = window
        self.cell_size = cell_size
        
        self.color = (88, 230, 255)

        # To be safe
        self.x = 0
        self.y = 0
        
        self.radius_change = 0.5  # How much the radius changes each frame
        self.max_radius = 10  
        self.min_radius = 5 

        self.init_food()
    
    def init_food(self):
        self.radius = 8  

    def calculate_star_points(self, center_x, center_y, radius):
        points = []
        for i in range(8):
            angle = math.pi / 4 * i
            if i % 2 == 0:
                r = radius
            else:
                r = radius / 2.0
            x = center_x + r * math.cos(angle)
            y = center_y + r * math.sin(angle)
            points.append((x, y))
        return points

    def draw(self):
        print("Drawing food on coordiantes: ", self.x, self.y)

        points = self.calculate_star_points(self.y * self.cell_size + (self.cell_size/2 + 1), self.x * self.cell_size + (self.cell_size/2 + 1), self.radius)
        pygame.draw.polygon(self.window, self.color, points)

        #pygame.draw.circle(self.window, self.color, (self.y * self.cell_size + (self.cell_size/2 + 1) , self.x * self.cell_size + (self.cell_size/2 + 1)), self.radius)

    def update_pulse(self):
        self.radius += self.radius_change
        if self.radius >= self.max_radius or self.radius <= self.min_radius:
            self.radius_change = -self.radius_change
            
    def set_position(self, pos):
        self.x = pos[0]
        self.y = pos[1] 

    def get_position(self):
        return [self.x, self.y]

class Snek(object):
    FPS = 20
    WIDTH = 800
    HEIGHT = 800
    OUTLINE_COLOR = (100, 100, 100)
    OUTLINE_THICKNESS = 2
    BACKGROUND_COLOR = (25, 25, 25)
    CELL_SIZE = 25
    ROW_COUNT = 32
    COL_COUNT = 32
    WHITE = (235, 235, 235)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    direction = (0, 0)


    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snek")
        
        self.food = Food(self.window, self.CELL_SIZE)
        self.init_snek()

        self.run()
    
    def init_snek(self):
        self.SNEK = []
        
        self.explosions = []
        self.food.set_position(self.get_random_pos())
        self.snek_head = self.get_random_pos()
        self.direction = (0, 0)

        self.SNEK = [self.snek_head]
        
        self.food.draw()

        #pygame.draw.rect(self.window, self.WHITE, (self.food[1] * self.CELL_SIZE, self.food[0] * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
        pygame.draw.rect(self.window, self.WHITE, (self.snek_head[1] * self.CELL_SIZE, self.snek_head[0] * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
        pygame.display.update()

    def get_random_pos(self):
        while True:
            x = random.randint(0, self.ROW_COUNT - 1)
            y = random.randint(0, self.COL_COUNT - 1)
            
            if [x, y] not in self.SNEK:
                break   

        print(x, y)
        return [x, y]

    def draw_grid(self):
        for row in range(self.ROW_COUNT + 1):
            y = row * self.CELL_SIZE
            pygame.draw.line(self.window, self.OUTLINE_COLOR, (0, min(y, self.HEIGHT -  2)), (self.WIDTH, min(y, self.HEIGHT -  2)), self.OUTLINE_THICKNESS)

            for col in range(self.COL_COUNT + 1):
                x = col * self.CELL_SIZE
                pygame.draw.line(self.window, self.OUTLINE_COLOR, (min(x, self.WIDTH -  2), 0), (min(x, self.WIDTH - 2), self.HEIGHT), self.OUTLINE_THICKNESS)

    # Draw the snek
    def update(self):
        for index, body_part in enumerate(self.SNEK):
            color = self.WHITE if index % 2 else self.RED
            pygame.draw.rect(self.window, color, (body_part[1] * self.CELL_SIZE, body_part[0] * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))

        self.food.draw()
        #pygame.draw.rect(self.window, self.WHITE, (self.food[1] * self.CELL_SIZE, self.food[0] * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
        self.explosions = [explosion for explosion in self.explosions if explosion.particles]

        for explosion in self.explosions:
            explosion.draw(self.window)

        self.draw_grid()

    def update_snake(self):
        if self.snake_counter == 1:
            self.snake_counter = 0
        else:
            self.snake_counter += 1
            return

        add_tail = False

        # Check if the snek has collided with the food
        if self.SNEK[0] == self.food.get_position():
            print("Food eaten")
            add_tail = True

            # if food is eaten, explode it
            print("Exploding food")
            self.explosions.append(Explosion(self.food.y * self.CELL_SIZE + (self.CELL_SIZE/2 + 1), self.food.x * self.CELL_SIZE + (self.CELL_SIZE/2 + 1), 50))

            self.food.set_position(self.get_random_pos())
            self.food.init_food()
            self.food.draw()
            
        
        # Move the snek
        new_head = [self.SNEK[0][0] + self.direction[1], self.SNEK[0][1] + self.direction[0]]
        self.SNEK.insert(0, new_head)
        if not add_tail:
            self.SNEK.pop()
            
        # Check if the snek has collided with the wall
        if self.SNEK[0][0] < 0 or self.SNEK[0][0] >= self.ROW_COUNT or self.SNEK[0][1] < 0 or self.SNEK[0][1] >= self.COL_COUNT:
            self.wall_hit = True
            print("Game over // wall collision")
            return    

        # Check if the snek has collided with itself
        if self.SNEK[0] in self.SNEK[1:]:
            self.wall_hit = True
            return

    def next_frame(self):
        self.update_snake()            
        self.food.update_pulse()
        for explosion in self.explosions:
            explosion.update(self.dt) 
        self.update()
    
    def get_direction(self, event_key):
        if event_key == pygame.K_UP and self.direction != (0, 1):
            return (0, -1)
        elif event_key == pygame.K_DOWN and self.direction != (0, -1):
            return (0, 1)
        elif event_key == pygame.K_LEFT and self.direction != (1, 0):
            return (-1, 0)
        elif event_key == pygame.K_RIGHT and self.direction != (-1, 0):
            return (1, 0)

        return self.direction

    def run(self):
        clock = pygame.time.Clock()
        self.window.fill(self.BACKGROUND_COLOR)
        self.wall_hit = False
        self.dt = clock.tick(60) / 1000.0
        self.snake_counter = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                    self.direction = self.get_direction(event.key)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    print("Game over // space pressed")
                    self.init_snek()

            if self.wall_hit == True:
                print("Game over // wall collision // restarting")
                self.wall_hit = False
                self.init_snek()
                continue

            self.window.fill(self.BACKGROUND_COLOR)
            self.draw_grid()
            self.next_frame()
            pygame.display.update()

            clock.tick(self.FPS)


if __name__ == "__main__":
    snek = Snek()
