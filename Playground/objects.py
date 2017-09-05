import numpy as np


class Blocks:

    def create(numBlocks, numColors, numSizes, workspace):
        lst = []
        for i in range(0, numBlocks):
            lst.append(Blocks(numColors, numSizes, workspace, i))
        return lst

    def update_pos(self, new_position):
        self.pos = new_position
        return self

    def __init__(self, numColors, numSizes, workspace, ind):
        self.index = self.ind(ind)
        self.size = self.siz(numSizes)
        self.color = self.col(numColors)
        self.pos = (np.random.uniform(0, workspace[0]),
            np.random.uniform(0, workspace[1]))

    def ind(self, index):
        self.index = index
        return self.index

    def col(self, numColors):
        colors = np.random.randint(0, numColors)
        if(colors == 0):
            self.color = 'Red'
        elif(colors == 1):
            self.color = 'Green'
        elif(colors == 2):
            self.color = 'Blue'
        else:
            print('Error: Color Selection out of range')
            self.color = []
        return self.color


    def siz(self, numSizes):
        sizes = np.random.randint(0, numSizes)
        if(sizes == 0):
            self.size = 'Small'
        elif(sizes == 1):
            self.size = 'Large'
        elif(sizes == 2):
            self.size = 'Medium'
        else:
            print('Error: Size Selection out of range')
            self.size = []
        return self.size


class Robot:
    def __init__(self, workspace, position='rand'):
        if(position == 'rand'):
            self.pos = (np.random.uniform(0, workspace[0]),
                np.random.uniform(0, workspace[1]))
        elif(position == 'center'):
            self.pos = (workspace[0]/2, workspace[1]/2)


    def update_pos(self, new_position):
            self.pos = new_position
            return self
