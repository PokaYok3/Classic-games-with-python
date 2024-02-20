import pygame
import sys
import random

class TicTacToe:
    def __init__(self):
        # Inicializar Pygame
        pygame.init()

        # Configuración del juego
        self.WIDTH, self.HEIGHT = 300, 300
        self.LINE_COLOR = (255, 255, 255)
        self.TEXT_COLOR = (255, 0, 0)  # Cambiado a rojo
        self.BG_COLOR = (0, 0, 0)
        self.LINE_WIDTH = 15
        self.GRID_SIZE = 3
        self.CELL_SIZE = self.WIDTH // self.GRID_SIZE

        # Inicializar la pantalla
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")

        # Inicializar el tablero
        self.board = [['' for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]

        # Jugador actual
        self.current_player = 'X'

        # Historial de movimientos
        self.moves_history = []

        # Resultado del juego
        self.result = None

    def draw_grid(self):
        for i in range(1, self.GRID_SIZE):
            pygame.draw.line(self.screen, self.LINE_COLOR, (i * self.CELL_SIZE, 0), (i * self.CELL_SIZE, self.HEIGHT), self.LINE_WIDTH)
            pygame.draw.line(self.screen, self.LINE_COLOR, (0, i * self.CELL_SIZE), (self.WIDTH, i * self.CELL_SIZE), self.LINE_WIDTH)

    def draw_symbols(self):
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                if self.board[row][col] == 'X':
                    self.draw_x(col, row)
                elif self.board[row][col] == 'O':
                    self.draw_o(col, row)

    def draw_x(self, col, row):
        pygame.draw.line(self.screen, self.LINE_COLOR, (col * self.CELL_SIZE, row * self.CELL_SIZE),
                         ((col + 1) * self.CELL_SIZE, (row + 1) * self.CELL_SIZE), self.LINE_WIDTH)
        pygame.draw.line(self.screen, self.LINE_COLOR, ((col + 1) * self.CELL_SIZE, row * self.CELL_SIZE),
                         (col * self.CELL_SIZE, (row + 1) * self.CELL_SIZE), self.LINE_WIDTH)

    def draw_o(self, col, row):
        center = ((col + 0.5) * self.CELL_SIZE, (row + 0.5) * self.CELL_SIZE)
        radius = self.CELL_SIZE // 2 - self.LINE_WIDTH // 2
        pygame.draw.circle(self.screen, self.LINE_COLOR, center, radius, self.LINE_WIDTH)

    def draw_result(self):
        font = pygame.font.Font(None, 36)
        if self.result:
            text = font.render(self.result, True, self.TEXT_COLOR)
            text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
            self.screen.blit(text, text_rect)

    def make_move(self, row, col):
        if self.result:
            return  # No hacer movimientos si el juego ya ha terminado

        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.moves_history.append((row, col))

            # Verificar el resultado después de cada movimiento
            self.result = self.check_result()
            if self.result:
                pygame.time.delay(2000)  # Retraso de 2 segundos antes de cerrar el juego

            self.switch_player()

            # Después de que el jugador hace su movimiento, la máquina realiza su movimiento
            self.machine_move()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def machine_move(self):
        if self.result:
            return  # No hacer movimientos si el juego ya ha terminado

        available_moves = [(i, j) for i in range(self.GRID_SIZE) for j in range(self.GRID_SIZE) if self.board[i][j] == '']
        if available_moves:
            row, col = random.choice(available_moves)
            self.board[row][col] = 'O'
            self.moves_history.append((row, col))

            # Verificar el resultado después de cada movimiento
            self.result = self.check_result()
            if self.result:
                pygame.time.delay(2000)  # Retraso de 2 segundos antes de cerrar el juego

            self.switch_player()

    def check_winner(self):
        # Implementa tu lógica para verificar el ganador
        for i in range(self.GRID_SIZE):
            if all(self.board[i][j] == self.current_player for j in range(self.GRID_SIZE)) or \
               all(self.board[j][i] == self.current_player for j in range(self.GRID_SIZE)):
                return True

        if all(self.board[i][i] == self.current_player for i in range(self.GRID_SIZE)) or \
           all(self.board[i][self.GRID_SIZE - 1 - i] == self.current_player for i in range(self.GRID_SIZE)):
            return True

        return False

    def check_draw(self):
        return all(self.board[i][j] != '' for i in range(self.GRID_SIZE) for j in range(self.GRID_SIZE))

    def check_result(self):
        if self.check_winner():
            return f"¡{self.current_player} ha ganado!"
        elif self.check_draw():
            return "¡Empate!"
        return None

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    col = x // self.CELL_SIZE
                    row = y // self.CELL_SIZE
                    self.make_move(row, col)

            self.screen.fill(self.BG_COLOR)
            self.draw_grid()
            self.draw_symbols()
            self.draw_result()
            pygame.display.flip()

if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.run_game()
