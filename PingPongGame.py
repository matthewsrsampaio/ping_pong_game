from tkinter import *
import time

from PIL import Image, ImageTk

from Barra import Barra
from Bola import Bola


class PingPongGame:

    def __init__(self):
        self.root = Tk()
        self.root.title("Star Pong")
        self.root.resizable(0, 0)
        self.root.wm_attributes("-topmost", 1)
        self.root.iconbitmap("image/icone.ico")

        self.canvas = Canvas(self.root, width=800, height=600, bd=0, highlightthickness=0)
        self.canvas.pack()

        back_img_path = "image/nv3.jpg"
        bg_image = Image.open(back_img_path)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.canvas.create_image(0, 0, image=self.bg_photo, anchor=NW)

        self.level_label = Label(self.root, text="Qual nível você gostaria de jogar? 1/2/3/4/5", font=("Arial", 20))
        self.level_label.pack()
        self.level_entry = Entry(self.root, font=("Arial", 20))
        self.level_entry.pack()
        self.submit_button = Button(self.root, text="PLAY", font=("Arial", 20, " bold"), command=self.set_level)
        self.submit_button.pack()
        self.submit_button.bind("<Return>", self.set_level)

        self.count = 0
        self.lost = False

    def set_level(self, event=None):
        self.level = int(self.level_entry.get())
        self.length = 500 / self.level
        self.level_label.destroy()
        self.level_entry.destroy()
        self.submit_button.destroy()
        self.init_game()

    def reset_score(self):
        self.count = 0
        self.canvas.itemconfig(self.score_now, text=self.score_now_text)

    def score_now(self):
        score_now_text = "    HITS: " + str(self.count) + "x"
        score_now_colour = "cyan"
        score_now_font = "Arial", 25, "bold"
        self.score_now_text = score_now_text

        self.score_now = self.canvas.create_text(  # chama so no começo
            370, 20, text=score_now_text, fill=score_now_colour, font=score_now_font, anchor=CENTER
        )

    def score(self):
        self.count += 1
        score_text = "   HITS: " + str(self.count) + "x"
        self.canvas.itemconfig(self.score_now, text=score_text)  # chama durante o jogo

    def init_game(self): #Primeira função iniciada

        self.barra = Barra(self.canvas, "cyan", self.length)
        self.bola = Bola(self.canvas, self.barra, "olive", self.score, self.game_over)

        self.score_now()
        self.game = self.canvas.create_text(400, 300, text=" ", fill="black", font=("Arial", 40)) #Se tirar essa linha o cod quebra
        self.start_game()

    def start_game(self, event=None):
        self.count = 0 #esse cara aqui ta zerando a contagem
        self.lost = False
        self.canvas.itemconfig(self.game, text="")
        time.sleep(1)
        self.barra.draw()
        self.bola.draw()

    def quit_game(self, event=None):
        self.root.quit()

    def game_over(self):
        button_font = "Arial", 20, "bold"
        youdied_style_text = "YOU DIED"
        youdied_style_font = "Arial", 100, "bold"
        youdied_style_colour = "red"
        button_restart_text = "PLAY AGAIN"
        button_restart_x = 300
        button_restart_y = 400
        button_quit_text = "QUIT"
        button_quit_x = 350
        button_quit_y = 500
        return_ = "<Return>"

        self.canvas.itemconfig(self.game, text=youdied_style_text, fill=youdied_style_colour, font=youdied_style_font, anchor=CENTER)

        def restart_game():
            self.restart_button.destroy()  # Destroi o botão
            self.quit_button.destroy()
            self.start_game()  # Reinicia o jogo
            self.reset_score() #reseta_score

        self.restart_button = Button(self.root, text=button_restart_text, font=button_font, command=restart_game)
        self.restart_button.place(x=button_restart_x, y=button_restart_y)
        self.restart_button.bind(return_, restart_game)

        self.quit_button = Button(self.root, text=button_quit_text, font=button_font, command=self.quit_game)
        self.quit_button.place(x=button_quit_x, y=button_quit_y)
        self.quit_button.bind(return_, self.quit_game)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = PingPongGame()
    game.run()
