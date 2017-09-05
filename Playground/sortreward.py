import numpy as np


class SortReward:
    def color(block, blocks, numBlocks):
        pos = []
        count = 0
        rwd = 0
        for i in range(0, numBlocks):
            if(blocks[i].color == block.color):
                pos = pos.append(blocks[i].pos, axis=0)
                count = count + 1
        for i in range(0, count):
            rwd = rwd - (abs(block.pos[0]-pos[0, i])/20
                + abs(block.pos[1]-pos[1, i])/20)
        return rwd


    def size(blocks, numBlocks):
