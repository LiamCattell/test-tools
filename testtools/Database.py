import numpy as np
import matplotlib.pyplot as plt

class Database:
    def __init__(self):
        self.myvar = np.random.rand(5,5)
        return
    
    def add(self, x):
        return self.myvar + x
    
    def plot(self):
        plt.matshow(self.myvar)
        plt.show()
        return