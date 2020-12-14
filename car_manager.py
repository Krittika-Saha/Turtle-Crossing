import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]



class CarManager:
  def __init__(self):
    self.all_cars = []
    self.STARTING_MOVE_DISTANCE = 5
    self.MOVE_INCREMENT = 10
    
  def create_car(self):
    random_chance = random.randint(1, 6)
    if random_chance == 1:
      new_car = Turtle('square')
      new_car.shapesize(1,2)
      new_car.up()
      new_car.color(random.choice(COLORS))
      random_y = random.randint(-230, 230)
      new_car.goto(300, random_y)
      self.all_cars.append(new_car)

  def move_cars(self):
    for car in self.all_cars:
      car.backward(self.STARTING_MOVE_DISTANCE)

  def increment_move(self):
    self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT