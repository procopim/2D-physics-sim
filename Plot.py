## @file Plot.py
#  @author Mark Procopio 400344315
#  @brief Plot.py module
#  @date Feb 13, 2021
#  @details plots results of our motion simulation

import matplotlib.pyplot as plt

def plot(w, t):
    # @brief plot class provides plotting functionality for our Scene
    # @param w takes in our dependent variable data
    # @param t is our independent time variable

    if len(w) != len(t):
        return ValueError

    x = [w[i][0] for i in range(len(t))]
    y = [w[i][1] for i in range(len(t))]


    fig, axs = plt.subplots(3)
    fig.suptitle('Motion Simulation')
    axs[0].plot(t, x)
    axs[1].plot(t, y)
    axs[2].plot(x, y)

    axs[0].set(ylabel='x (m)')
    axs[1].set(ylabel='y (m)')
    axs[2].set(ylabel='y (m)')
    plt.show()