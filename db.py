import numpy as np
class database:
    def __init__(self,filepath):
        self.DB = np.loadtxt("./" + filepath, dtype = str)
    
    @property
    def title(self):
        return self.DB[:,0]
    @property
    def authors(self):
        return self.DB[:,1]
    @property
    def published(self):
        return self.DB[:,2]
    @property
    def publisher(self):
        return self.DB[:,3]
    @property
    def genre(self):
        return self.DB[:,4]

    


