import pygame
import random
import sys
import time

class RockPaperScissorsGame:
    def __init__(self):
        # Inicializar Pygame
        pygame.init()

        # Definir colores
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)

        # Definir dimensiones de la ventana
        self.WIDTH, self.HEIGHT = 800, 600

        # Inicializar la ventana
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Rock, Paper, Scissors Game")

        # Cargar imágenes
        self.rock_image = pygame.image.load("rock.png")
        self.paper_image = pygame.image.load("paper.png")
        self.scissors_image = pygame.image.load("scissors.png")

        # Escalar imágenes para que se ajusten a la pantalla
        image_scale = 0.6
        self.rock_image = pygame.transform.scale(self.rock_image, (int(300 * image_scale), int(300 * image_scale)))
        self.paper_image = pygame.transform.scale(self.paper_image, (int(300 * image_scale), int(300 * image_scale)))
        self.scissors_image = pygame.transform.scale(self.scissors_image, (int(300 * image_scale), int(300 * image_scale)))

        # Crear botones
        button_width, button_height = 200, 100
        button_spacing = 20
        button_y = self.HEIGHT - button_height - 20
        self.rock_button = pygame.Rect(self.WIDTH // 2 - button_width - button_spacing, button_y, button_width, button_height)
        self.paper_button = pygame.Rect(self.WIDTH // 2, button_y, button_width, button_height)
        self.scissors_button = pygame.Rect(self.WIDTH // 2 + button_width + button_spacing, button_y, button_width, button_height)

        # Definir opciones del juego
        self.OPTIONS = ["Rock", "Paper", "Scissors"]

        # Inicializar puntuaciones y resultado del juego
        self.player_score = 0
        self.computer_score = 0
        self.game_result = None

        # Elecciones de los jugadores
        self.player_choice = None
        self.computer_choice = None

        # Tiempo para cerrar la ventana después de que finalice el juego (en segundos)
        self.closing_time = 3

    def display_choices(self):
        if self.player_choice:
            self.screen.blit(getattr(self, f"{self.player_choice.lower()}_image", None), (self.WIDTH // 4, self.HEIGHT // 4))
        if self.computer_choice:
            self.screen.blit(getattr(self, f"{self.computer_choice.lower()}_image", None), (self.WIDTH // 2, self.HEIGHT // 4))

    def display_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Player Score: {self.player_score} | Computer Score: {self.computer_score}", True, self.WHITE)
        self.screen.blit(text, (self.WIDTH // 4, 20))

    def display_last_play(self):
        if self.player_choice and self.computer_choice:
            font = pygame.font.Font(None, 36)
            text = font.render(f"You chose {self.player_choice} | Computer chose {self.computer_choice}", True, self.WHITE)
            self.screen.blit(text, (self.WIDTH // 4, 80))

    def display_result(self):
        if self.game_result:
            font = pygame.font.Font(None, 48)
            color = self.RED
            text = font.render(self.game_result, True, color)
            self.screen.blit(text, (self.WIDTH // 4, self.HEIGHT // 2))

    def run_game(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if self.rock_button.collidepoint(mouse_pos):
                        self.player_choice = "Rock"
                    elif self.paper_button.collidepoint(mouse_pos):
                        self.player_choice = "Paper"
                    elif self.scissors_button.collidepoint(mouse_pos):
                        self.player_choice = "Scissors"
                    else:
                        continue

                    # El jugador hace clic para elegir
                    self.computer_choice = random.choice(self.OPTIONS)

                    # Determinar el ganador y actualizar puntajes
                    self.update_score()

                    # Comprobar si el juego ha terminado
                    if self.player_score == 3 or self.computer_score == 3:
                        self.game_result = "You win!" if self.player_score == 3 else "Computer wins!"
                        print(self.game_result)

                        # Esperar un tiempo y cerrar la ventana
                        time.sleep(self.closing_time)
                        pygame.quit()
                        sys.exit()

                    # Actualizar la pantalla
                    self.screen.fill(self.BLACK)
                    self.display_choices()
                    self.display_score()
                    self.display_last_play()
                    self.display_result()
                    pygame.display.flip()

            # Dibujar botones
            pygame.draw.rect(self.screen, self.WHITE, self.rock_button)
            pygame.draw.rect(self.screen, self.WHITE, self.paper_button)
            pygame.draw.rect(self.screen, self.WHITE, self.scissors_button)

            # Mostrar texto en botones
            self.display_button_text("Rock", self.rock_button)
            self.display_button_text("Paper", self.paper_button)
            self.display_button_text("Scissors", self.scissors_button)

            pygame.display.flip()
            clock.tick(60)

    def display_button_text(self, text, button_rect):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, self.BLACK)
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.screen.blit(text_surface, text_rect)

    def update_score(self):
        if self.player_choice == self.computer_choice:
            print("It's a tie!")
        elif (self.player_choice == "Rock" and self.computer_choice == "Scissors") or \
             (self.player_choice == "Paper" and self.computer_choice == "Rock") or \
             (self.player_choice == "Scissors" and self.computer_choice == "Paper"):
            print("You win!")
            self.player_score += 1
        else:
            print("Computer wins!")
            self.computer_score += 1

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.run_game()
