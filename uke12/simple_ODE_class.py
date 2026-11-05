import numpy as np
import matplotlib.pyplot as plt


class ForwardEuler:

    def __init__(self, f: function):
        self._f = f

    def solve(self, u_0: float, t_start: int, t_stop: int, steps: int):
        t = np.linspace(t_start, t_stop, steps+1)
        u = np.zeros(steps+1)
        dt = (t_stop - t_start) / steps

        u[0] = u_0

        for i in range(steps):
            u[i+1] = self._advance(u[i], t[i], dt)
        
        return t, u

    def _advance(self, u_i, t_i, dt):
        return u_i + dt * self._f(u_i, t_i)

class Exponential:

    def __init__(self, k):
        self._k = k

    def __call__(self, u, t):
        return self._k * u


f = Exponential(1/5)
euler1 = ForwardEuler(f)
t, u = euler1.solve(0.1, 0, 20, 100)
plt.plot(t, u)
plt.grid()
plt.show()