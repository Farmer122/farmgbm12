import numpy as np

# This Python class simulates and plots the Geometric Brownian Motion process.
class pygbm:
    """
    A class to simulate and plot Geometric Brownian Motion (GBM).
    Attributes:
    -----------
    y0 : float
        Initial value of the process.
    mu : float
        Drift coefficient.
    sigma : float
        Diffusion coefficient.
    T : float
        Total time.
    N : int
        Number of time steps.
    seed : int, optional
        Random seed for reproducibility (default is 2).
    Methods:
    --------
    simulate():
        Simulates the GBM process and returns the simulated values.
    plot():
        Plots the simulated GBM process.
    """
    """
    Initializes the pygbm class with the given parameters.
    Parameters:
    -----------
    y0 : float
        Initial value of the process.
    mu : float
        Drift coefficient.
    sigma : float
        Diffusion coefficient.
    T : float
        Total time.
    N : int
        Number of time steps.
    seed : int, optional
        Random seed for reproducibility (default is 2).
    """
    """
    Simulates the Geometric Brownian Motion (GBM) process.
    Returns:
    --------
    y : numpy.ndarray
        Simulated values of the GBM process.
    """
    """
    Plots the simulated Geometric Brownian Motion (GBM) process.
    The plot displays the GBM process over the specified number of steps.
    """

    def __init__(self, y0, mu, sigma, T, N, seed=2):
        self.y0 = y0
        self.mu = mu
        self.sigma = sigma
        self.T = T
        self.N = N
        self.seed = seed
    
    def simulate(self):
        np.random.seed(self.seed)
        dt = self.T / self.N
        dW = np.random.normal(0, np.sqrt(dt), self.N)
        W = np.cumsum(dW)
        t = np.linspace(0, self.T, self.N)
        y = self.y0 * np.exp((self.mu - 0.5 * self.sigma ** 2) * t + self.sigma * W)
        return y
    
    def plot(self):
        import matplotlib.pyplot as plt

        plt.plot(self.simulate())
        plt.title('Geometric Brownian Motion')
        plt.xlabel('steps')
        plt.ylabel('Value')
        plt.show()