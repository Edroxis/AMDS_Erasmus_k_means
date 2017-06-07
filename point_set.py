from point import Point

"""
Inherit from list, made to store points in order to calculate centroid
"""


class PointSet(list):
    # Constructor
    def __init__(self, cent=None):
        self.centroid = cent

    # Getter and Setter
    def get_centroid(self):
        return self.centroid

    def set_centroid(self, cent):
        self.centroid = cent

    # Methods
    """
    Calculate the centroid of the point set with point in the list
    """
    def calc_centroid(self):
        x = 0
        y = 0
        # Sum coordinates of all points
        for pt in self:
            x += pt.x
            y += pt.y
        # Security if list is not empty
        if x != 0:
            x = x/len(self)
        if y != 0:
            y = y/len(self)

        # Define centroid
        self.centroid = Point(x, y, "#FF0000")
