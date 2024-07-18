import matplotlib.pyplot as plt
import numpy as np

# Create the figure
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Define brain outline in 3D
theta = np.linspace(0, 2 * np.pi, 100)
x = 0.4 * np.cos(theta)
y = 0.4 * np.sin(theta)
z = np.linspace(-0.3, 0.3, 100)

# Draw the brain outline
for zi in z:
    ax.plot(x, y, zi, color='black')

# Highlight the postcentral gyrus area
postcentral_x = [0.45, 0.45, 0.55, 0.55]
postcentral_y = [0.35, 0.65, 0.65, 0.35]
postcentral_z = [0, 0, 0, 0]
ax.plot_trisurf(postcentral_x, postcentral_y, postcentral_z, color='red', alpha=0.5)
ax.text(0.5, 0.65, 0, 'Postcentral Gyrus', color='red', fontsize=12, ha='center')

# Highlight the Prefrontal Cortex
prefrontal_x = [0.1, 0.1, 0.3, 0.3]
prefrontal_y = [0.7, 0.9, 0.9, 0.7]
prefrontal_z = [0, 0, 0, 0]
ax.plot_trisurf(prefrontal_x, prefrontal_y, prefrontal_z, color='orange', alpha=0.5)
ax.text(0.2, 0.8, 0, 'Prefrontal Cortex', color='orange', fontsize=12, ha='center')

# Highlight the Amygdala
amygdala_x = [0.65, 0.65, 0.85, 0.85]
amygdala_y = [0.2, 0.4, 0.4, 0.2]
amygdala_z = [0, 0, 0, 0]
ax.plot_trisurf(amygdala_x, amygdala_y, amygdala_z, color='purple', alpha=0.5)
ax.text(0.75, 0.3, 0, 'Amygdala', color='purple', fontsize=12, ha='center')

# Add arrows for left to right dreaming
ax.quiver(0.2, 0.5, 0, 0.25, 0, 0, color='blue', arrow_length_ratio=0.1)
ax.text(0.325, 0.55, 0, 'Left to Right Dream State', color='blue', fontsize=12, ha='center')

# Add arrows for right to left dreaming
ax.quiver(0.8, 0.5, 0, -0.25, 0, 0, color='green', arrow_length_ratio=0.1)
ax.text(0.675, 0.55, 0, 'Right to Left Dream State', color='green', fontsize=12, ha='center')

# Label the opposing side
ax.text(0.8, 0.35, 0, 'Opposing Side', color='black', fontsize=12, ha='center')

# Label the frontal lobe (anterior part)
ax.text(0.2, 0.8, 0, 'Frontal Lobe', color='black', fontsize=12, ha='center')

# Label the occipital lobe (posterior part)
ax.text(0.8, 0.2, 0, 'Occipital Lobe', color='black', fontsize=12, ha='center')

# Add Nash Equilibrium (using color for 4th dimension)
nash_x = [0.05, 0.05, 0.25, 0.25]
nash_y = [0.05, 0.15, 0.15, 0.05]
nash_z = [0, 0, 0, 0]
ax.plot_trisurf(nash_x, nash_y, nash_z, color='blue', alpha=0.3)
ax.text(0.15, 0.1, 0, 'Nash Equilibrium', color='blue', fontsize=12, ha='center')

# Add Naash Equilibrium (using color for 4th dimension and shapes for 5th dimension)
naash_x = [0.75, 0.75, 0.95, 0.95]
naash_y = [0.05, 0.15, 0.15, 0.05]
naash_z = [0, 0, 0, 0]
ax.plot_trisurf(naash_x, naash_y, naash_z, color='green', alpha=0.3)
ax.text(0.85, 0.1, 0, 'Naash Equilibrium', color='green', fontsize=12, ha='center')

# Adding decay and despair factors to Naash Equilibrium
ax.quiver(0.75, 0.15, 0, 0.05, 0.1, 0, color='darkgreen', arrow_length_ratio=0.1)
ax.text(0.8, 0.25, 0, 'Decay', color='darkgreen', fontsize=10, ha='center')

ax.quiver(0.95, 0.15, 0, -0.05, 0.1, 0, color='darkred', arrow_length_ratio=0.1)
ax.text(0.9, 0.25, 0, 'Despair', color='darkred', fontsize=10, ha='center')

# Adding cosmic strings to represent the Gott Time Machine Metric
cosmic_string_x = np.linspace(0, 1, 100)
cosmic_string_y = 0.5 + 0.1 * np.sin(10 * cosmic_string_x)
cosmic_string_z = 0.3 * np.sin(5 * cosmic_string_x)
ax.plot(cosmic_string_x, cosmic_string_y, cosmic_string_z, color='purple', linestyle='--', linewidth=2, label='Cosmic String')
ax.plot(cosmic_string_x, 1 - cosmic_string_y, -cosmic_string_z, color='purple', linestyle='--', linewidth=2)

# Format the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(-0.5, 0.5)
ax.set_title('Depiction of Dream State Direction with Nash and Naash Equilibria in 5D (Superior View)')
ax.axis('off')
ax.legend()

plt.show()
