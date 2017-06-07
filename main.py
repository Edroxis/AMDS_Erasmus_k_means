from tkinter import *
from point_set import PointSet
from random_point_generator import cluster4_point
import draw_functions
from centroid_k_mean import k_mean
from parameters import *

root = Tk()
can = Canvas(root, width=WIN_SIZE, height=WIN_SIZE)
can.pack()

if __name__ == "__main__":
    # Declare point set and add point in it
    ps = PointSet()
    for i in range(0, NB_POINTS):
        point = cluster4_point()
        ps.append(point)

    # Call K_Mean algorithm
    cluster_set = k_mean(ps, NB_CLUSTER)

    # Draw points
    for point in ps:
        can.draw_point(point)

    # Draw Clusters centroids
    for cluster in cluster_set:
        can.draw_point(cluster.centroid)

    mainloop()