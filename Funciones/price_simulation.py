import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

def generate_price_distribution():
   
    k = 10
    lambda_weibull = 50
    prices = weibull_min.rvs(c=k, scale=lambda_weibull, size=1000)
    return prices

def plot_price_distribution(prices, P0=51):
    
    plt.figure(figsize=(8,5))
    plt.hist(prices, bins=50, density=True, alpha=0.6, color='b', edgecolor='black')
    
    plt.axvline(P0, color='red', linestyle='dashed', linewidth=2, label=f"P0 = {P0}")

    plt.title("Weibull Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    prices = generate_price_distribution()
    plot_price_distribution(prices)