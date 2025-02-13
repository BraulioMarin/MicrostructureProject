import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

lambda1 = 50
k = 10
P0 = 51

x = np.linspace(30, 80, 1000)

pdf = weibull_min.pdf(x, k, scale=lambda1)

plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label=f"Weibull PDF\nλ={lambda1}, k={k}", color="blue")
plt.axvline(P0, color="red", linestyle="--", label=f"Precio Spot (P₀ = {P0})")
plt.title("Distribución Weibull para el Precio Spot")
plt.xlabel("Precio Spot (x)")
plt.ylabel("Densidad de Probabilidad")
plt.legend()
plt.grid()
plt.show()

if __name__=="__main__":
    main()