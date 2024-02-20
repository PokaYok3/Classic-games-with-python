import pygame
import sys
import random

class Minesweeper:
    def __init__(self, width, height, grid_size, mine_count):
        pygame.init()

        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.mine_count = mine_count
        self.cell_size = self.width // self.grid_size

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Buscaminas")

        self.font = pygame.font.Font(None, 36)

        self.reset()

    def reset(self):
        self.board = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.revealed_cells = [[False] * self.grid_size for _ in range(self.grid_size)]
        self.place_mines()
        self.game_over = False
        self.victory = False

    def place_mines(self):
        for _ in range(self.mine_count):
            row, col = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
            while self.board[row][col] == 1:
                row, col = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
            self.board[row][col] = 1

    def count_mines(self, row, col):
        count = 0
        for i in range(max(0, row - 1), min(self.grid_size, row + 2)):
            for j in range(max(0, col - 1), min(self.grid_size, col + 2)):
                count += self.board[i][j]
        return count

    def reveal_cells(self, row, col):
        if not (0 <= row < self.grid_size and 0 <= col < self.grid_size) or self.revealed_cells[row][col]:
            return

        self.revealed_cells[row][col] = True

        if self.board[row][col] == 1:
            print("¡Has perdido!")
            self.game_over = True
        elif self.count_mines(row, col) == 0:
            for i in range(max(0, row - 1), min(self.grid_size, row + 2)):
                for j in range(max(0, col - 1), min(self.grid_size, col + 2)):
                    self.reveal_cells(i, j)

    def check_win(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.board[row][col] == 0 and not self.revealed_cells[row][col]:
                    return False
        return True

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    x, y = event.pos
                    col = x // self.cell_size
                    row = y // self.cell_size

                    self.reveal_cells(row, col)

                    if self.board[row][col] == 1:
                        print("¡Has perdido!")
                        self.game_over = True
                    elif self.check_win():
                        print("¡Has ganado!")
                        self.game_over = True
                        self.victory = True

                if event.type == pygame.KEYDOWN and self.game_over:
                    if event.key == pygame.K_r:
                        self.reset()

            self.screen.fill((0, 0, 0))

            for row in range(self.grid_size):
                for col in range(self.grid_size):
                    rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                    if self.revealed_cells[row][col]:
                        pygame.draw.rect(self.screen, (150, 150, 150), rect)
                        if self.board[row][col] == 1:
                            pygame.draw.circle(self.screen, (255, 0, 0), rect.center, self.cell_size // 2)
                        elif self.count_mines(row, col) > 0:
                            color = (255, 255, 255)  # Color blanco para números de minas
                            text = self.font.render(str(self.count_mines(row, col)), True, color)
                            text_rect = text.get_rect(center=rect.center)
                            self.screen.blit(text, text_rect)
                    else:
                        pygame.draw.rect(self.screen, (192, 192, 192), rect, 1)

            if self.game_over:
                if self.victory:
                    text = self.font.render("¡Has ganado! Presiona 'R' para reiniciar.", True, (0, 255, 0))
                else:
                    text = self.font.render("¡Has perdido! Presiona 'R' para reiniciar.", True, (255, 0, 0))

                text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
                self.screen.blit(text, text_rect)

            pygame.display.flip()

if __name__ == "__main__":
    minesweeper = Minesweeper(400, 400, 10, 15)
    minesweeper.game_loop()
