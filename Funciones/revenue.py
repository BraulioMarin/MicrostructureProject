import numpy as np
import matplotlib.pyplot as plt


def plot_expected_revenue():
    
    S = np.linspace(0, 7, 1000)  
    PI = 0.4  
    PL = np.clip(0.5 - 0.08 * S, 0, 0.5)  

   
    Q = S  
    R = Q * (1 - PI)  
    E = R * PL  

    
    E[E < 0] = 0  

    
    plt.figure(figsize=(8, 6))
    plt.plot(S, Q, label='Q Revenues if traders are liquidity motivated', linestyle='solid', color='red')
    plt.plot(S, R, label='R Revenues if 40% are informed', linestyle='solid', color='blue')
    plt.plot(S, E, label='Expected Revenue', linestyle='solid', color='green')

   
    plt.xlabel('Bid-Ask Spread (S)')
    plt.ylabel('Money')
    plt.title('Bid-Ask Spread')
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.legend()
    plt.grid(True)

    
    plt.show()

if __name__ == '__main__':
    plot_expected_revenue()
