
class Barra:
    def __init__(self, canvas, color, length):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)
        self.x = 0
        self.pos = self.canvas.coords(self.id)
        self.lost = False
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-a>", self.move_left)
        self.canvas.bind_all("<KeyPress-d>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0

        if self.pos[2] >= self.canvas_width:
            self.x = 0

        if self.lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3

