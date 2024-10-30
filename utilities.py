from sklearn.neighbors import KDTree
import json
import numpy as np
    
class PersonalityComparison:
    def __init__(self, scores):
        self.scores = scores
        self.data = json.load(open("scores.json"))

        # make scores an array
        X = np.array([list(self.data[i].values()) for i in self.data.keys()])
        self.tree = KDTree(X)

    def find_nearest_neighbors(self, query):
        query = np.array([query])
        distances, indices = self.tree.query(query, k=1)
        if indices[0][0] == 0:
            return "You are most similar to Kenny"
        elif indices[0][0] == 1:
            return "You are most similar to Ruben"
        else:
            return "You are most similar to Will"