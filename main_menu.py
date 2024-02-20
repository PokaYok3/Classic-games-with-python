import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime

class PyClassicGamesApp:
    def __init__(self, master):
        self.master = master
        master.geometry("800x600")
        master.title("PyClassicGames")

        master.resizable(False, False)

        self.button_size = 30

        self.canvas = tk.Canvas(master, width=800, height=600)
        self.canvas.place(x=0, y=0)

        self.background_image = Image.open("fondo.png")
        self.background_image = self.background_image.resize((800, 600))
        self.background_image = ImageTk.PhotoImage(self.background_image)

        self.canvas.create_image(0, 0, image=self.background_image, anchor=tk.NW)

        self.button1 = tk.Button(master, text="Snake", command=self.start_snake_game, width=self.button_size, height=self.button_size // 3,
                                 bg="#FFD740", bd=1, relief="solid", font=("Helvetica", 12, "bold"),
                                 activebackground="#FFF000", activeforeground="black")
        self.button1.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

        self.button2 = tk.Button(master, text="Rock, Paper, Scissors",command=self.start_rock_paper_scissors_game, width=self.button_size, height=self.button_size // 3,
                                 bg="#00BFFF", bd=1, relief="solid", font=("Helvetica", 12, "bold"),
                                 activebackground="#87CEFF", activeforeground="black")
        self.button2.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

        self.button3 = tk.Button(master, text="Tic-Tac-Toe", command=self.start_tic_tac_toe_game, width=self.button_size, height=self.button_size // 3,
                                 bg="#8B0000", bd=1, relief="solid", font=("Helvetica", 12, "bold"),
                                 activebackground="#FFA07A", activeforeground="black")
        self.button3.place(relx=0.3, rely=0.8, anchor=tk.CENTER)

        self.button4 = tk.Button(master, text="Minesweeper", command=self.start_minesweeper_game, width=self.button_size, height=self.button_size // 3,
                                 bg="#FF8C00", bd=1, relief="solid", font=("Helvetica", 12, "bold"),
                                 activebackground="#FFB6C1", activeforeground="black")
        self.button4.place(relx=0.7, rely=0.8, anchor=tk.CENTER)

        self.title = tk.Label(master, text="PyClassicGames", font=("Helvetica", 36), bg="lightblue")
        self.title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.date_label = tk.Label(master, text="", font=("Helvetica", 12), bg="lightblue")
        self.date_label.place(relx=0.95, rely=0.05, anchor=tk.NE)

        self.update_date()

    def start_snake_game(self):
        import subprocess
        subprocess.run(["python", "games/snake/main.py"])

    def start_minesweeper_game(self):
        import subprocess
        subprocess.run(["python", "games/minesweeper/main.py"])

    def start_tic_tac_toe_game(self):
        import subprocess
        subprocess.run(["python", "games/tictactoe/main.py"])
    def start_rock_paper_scissors_game(self):
        import subprocess
        subprocess.run(["python", "games/rockpapersci/main.py"])

    def update_date(self):
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        self.date_label.config(text=formatted_date)
        self.master.after(1000, self.update_date)

def main():
    root = tk.Tk()
    app = PyClassicGamesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
