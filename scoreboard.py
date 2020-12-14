from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
      super().__init__()
      self.up()
      self.goto(-230, 240)
      self.level = 1
      self.speed('fastest')
      self.hideturtle()
      self.write_level()

    def write_level(self):
      self.write(f"Level:{self.level}", align='center', font=FONT)

    def level_up(self):
      self.level += 1
      self.clear()
      self.write_level()

    def game_over(self):
      self.goto(0, 0)
      self.write(f"GAME OVER", align='center', font=FONT)
