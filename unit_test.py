# -*- coding: utf-8 -*-

import unittest
from point import Point
from point_set import PointSet


class TestPoint(unittest.TestCase):
    def test_blank(self):
        self.assertEqual(True, True)

    def test_euclidian_distance(self):
        p1 = Point(0, 0)
        p2 = Point(0, 2)
        self.assertEqual(p1.euclidian_distance(p2), 2)

    def test_assign_cluster(self):
        ps1 = PointSet(Point(0, 0))
        ps2 = PointSet(Point(5, 5))
        cluster_list = [ps1, ps2]
        p1 = Point(1, 1)
        ps = p1.assign_cluster(cluster_list)
        self.assertEqual(ps, ps1)


class TestPointSet(unittest.TestCase):
    def test_blank(self):
        self.assertEqual(True, True)

    def test_calc_centroid(self):
        cluster = PointSet()
        cluster.append(Point(0, 0))
        cluster.append(Point(2, 0))
        cluster.append(Point(0, 2))
        cluster.append(Point(2, 2))
        cluster.calc_centroid()
        self.assertEqual(cluster.centroid.x, 1)
        self.assertEqual(cluster.centroid.y, 1)


if __name__ == '__main__':
    unittest.main()