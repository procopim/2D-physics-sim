from CircleT import CircleT
from TriangleT import TriangleT
from BodyT import BodyT
from Scene import Scene
from Plot import plot
import pytest 
from scipy import integrate




#tests the circleT constructor 
def test_circleT():
    c = CircleT(1.0, 10.0, 0.5, 1.0)
    assert c.cm_x() == 1.0
    assert c.cm_y() == 10.0
    assert c.mass() == 1.0
    assert c.m_inert() == 0.125 

#test to ensure test condition raises ValueError 
def test_circleT_exception():
    with pytest.raises(ValueError):
        c = CircleT(1.0, 10.0, -1, 1.0)

#test to ensure test condition holds for two falses 
def test_circleT_exception2():
    with pytest.raises(ValueError):
        c = CircleT(1.0, 10.0, -1, -1.0)

#tests the TriangleT constructor 
def test_triT():
    t = TriangleT(1.0, -10.0, 5, 17.5)
    assert t.cm_x() == 1.0
    assert t.cm_y() == -10.0
    assert t.mass() == 17.5
    assert round(t.m_inert(), 2) == 36.46

#test to ensure test condition raises ValueError 
def test_triT_exception():
    with pytest.raises(ValueError):
        t = TriangleT(1.0, -10.0, -5, 17.5)

#test to ensure test condition holds for two falses 
def test_triT_exception2():
    with pytest.raises(ValueError):
        t = TriangleT(1.0, -10.0, -5, -17.5)

#test body constructor with non spec provided 
def test_body():
    b = BodyT([1, -1, -1, 1], [5, 5, 5, 5], [5,5,5,5])
    assert b.cm_x() == 0
    assert b.cm_y() == 5
    assert b.mass() == 20
    
#test body constructor to ensure m_inert functioning 
def test_body1():
    b = BodyT([1, -1, -1, 1], [1, 1, -1, -1], [10, 10, 10, 10])
    assert b.cm_x() == 0
    assert b.cm_y() == 0
    assert b.mass() == 40.0
    assert round(b.m_inert(), 2) == 80.0

#body constuctor - cm should be shifted to 10, 10
#b.m_inert() should be equal to b2.m_inert()
def test_body2():
    b2 = BodyT([11, 9, 9, 11], [11, 11, 9, 9], [10, 10, 10, 10])
    assert b2.cm_x() == 10
    assert b2.cm_y() == 10
    assert b2.mass() == 40.0
    assert round(b2.m_inert(), 2) == 80.0

#test conditional exception: xs == ys == ms 
def test_body3():
    with pytest.raises(ValueError):
        b2 = BodyT([11, 9, 9], [11, 11, 9, 9], [10, 10, 10, 10])

#test conditional exception: min(ms) < 1
def test_body4():
    with pytest.raises(ValueError):
        b2 = BodyT([11, 9, 9,11], [11, 11, 9, 9], [0, 10, 10, 10])
    
#test Scene.sim() using Circle object
# test simulates a falling circle under force of gravity in the negative y dir  
#initial velocity in x dir is 0
#initial velocity in y dir is 0
def test_scene_sim():
    c = CircleT(1.0, 100.0, 0.5, 1.0)
    g = 9.81 
    m = 5 #kg 
    Fx = 0
    Fy = -1 * g * m 
    S = Scene(c, Fx, Fy, 0, 0)
    time = [(i * 10) / (100 - 1) for i in range(100)]

    #test 100 steps over 10 seconds 
    t, wsol = S.sim(10, 100)
    max_row = max(wsol) #row index  
    max_val = max(max_row) #max val from the max row

    max_row_index = wsol.index(max_row) #index num of our max row
    max_val_index = max_row.index(max_val) #index of max val in max row

    #manually calc odeint 
    time_res, res = integrate.odeint(Scene.sim.ode, [c.cm_x(), c.cm_y(), 0, 0], time)

    max_row2 = max(res) #row index  
    max_val2 = max(max_row2) #max val from the max row

    assert max_val == max_val2

    
    # max_row_index2 = res.index(max_row2) #index num of our max row
    # max_val_index2 = max_row2.index(max_val2) #index of max val in max row 









