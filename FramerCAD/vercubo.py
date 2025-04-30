import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Definir las vértices del cubo
vertices = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],  # Base inferior
            [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]]  # Base superior

# Definir las caras del cubo conectando las vértices
faces = [[vertices[j] for j in [0, 1, 2, 3]],  # Base inferior
         [vertices[j] for j in [4, 5, 6, 7]],  # Base superior
         [vertices[j] for j in [0, 1, 5, 4]],  # Lado frontal
         [vertices[j] for j in [2, 3, 7, 6]],  # Lado posterior
         [vertices[j] for j in [0, 3, 7, 4]],  # Lado izquierdo
         [vertices[j] for j in [1, 2, 6, 5]]]  # Lado derecho

# Crear la figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar las caras del cubo
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Establecer los límites del gráfico
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])
ax.set_zlim([0, 2])

plt.show()
