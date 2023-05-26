import random


class Bola:
    def __init__(self, canvas, Barra, color, score_callback, game_over_cb):
        self.canvas = canvas
        self.Barra = Barra
        self.id = self.canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)
        self.count = 0
        self.score_callback = score_callback
        self.game_over_cb = game_over_cb

        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3

        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)

        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                self.count += 1
                self.score_callback()


        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            self.game_over_cb()
            self.lost = True
