from draw_functions import *
from point_set import PointSet
from random_point_generator import cluster4_point
import draw_functions
from parameters import *

root = Tk()
can = Canvas(root, width=WIN_SIZE, height=WIN_SIZE)
can.pack()

if __name__ == "__main__":
    ps = PointSet()
    centroids = []
    cluster_set = [0]*NB_CLUSTER

    for i in range(0, NB_POINTS):
        point = cluster4_point()
        can.draw_point(point)
    #     ps.append(point)
    #     if i < 4:
    #         centroids.append(point)
    #
    # for pt in ps:
    #     ps.assign_centroid(centroids)

    mainloop()