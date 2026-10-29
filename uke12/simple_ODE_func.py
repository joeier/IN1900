import matplotlib.pyplot as plt
import numpy as np


def ODEsolver(f, u_k, t_start, t_stop, steps):
    t = np.linspace(t_start, t_stop, steps+1)
    u = np.zeros(steps+1)
    u[0] = u_k
    dt = (t_stop - t_start) / steps

    for i in range(steps):
        u[i+1] = dt * f(u[i], t[i]) - u[i]

    return t, u

def f(u, t=0):
    return u / 5

def exact(t):
    return 0.1 * np.exp(5*t)


result = ODEsolver(f, 0.1, 0, 20, 10000)
plt.plot(result[0], result[1])
plt.grid()
plt.show()