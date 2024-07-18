import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Create the figure
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Define hemisphere outline
u = np.linspace(0, np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
x = 0.4 * np.outer(np.sin(u), np.cos(v))
y = 0.4 * np.outer(np.sin(u), np.sin(v))
z = 0.4 * np.outer(np.cos(u), np.ones_like(v))

# Draw the hemisphere
ax.plot_surface(x, y, z, color='lightgrey', alpha=0.5, rstride=5, cstride=5)

# Highlight the postcentral gyrus area
postcentral_x = [0.05, 0.05, 0.15, 0.15]
postcentral_y = [0.1, 0.2, 0.2, 0.1]
postcentral_z = [0.3, 0.3, 0.3, 0.3]
verts = [list(zip(postcentral_x, postcentral_y, postcentral_z))]
ax.add_collection3d(Poly3DCollection(verts, facecolors='red', alpha=0.5))
ax.text(0.1, 0.15, 0.35, 'Postcentral Gyrus', color='red', fontsize=12, ha='center')

# Highlight the Prefrontal Cortex
prefrontal_x = [0.15, 0.15, 0.3, 0.3]
prefrontal_y = [0.3, 0.4, 0.4, 0.3]
prefrontal_z = [0.3, 0.3, 0.3, 0.3]
verts = [list(zip(prefrontal_x, prefrontal_y, prefrontal_z))]
ax.add_collection3d(Poly3DCollection(verts, facecolors='orange', alpha=0.5))
ax.text(0.225, 0.35, 0.35, 'Prefrontal Cortex', color='orange', fontsize=12, ha='center')

# Highlight the Amygdala
amygdala_x = [0.05, 0.05, 0.15, 0.15]
amygdala_y = [0.25, 0.35, 0.35, 0.25]
amygdala_z = [0.1, 0.1, 0.1, 0.1]
verts = [list(zip(amygdala_x, amygdala_y, amygdala_z))]
ax.add_collection3d(Poly3DCollection(verts, facecolors='purple', alpha=0.5))
ax.text(0.1, 0.3, 0.15, 'Amygdala', color='purple', fontsize=12, ha='center')

# Add arrows for left to right dreaming
ax.quiver(0.1, 0.2, 0.3, 0.2, 0, 0, color='blue', arrow_length_ratio=0.1)
ax.text(0.2, 0.2, 0.35, 'Left to Right Dream State', color='blue', fontsize=12, ha='center')

# Add arrows for right to left dreaming
ax.quiver(0.3, 0.2, 0.3, -0.2, 0, 0, color='green', arrow_length_ratio=0.1)
ax.text(0.25, 0.2, 0.35, 'Right to Left Dream State', color='green', fontsize=12, ha='center')

# Add Nash Equilibrium (using color for 4th dimension)
nash_x = [0.1, 0.1, 0.2, 0.2]
nash_y = [0.05, 0.15, 0.15, 0.05]
nash_z = [0.25, 0.25, 0.25, 0.25]
verts = [list(zip(nash_x, nash_y, nash_z))]
ax.add_collection3d(Poly3DCollection(verts, facecolors='blue', alpha=0.3))
ax.text(0.15, 0.1, 0.3, 'Nash Equilibrium', color='blue', fontsize=12, ha='center')

# Add Naash Equilibrium (using color for 4th dimension and shapes for 5th dimension)
naash_x = [0.25, 0.25, 0.35, 0.35]
naash_y = [0.05, 0.15, 0.15, 0.05]
naash_z = [0.2, 0.2, 0.2, 0.2]
verts = [list(zip(naash_x, naash_y, naash_z))]
ax.add_collection3d(Poly3DCollection(verts, facecolors='green', alpha=0.3))
ax.text(0.3, 0.1, 0.25, 'Naash Equilibrium', color='green', fontsize=12, ha='center')

# Adding decay and despair factors to Naash Equilibrium
ax.quiver(0.25, 0.15, 0.2, 0.05, 0.05, 0, color='darkgreen', arrow_length_ratio=0.1)
ax.text(0.275, 0.2, 0.225, 'Decay', color='darkgreen', fontsize=10, ha='center')

ax.quiver(0.35, 0.15, 0.2, -0.05, 0.05, 0, color='darkred', arrow_length_ratio=0.1)
ax.text(0.325, 0.2, 0.225, 'Despair', color='darkred', fontsize=10, ha='center')

# Adding cosmic strings to represent the Gott Time Machine Metric
cosmic_string_x = np.linspace(0, 0.4, 100)
cosmic_string_y = 0.2 + 0.1 * np.sin(10 * cosmic_string_x)
cosmic_string_z = 0.2 + 0.1 * np.sin(5 * cosmic_string_x)
ax.plot(cosmic_string_x, cosmic_string_y, cosmic_string_z, color='purple', linestyle='--', linewidth=2, label='Cosmic String')
ax.plot(cosmic_string_x, 0.4 - cosmic_string_y, 0.4 - cosmic_string_z, color='purple', linestyle='--', linewidth=2)

# Adding integral-like straight lines between points on the cosmic string
gap = 5  # gap between the lines
for i in range(0, len(cosmic_string_x), gap):
    for j in range(i + gap, len(cosmic_string_x), gap):
        ax.plot([cosmic_string_x[i], cosmic_string_x[j]], 
                [cosmic_string_y[i], cosmic_string_y[j]], 
                [cosmic_string_z[i], cosmic_string_z[j]], 
                color='purple', linestyle=':', linewidth=0.5)

# Adding time travel paths
time_travel_x = [0.1, 0.2, 0.3, 0.25, 0.15]
time_travel_y = [0.2, 0.25, 0.2, 0.1, 0.05]
time_travel_z = [0.3, 0.2, 0.25, 0.3, 0.35]
ax.plot(time_travel_x, time_travel_y, time_travel_z, color='black', linestyle='-', linewidth=1.5, label='Time Travel Path')
ax.scatter(time_travel_x, time_travel_y, time_travel_z, color='black', s=50)

# Adding brain state transitions
transitions = [
    ([0.225, 0.15], [0.35, 0.2], [0.35, 0.3]),  # Prefrontal Cortex to Postcentral Gyrus
    ([0.15, 0.1], [0.2, 0.15], [0.3, 0.35]),    # Postcentral Gyrus to Amygdala
    ([0.05, 0.3], [0.35, 0.4], [0.1, 0.35])     # Amygdala to Prefrontal Cortex
]

for t in transitions:
    ax.plot(t[0], t[1], t[2], color='cyan', linestyle='-', linewidth=1.5, label='State Transition')
    ax.scatter(t[0], t[1], t[2], color='cyan', s=50)

# Format the plot
ax.set_xlim(0, 0.4)
ax.set_ylim(0, 0.4)
ax.set_zlim(0, 0.4)
ax.set_title('Visualization of Brain State Transitions with Time Travel')
ax.axis('off')
ax.legend()

plt.show()
