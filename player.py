from turtle import Turtle
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10



class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('turtle')
    self.left(90)
    self.up()
    self.speed('fastest')
    self.goto(STARTING_POSITION)
    self.FINISH_LINE_Y = 280

  def move_up(self):
    self.fd(20)

  def reached_finish_line(self):
    self.goto(STARTING_POSITION)
