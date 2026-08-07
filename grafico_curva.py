import numpy as np
import matplotlib.pyplot as plt

def sigma_desde_punto(xi, yi, x0, y0, p):
    return abs(xi - x0) / (-np.log(yi / y0))**(1/p)


def curva_partida(x, x0, y0, sigma_izq, sigma_der, p):
    sigma = np.where(x < x0, sigma_izq, sigma_der)
    return y0 * np.exp(-(np.abs(x - x0) / sigma)**p)


def graficar(Punto_1, Punto_2, Punto_3, mitad_compliance, p=1.3):
    x0, y0 = Punto_1

    sigma_der = sigma_desde_punto(*Punto_2, x0, y0, p)
    sigma_izq = sigma_desde_punto(*Punto_3, x0, y0, p)

    x_plot = np.linspace(x0 - 4*sigma_izq, x0 + 4*sigma_der, 400)
    y_plot = curva_partida(x_plot, x0, y0, sigma_izq, sigma_der, p)

    plt.figure(figsize=(8, 5))
    plt.plot(x_plot, y_plot, color="steelblue", linewidth=2, label="Curva de compliancia")

    plt.scatter([Punto_1[0], Punto_2[0], Punto_3[0]],
                [Punto_1[1], Punto_2[1], Punto_3[1]],
                color="red", zorder=5, label="Puntos característicos")

    plt.axhline(mitad_compliance, color="gray", linestyle=":", alpha=0.6)
    plt.xlabel("Presión (daPa)")
    plt.ylabel("Compliancia (ml)")
    plt.title("Timpanograma")
    plt.grid(alpha=0.3)
    plt.legend()

    plt.xlim(-300, 300)
    plt.ylim(0, 1.5)
    plt.show()