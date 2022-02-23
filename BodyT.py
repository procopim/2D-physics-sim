## @file BodyT.py
#  @author Mark Procopio 400344315
#  @brief BodyT Abstract Data Type module, using Shape interface.
#  @detail Assumed that arguments provided will be correct type
#  @date Feb 13, 2021


from Shape import Shape

# @brief BodyT ADT utilizing Shape interface
# @details

class BodyT(Shape):

    # @brief constructor for class BodyT; representing a body of masses in space
    # @detail if any of r and m are less than 1, then we throw ValueError
    # @param xs is a sequence of x coordinates
    # @param ys is a sequence of y coordinates
    # @param ms is a sequence of masses
    def __init__(self, xs, ys, ms):
        if (len(xs) == len(ys) == len(ms)) == False:
            raise ValueError
        if min(ms) < 1:
            raise ValueError

        self.cmx = cm(xs, ms)
        self.cmy = cm(ys, ms)
        self.m = sum(ms)
        self.moment = (mmom(xs, ys, ms) - self.m * (self.cmx ** 2 + self.cmy ** 2))


    # @brief x centermass of BodyT object
    # @return integer indicating x center of mass coordinate of BodyT object
    def cm_x(self):
        return self.cmx

    # @brief y centermass of BodyT object
    # @return integer indicating y center of mass coordinate BodyT object
    def cm_y(self):
        return self.cmy

    # @brief mass of BodyT object
    # @return integer indicating mass of BodyT object
    def mass(self):
        return self.m

    # @brief mass moment of inertia for BodyT object
    # @return integer indicating mass moment of inertia
    def m_inert(self):
        return self.moment

# @brief helper function returning center mass weighted by coordinate
# @detail function takes sequences as input
# @return integer of weighted center of mass
def cm(z, m):
    weighted = 0
    for i in range(len(m)):
        weighted += (z[i] * m[i])
    return weighted / sum(m)


# @brief mmom variable, imperative to BodyT constructor where state variable
# moment uses mmom to calculate moment of inertia
# @return integer reflecting sum of mass times (x**2 + y**2) for each
#member of sequence xs, ys, ms
def mmom(x, y, m):
    sum = 0
    for i in range(len(m)):
        sum += m[i] * (x[i]**2 + y[i]**2 )
    return sum