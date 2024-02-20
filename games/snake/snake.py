# games/snake/snake_pygame.py
import pygame
import sys
import random

class SnakeGame:
    def __init__(self):
        pygame.init()

        self.width, self.height = 400, 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = (1, 0)  # Initial direction: right
        self.food_position = self.generate_food()

        self.run_game()

    def generate_food(self):
        x = random.randint(1, 19) * 20
        y = random.randint(1, 19) * 20
        return x, y

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (*segment, 20, 20))

    def draw_food(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (*self.food_position, 20, 20))

    def move_snake(self):
        head = self.snake[0]
        new_head = (head[0] + self.direction[0] * 20, head[1] + self.direction[1] * 20)
        self.snake = [new_head] + self.snake[:-1]

    def check_collision(self):
        head = self.snake[0]
        if head in self.snake[1:]:
            self.game_over()

        if not (0 <= head[0] <= self.width - 20 and 0 <= head[1] <= self.height - 20):
            self.game_over()

    def check_food_collision(self):
        head = self.snake[0]
        if head == self.food_position:
            self.snake.append(self.snake[-1])
            self.food_position = self.generate_food()

    def game_over(self):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 30)
        text = font.render('Game Over', True, (255, 255, 255))
        self.screen.blit(text, (self.width // 2 - 100, self.height // 2 - 15))
        pygame.display.flip()

        pygame.time.wait(2000)  # Wait for 2 seconds before exiting
        pygame.quit()
        sys.exit()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.direction != (0, 1):
                self.direction = (0, -1)
            elif keys[pygame.K_DOWN] and self.direction != (0, -1):
                self.direction = (0, 1)
            elif keys[pygame.K_LEFT] and self.direction != (1, 0):
                self.direction = (-1, 0)
            elif keys[pygame.K_RIGHT] and self.direction != (-1, 0):
                self.direction = (1, 0)

            self.move_snake()
            self.check_collision()
            self.check_food_collision()

            self.screen.fill((0, 0, 0))
            self.draw_snake()
            self.draw_food()

            pygame.display.flip()
            self.clock.tick(10)  # Adjust the speed of the game
