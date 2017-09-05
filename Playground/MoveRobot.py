<<<<<<< HEAD
=======
from objects import Robot


>>>>>>> fbd0af3803fe5f7d5e975dbd2f71ed02300487ea
class SimpleMove:
    def move(actor, action):
        if(action == 0):  # Up
            actor[1] = actor[1]+1
        if(action == 1):  # Down
            actor[1] = actor[1]-1
        if(action == 2):  # Left
            actor[0] = actor[0]-1
        if(action == 3):  # Right
            actor[0] = actor[0]+1
        return actor

class Sort:
<<<<<<< HEAD
    def move(position, goal):
=======
    def move(self, goal):  # Straight line between objects
>>>>>>> fbd0af3803fe5f7d5e975dbd2f71ed02300487ea
        return 0
