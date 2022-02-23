## @file Scene.py
#  @author Mark Procopio 400344315
#  @brief Scene Abstract Data Type module, using Shape interface and scipy.
#  @date Feb 13, 2021
#  @details Assumed that arguments provided will be correct type;
#  @details uses Shape and SciPy modules

from Shape import Shape
from scipy import integrate


class Scene():

    # @brief constructor for class Scene;
    # @param s represents a Shape object
    # @param fx represents function of time
    # @param fy represents function of gravity
    # @param vx represents velocity in x direction
    # @param vy represents velocity in y direction
    def __init__(self, s, Fx, Fy, vx, vy):
        self.s = s
        self.Fx = Fx
        self.Fy = Fy
        self.vx = vx
        self.vy = vy

    # @brief getter method: gets the shape of object
    # @return Shape object
    def get_shape(self):
        return self.s

    # @brief getter method: function that gets the unbalanced force of object
    # @return function of time fx, and function of gravity fy
    def get_unbal_forces(self):
        return self.Fx, self.Fy

    # @brief getter method: get initial velocity of object
    # @return object initial velocity in x dir and y dir
    def get_init_velo(self):
        return self.vx, self.vy

    # @brief setter method: set the shape to user provided shape
    # @return none
    def set_shape(self, s2):
        self.s = s2

    # @brief setter method: set unbalanced forces of shape object
    # @return none
    def set_unbal_forces(self, fx1, fy1):
        self.Fx = fx1
        self.Fy = fy1

    # @brief setter method: set initial velocity of shape object
    # @return none
    def set_init_velo(self, vx1, vy1):
        self.vx = vx1
        self.vy = vy1

    # @brief simulates motion with respect to time
    # @return time array, array of position and velocity vecotrs
    def sim(self, tfinal, nsteps):

        t = [(i * tfinal) / (nsteps - 1) for i in range(nsteps)]

        # @brief Ordinary Differential Equation for use in scipy.integrate.odeint
        # @return array of 4 elements needed by odeint to perform ode integration
        def ode(w, t):
            return [w[2], w[3], self.Fx(t) / self.s.mass(), self.Fy(t) / self.s.mass()]

        return t, integrate.odeint(ode, [self.s.cm_x(), self.s.cm_y(), self.vx, self.vy], t)


