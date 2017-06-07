from point_set import PointSet
from point import Point

"""
Find centroids of clusters with k_mean Algorithm
:param cluster_list list of PointSet with defined centroid
:nb_cluster number of cluster in the PointSet
"""
def k_mean(point_set, nb_cluster):
    cluster_set = [0]*nb_cluster

    # Put first points as center of centroids
    for i in range(0, nb_cluster):
        cluster_set[i] = PointSet(point_set[i])

    for i in range(0, 10):
        # Assign each point to closest cluster
        for pt in point_set:
            pt.assign_cluster(cluster_set)

        # Recalculate centroids for each clusters and clear its point list
        for cluster in cluster_set:
            cluster.calc_centroid()
            cluster.clear()

    return cluster_set
