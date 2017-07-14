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
    def move(position, goal):
