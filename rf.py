# Custom Reward Functions
import math


class rf:
    def avoid(robot_position, human_position, object_positions):
        reward = -pow(math.sqrt(robot_position[0]-human_position[0]), 2) \
            - pow(math.sqrt(robot_position[1]-human_position[1]), 2)
        return reward

    def sort(robot_position, human_position, object_positions):
        reward = 0
        return reward

    def copy(agent_position, human_position, object_positions):
        reward = -abs(agent_position[0]-human_position[0]) \
            - abs(agent_position[1]-human_position[1])
        return reward
