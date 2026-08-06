import matplotlib.pyplot as plt
import numpy as np

compliancia_estatica = 0.2  # ml
mitad_compliance = compliancia_estatica / 2

presion = 0  # daPa

gradiente = 100

mitad_gradiente = gradiente / 2

ancho_1 = presion + mitad_gradiente
ancho_2 = presion - mitad_gradiente

Punto_1 = np.array([presion, compliancia_estatica])
Punto_2 = np.array([ancho_1, mitad_compliance])
Punto_3 = np.array([ancho_2, mitad_compliance])

x0, y0 = Punto_1  # pico

# --- Parámetro de "puntiagudez" ---
p = 1.3   # 2 = redondeado (Gaussiana normal), 1 = punta marcada, <1 = más afilado aún

def sigma_desde_punto(xi, yi, p):
    return abs(xi - x0) / (-np.log(yi / y0))**(1/p)

sigma_der = sigma_desde_punto(*Punto_2, p)  # lado derecho
sigma_izq = sigma_desde_punto(*Punto_3, p)  # lado izquierdo

def curva_partida(x, p):
    sigma = np.where(x < x0, sigma_izq, sigma_der)
    return y0 * np.exp(-(np.abs(x - x0) / sigma)**p)

# --- Curva ---
x_plot = np.linspace(x0 - 4*sigma_izq, x0 + 4*sigma_der, 400)
y_plot = curva_partida(x_plot, p)

# --- Gráfico ---
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

plt.xlim(-300,300)
plt.ylim(0,1.5)
plt.show()