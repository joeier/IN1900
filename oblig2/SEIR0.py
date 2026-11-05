from lib.ODESolver import *
import matplotlib.pyplot as plt


class SEIR0:
    def __init__(self, beta=0.33, r_ia=0.1,
                r_e2=1.25, lmbda_1=0.33,
                lmbda_2=0.5, p_a=0.4, mu=0.2):

        self.beta = beta
        self.r_ia = r_ia
        self.r_e2 = r_e2
        self.lmbda_1 = lmbda_1
        self.lmbda_2 = lmbda_2
        self.p_a = p_a
        self.mu = mu

    def __call__(self, t, u):
        beta = self.beta
        r_ia = self.r_ia
        r_e2 = self.r_e2
        lmbda_1 = self.lmbda_1
        lmbda_2 = self.lmbda_2
        p_a = self.p_a
        mu = self.mu

        S, E1, E2, I, Ia, R = u
        N = sum(u)
        dS = -beta * S * I / N - r_ia * beta * S * Ia / N \
            - r_e2 * beta * S * E2 / N
        dE1 = beta * S * I / N + r_ia * beta * S * Ia / N \
            + r_e2 * beta * S * E2 / N - lmbda_1 * E1
        dE2 = lmbda_1 * (1 - p_a) * E1 - lmbda_2 * E2
        dI = lmbda_2 * E2 - mu * I
        dIa = lmbda_1 * p_a * E1 - mu * Ia
        dR = mu * (I + Ia)
        return [dS, dE1, dE2, dI, dIa, dR]


# a)
def test_SEIR0():
    model = SEIR0()
    t = 0
    u = [1, 2, 3, 4, 5, 6]
    result = model(t, u)
    expected = [(-363 / 2800), (-297 / 560), (-138 / 125), (7 / 10), (-92 / 125), (9 / 5)]
    tol = 1e-10
    msg = "The SEIR0 class does not work properly"

    for result_val, expect_val in zip(result, expected):
        comparison = abs(result_val - expect_val) < tol
        assert comparison, msg


# b)
def solve_SEIR(model, T, N, S_0, E2_0):
    u0 = [S_0, 0, E2_0, 0, 0, 0]
    t_span = (0, T)
    solver = RungeKutta4(model)
    solver.set_initial_condition(u0)
    return solver.solve(t_span, N)

def test_solve_SEIR():
    t, u = solve_SEIR(SEIR0(), 100, 200, 1000, 10)
    msg = "The solve_SEIR function is not working properly"
    expected = 1010
    computed = sum(u[-1])
    tol = 1e-10
    assert (expected - computed) < tol, msg


# c)
def plot_SEIR(t, u):
    N = len(t)
    S, I, Ia, R = [np.zeros(N) for i in range(4)]
    for i in range(N):
        S[i] = u[i][0]
        I[i] = u[i][3]
        Ia[i] = u[i][4]
        R[i] = u[i][5]
    
    plot_data = {
        "S": S,
        "I": I,
        "Ia": Ia,
        "R": R
    }

    for key, value in plot_data.items():
        plt.plot(t, value, label=key)
    plt.xlabel("Time (days)")
    plt.ylabel("Number in each category")
    plt.legend()
    plt.show()


# d)
if __name__ == "__main__":
    test_SEIR0()
    test_solve_SEIR()
    model = SEIR0(beta=0.4)
    t, u = solve_SEIR(model, 200, 400, 5.5e6, 100)
    plot_SEIR(t, u)