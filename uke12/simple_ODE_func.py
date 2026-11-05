import matplotlib.pyplot as plt
import numpy as np


def ForwardEuler(f, u_0, t_start, t_stop, steps):
    t = np.linspace(t_start, t_stop, steps+1)
    u = np.zeros(steps+1)
    u[0] = u_0
    dt = (t_stop - t_start) / steps

    for i in range(steps):
        u[i+1] = u[i] + dt * f(u[i], t[i])

    return t, u

def exact(f, x_start, x_stop, steps):
    x = np.linspace(x_start, x_stop, steps)
    y = np.zeros(steps)
    dt = (x_stop - x_start) / steps

    for i in range(steps):
        y[i] = f(x[i])

    return x, y

def f(u, t):
    return u / 5

def f_e(x):
    return 0.1 * np.exp((1/5) * x)


x, y = exact(f_e, 0, 20, 100)
t_1, u_1 = ForwardEuler(f, 0.1, 0, 20, 4)
t_2, u_2 = ForwardEuler(f, 0.1, 0, 20, 20)
t_3, u_3 = ForwardEuler(f, 0.1, 0, 20, 200)

plt.plot(x, y, label="Exact solution")
plt.plot(t_1, u_1, label="dt = 5")
plt.plot(t_2, u_2, label="dt = 1")
plt.plot(t_3, u_3, label="dt = 0.1")
plt.legend()
plt.grid()
plt.show()