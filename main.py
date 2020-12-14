import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

screen.listen()
screen.onkey(player.move_up, 'Up')

car_manager = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    
    #Detect when player has collided with car
    for car_detector in car_manager.all_cars:
      if player.distance(car_detector) < 20:
        game_is_on = False

    #Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).
    if player.FINISH_LINE_Y == player.ycor():
      player.reached_finish_line()
      car_manager.increment_move()

screen.exitonclick()