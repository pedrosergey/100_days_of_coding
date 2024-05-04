# import some libraries

from prettytable import PrettyTable
from turtle import Turtle, Screen



# chofli = Turtle()
# view = Screen()


# chofli.tilt(45)
# chofli.color("chocolate4", "darkgreen")
# chofli.shape("turtle")
# chofli.turtlesize(3.0,3.0,2)
# chofli.forward(100)

# view.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Bulbasaur", "Squirtle", "Charmander"], "r")
table.add_column("Type", ["Grass", "Water", "Fire"], "r")
table.align = "l"

print(table)