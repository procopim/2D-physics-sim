## @file TriangleT.py
#  @author Mark Procopio 400344315
#  @brief TriangleT Abstract Data Type module, using Shape interface.
#  @details Assumed that arguments provided will be correct type
#  @date Feb 13, 2021

from Shape import Shape

# @brief TriangleT ADT utilizing Shape interface

class TriangleT(Shape):
    # @brief constructor for class TriangleT; represents a Triangle shape in 2D space
    # @detail if any of r and m are less than 1, then we throw ValueError
    # @param x is x coordinate of center mass of Shape
    # @param y is y coordinate of center mass of Shape
    # @param s represents position of the shape body
    # @param m represents the mass of the shape
    def __init__(self, x, y, s, m):
        if (s > 0 and m > 0) is False:
            raise ValueError
        self.x = x
        self.y = y
        self.s = s
        self.m = m

    # @brief x centermass of TriangleT object
    # @return integer indicating x center of mass coordinate of TriangleT object
    def cm_x(self):
        return self.x

    # @brief y centermass of TriangleT object
    # @return integer indicating y center of mass coordinate TriangleT object
    def cm_y(self):
        return self.y

    # @brief mass of TriangleT object
    # @return integer indicating mass of TriangleT object
    def mass(self):
        return self.m

    # @brief mass moment of inertia for TriangleT object
    # @return integer indicating mass moment of inertia
    def m_inert(self):
        return (self.m * self.s ** 2) / 12
