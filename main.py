from tkinter import *
from point_set import PointSet
from random_point_generator import cluster4_point
from draw_functions import draw_point
from centroid_k_mean import k_mean
from parameters import *

if __name__ == "__main__":
    """
    Number of points generated, window size and number of cluster can be modified in parameter file
    """

    # Declare point set and add point in it
    ps = PointSet()
    for i in range(0, NB_POINTS):
        point = cluster4_point()
        ps.append(point)

    # Call K_Mean algorithm
    cluster_set = k_mean(ps, NB_CLUSTER)

    # Draw points (in black)
    for point in ps:
        draw_point(point)

    # Draw Clusters centroids (in red)
    for cluster in cluster_set:
        draw_point(cluster.centroid)

    mainloop()
