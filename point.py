from math import *
import sys


class Point:
    # Constructor
    def __init__(self, x, y, color="#000000"):
        self.x = x          # x the abscissa of the point
        self.y = y          # y the ordinate of the point
        self.color = color  # color the color of the point, black by default


    # Methods
    """
    Add this point to the closest centroid of clusters within the list in parameter
    :param cluster_list list of PointSet with defined centroid
    :return res the cluster it has been associated with
    """
    def assign_cluster(self, cluster_list):
        min_dist = sys.maxsize
        res = None

        # Search for closest centroid
        for cluster in cluster_list:
            # Calculate distance
            dist = self.euclidian_distance(cluster.centroid)
            # Is tested one closest?
            if dist < min_dist:
                min_dist = dist
                res = cluster
        # Add point to found cluster
        res.append(self)
        return res

    """
    Calculate the distance between current point and another
    :param point the point to calculate distance between
    """
    def euclidian_distance(self, point):
        x = self.x-point.x
        y = self.y-point.y
        return sqrt(pow(x, 2) + pow(y, 2))
