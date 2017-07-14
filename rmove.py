# Moves robot from position to goal through shortest path at constant speed

import math


class RbtMove:
    def path(position, goal, speed=50):  # speed [pixel/frame]
        if(position == goal):
            dx = 0
            dy = 0
            t = 1
            return (dx, dy, t)
        else:
            x = goal[0]-position[0]
            y = goal[1]-position[1]
            dist = math.sqrt(pow(x, 2)+pow(y, 2))
            t = dist/speed
            dx = speed*x/dist
            dy = speed*y/dist
            return (dx, dy, t)

    def move(position, dx, dy):
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position
