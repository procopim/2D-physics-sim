## @file CircleT.py
#  @author Mark Procopio 400344315
#  @brief CircleT Abstract Data Type module, using Shape interface.
#  @details Assumed that arguments provided will be correct type
#  @date Feb 12, 2021

from Shape import Shape


# @brief CircleT ADT utilizing Shape interface
# @details

class CircleT(Shape):

    # @brief constructor for class CircleT; represents a Circle shape in 2D space
    # @detail if any of r and m are less than 1, then we throw ValueError
    # @param x is x coordinate of center mass of Shape
    # @param y is y coordinate of center mass of Shape
    # @param r represents position of the shape body
    # @param m represents the mass of the shape
    def __init__(self, x, y, r, m):
        if (r > 0 and m > 0) is False:
            raise ValueError
        self.x = x
        self.y = y
        self.r = r
        self.m = m

    # @brief x centermass of CircleT object
    # @return integer indicating x center of mass coordinate of CirtceT object
    def cm_x(self):
        return self.x

    # @brief y centermass of CircleT object
    # @return integer indicating y center of mass coordinate CirtceT object
    def cm_y(self):
        return self.y

    # @brief mass of CircleT object
    # @return integer indicating mass of CircleT object
    def mass(self):
        return self.m

    # @brief mass moment of inertia for CircleT object
    # @return integer indicating mass moment of inertia
    def m_inert(self):
        return (self.m * self.r) ** 2 / 2