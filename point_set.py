

class PointSet(list):
    def __init__(self):
        self.centroid = None

    def get_centroid(self):
        return self.centroid

    def set_centroid(self, cent):
        self.centroid = cent


