from SEIR0 import *


# a)
class SEIR(SEIR0):
    def __init__(self, beta=0.33, r_ia=0.1,
                r_e2=1.25, lmbda_1=0.33,
                lmbda_2=0.5, p_a=0.4, mu=0.2):

        if isinstance(beta, (float, int)):
            self._beta_func = lambda t: beta
        elif callable(beta):
            self._beta_func = beta
        else:
            raise TypeError("Variable beta is not a number nor callable")

        super().__init__(self._beta_func(0), r_ia, r_e2, lmbda_1, lmbda_2, p_a, mu)

    def __call__(self, t, u):
        self.beta = self._beta_func(t)
        return super().__call__(t, u)


# b)
def test_SEIR_beta_const():
    model = SEIR(beta=0.33)
    t = 0
    u = [1, 2, 3, 4, 5, 6]
    result = model(t, u)
    expected = [(-363 / 2800), (-297 / 560), (-138 / 125), (7 / 10), (-92 / 125), (9 / 5)]
    tol = 1e-10
    msg = "The SEIR class does not work properly"

    for result_val, expect_val in zip(result, expected):
        comparison = abs(result_val - expect_val) < tol
        assert comparison, msg

def test_SEIR_beta_var():
    beta_t = lambda t: 0.33 - 0.1*t
    model = SEIR(beta=beta_t)
    t = 2
    u = [1, 1, 1, 1, 1, 1]
    result = model(t, u)
    expected = [(-611 / 12000), (-3349 / 12000), (-151 / 500), (3 / 10), (-17 / 250), (2 / 5)]
    tol = 1e-10
    msg = "The SEIR class does not work properly with variable beta value"

    for result_val, expect_val in zip(result, expected):
        comparison = abs(result_val - expect_val) < tol
        assert comparison, msg


# c)
def plot_SEIR(t, u, components=["S", "I", "Ia", "R"]):
    u_index = {
        "S": 0,
        "E1": 1,
        "E2": 2,
        "I": 3,
        "Ia": 4,
        "R": 5
    }
    
    u_keys = u_index.keys()
    all_components = list(u_keys)
    for key in all_components:
        if key not in components:
            u_index.pop(key)
    
    N = len(t)
    plot_data = {}
    for key in u_keys:
        plot_data[key] = np.zeros(N)

    for i in range(N):
        for key in plot_data.keys():
            plot_data[key][i] = u[i][u_index[key]]
    
    # # Disse linjene printer det største antallet smittede som trenger ventilatorbehandling. Med de parameterene vi bruker i oppgaven, får vi ca. 12927 pasienter som trenger ventilator. Det er langt mer enn de 700 som vi har i Norge
    # I_peak = max(plot_data["I"])
    # hospital = I_peak / 100 * 20
    # ventilator = hospital / 100 * 25
    # print(ventilator)

    for key, value in plot_data.items():
        plt.plot(t, value, label=key)
    plt.xlabel("Time (days)")
    plt.ylabel("Number in each category")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    test_SEIR_beta_const()
    test_SEIR_beta_var()
    model = SEIR(beta = 0.4)
    t, u = solve_SEIR(model, T = 200, N = 400,
    S_0 = 5.5e6, E2_0 = 100)
    plot_SEIR(t,u)