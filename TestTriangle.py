# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest
implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of
# the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        """
        Test ID: 1
        Input: (3, 4, 5)
        Expected Results: 'Right'
        Actual Result: classifyTriangle(3,4,5)

        """
        self.assertEqual(
            classifyTriangle(3, 4, 5), "Right", "3,4,5 is a Right triangle"
        )

    def testRightTriangleB(self):
        """
        Test ID: 2
        Input: (5, 3, 4)
        Expected Results: 'Right'
        Actual Result: classifyTriangle(5,3,4)

        """
        self.assertEqual(
            classifyTriangle(5, 3, 4), "Right", "5,3,4 is a Right triangle"
        )

    def testEquilateralTriangles(self):
        """
        Test ID: 3
        Input: (1, 1, 1)
        Expected Results: 'Equilateral'
        Actual Result: classifyTriangle(1,1,1)

        """
        self.assertEqual(
            classifyTriangle(1, 1, 1),
            "Equilateral",
            "1,1,1 should be equilateral",
        )

    def testIsoscelesTriangleA(self):
        """
        Test ID: 4a
        Input: (5, 5, 3)
        Expected Results: 'Isoceles'
        Actual Result: classifyTriangle(5,5,3)

        """
        self.assertEqual(
            classifyTriangle(5, 5, 3), "Isoceles", "5,5,3 should be isosceles"
        )

    def testIsoscelesTriangleB(self):
        """
        Test ID: 4b
        Input: (3, 5, 5)
        Expected Results: 'Isoceles'
        Actual Result: classifyTriangle(3,5,5)

        """
        self.assertEqual(
            classifyTriangle(3, 5, 5), "Isoceles", "3,5,5 should be isosceles"
        )

    def testIsoscelesTriangleC(self):
        """
        Test ID: 4c
        Input: (5, 3, 5)
        Expected Results: 'Isoceles'
        Actual Result: classifyTriangle(5,3,5)

        """
        self.assertEqual(
            classifyTriangle(5, 3, 5), "Isoceles", "5,3,5 should be isosceles"
        )

    def testScaleneTriangleA(self):
        """
        Test ID: 5a
        Input: (4, 2, 3)
        Expected Results: 'Scalene'
        Actual Result: classifyTriangle(4,2,3)

        """
        self.assertEqual(
            classifyTriangle(4, 2, 3), "Scalene", "4,2,3 should be scalene"
        )

    def testScaleneTriangleB(self):
        """
        Test ID: 5b
        Input: (6, 7, 8)
        Expected Results: 'Scalene'
        Actual Result: classifyTriangle(6,7,8)

        """
        self.assertEqual(
            classifyTriangle(6, 7, 8), "Scalene", "6,7,8 should be scalene"
        )

    def testInvalidInputA(self):
        """
        Test ID: 6a
        Input: (-1, 2, 3)
        Expected Results: 'InvalidInput'
        Actual Result: classifyTriangle(-1,2,3)

        """
        self.assertEqual(
            classifyTriangle(-1, 2, 3),
            "InvalidInput",
            "Negative side should be invalid",
        )

    def testInvalidInputB(self):
        """
        Test ID: 6b
        Input: (0, 2, 3)
        Expected Results: 'InvalidInput'
        Actual Result: classifyTriangle(0,2,3)

        """
        self.assertEqual(
            classifyTriangle(0, 2, 3),
            "InvalidInput",
            "Zero side should be invalid",
        )

    def testInvalidInputC(self):
        """
        Test ID: 6c
        Input: (201, 2, 3)
        Expected Results: 'InvalidInput'
        Actual Result: classifyTriangle(201,2,3)

        """
        self.assertEqual(
            classifyTriangle(201, 2, 3),
            "InvalidInput",
            "Side > 200 should be invalid",
        )

    def testInvalidInputD(self):
        """
        Test ID: 6d
        Input: (2.5, 2, 2)
        Expected Results: 'InvalidInput'
        Actual Result: classifyTriangle(2.5,2,2)

        """
        self.assertEqual(
            classifyTriangle(2.5, 2, 2),
            "InvalidInput",
            "Non-integer side should be invalid",
        )

    def testInvalidInputE(self):
        """
        Test ID: 6e
        Input: ('a', 2, 2)
        Expected Results: 'InvalidInput'
        Actual Result: classifyTriangle('a',2,2)

        """
        self.assertEqual(
            classifyTriangle("a", 2, 2),
            "InvalidInput",
            "Non-integer side should be invalid",
        )

    def testNotATriangleA(self):
        """
        Test ID: 7a
        Input: (1, 2, 3)
        Expected Results: 'NotATriangle'
        Actual Result: classifyTriangle(1,2,3)

        """
        self.assertEqual(
            classifyTriangle(1, 2, 3),
            "NotATriangle",
            "1,2,3 cannot form a triangle",
        )

    def testNotATriangleB(self):
        """
        Test ID: 7b
        Input: (10, 1, 1)
        Expected Results: 'NotATriangle'
        Actual Result: classifyTriangle(10,1,1)

        """
        self.assertEqual(
            classifyTriangle(10, 1, 1),
            "NotATriangle",
            "10,1,1 cannot form a triangle",
        )

    def testNotATriangleC(self):
        """
        Test ID: 7c
        Input: (1, 10, 1)
        Expected Results: 'NotATriangle'
        Actual Result: classifyTriangle(1,10,1)

        """
        self.assertEqual(
            classifyTriangle(1, 10, 1),
            "NotATriangle",
            "1,10,1 cannot form a triangle",
        )

    def testNotATriangleD(self):
        """
        Test ID: 7d
        Input: (1, 1, 10)
        Expected Results: 'NotATriangle'
        Actual Result: classifyTriangle(1,1,10)

        """
        self.assertEqual(
            classifyTriangle(1, 1, 10),
            "NotATriangle",
            "1,1,10 cannot form a triangle",
        )

    def testEdgeCaseEquilateral(self):
        """
        Test ID: 8a
        Input: (200, 200, 200)
        Expected Results: 'Equilateral'
        Actual Result: classifyTriangle(200,200,200)

        """
        self.assertEqual(
            classifyTriangle(200, 200, 200),
            "Equilateral",
            "200,200,200 should be equilateral",
        )

    def testEdgeCaseIsosceles(self):
        """
        Test ID: 8b
        Input: (200, 199, 199)
        Expected Results: 'Isoceles'
        Actual Result: classifyTriangle(200,199,199)

        """
        self.assertEqual(
            classifyTriangle(200, 199, 199),
            "Isoceles",
            "200,199,199 should be isosceles",
        )


if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()
