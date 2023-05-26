# from tkinter import CENTER
#
# from Barra import Barra
# from Bola import Bola
#
# class Score:
#
#     def reset_score(self):
#         self.count = 0
#         self.canvas.itemconfig(self.score_now, text=self.score_now_text)
#
#     def score_now(self):
#         score_now_text = "    HITS: " + str(self.count) + "x"
#         score_now_colour = "cyan"
#         score_now_font = "Arial", 25, "bold"
#         self.score_now_text = score_now_text
#
#         self.score_now = self.canvas.create_text(  # chama so no começo
#             370, 20, text=score_now_text, fill=score_now_colour, font=score_now_font, anchor=CENTER)
#
#     def score(self):
#         self.count += 1
#         score_text = "   HITS: " + str(self.count) + "x"
#         self.canvas.itemconfig(self.score_now, text=score_text)  # chama durante o jogo
#
#
