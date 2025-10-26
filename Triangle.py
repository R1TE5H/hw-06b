# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to
classify triangles

@author: jrr
@author: rk
"""


def classifyTriangle(a, b, c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code
    passes all of you test cases.

    This function returns a string with the type of triangle from three
    integer values corresponding to the lengths of the three sides of the
    Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then
        return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    # First, check that all inputs are integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return "InvalidInput"

    # Check that all sides are in the valid range
    if a <= 0 or b <= 0 or c <= 0:
        return "InvalidInput"
    if a > 200 or b > 200 or c > 200:
        return "InvalidInput"

    # Check for triangle validity: sum of any two sides must be greater than
    # the third
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "NotATriangle"

    # Check for right triangle
    sides = sorted([a, b, c])
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return "Right"

    # Check for equilateral
    if a == b == c:
        return "Equilateral"

    # Check for isosceles
    if a == b or b == c or a == c:
        return "Isoceles"

    # Otherwise, scalene
    return "Scalene"
