from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "8")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        scoreboard.increase_score()
        player.go_to_start()
        cars.level_up()


screen.exitonclick()