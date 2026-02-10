import numpy as np
import math as m
import matplotlib.pyplot as plt
import pygame


mu = 398600  


position = np.array(
    list(map(float, input("Enter position r (x,y,z) km: ").split(",")))
)
velocity = np.array(
    list(map(float, input("Enter velocity v (vx,vy,vz) km/s: ").split(",")))
)


r = np.linalg.norm(position)
v = np.linalg.norm(velocity)

v_r = np.dot(position, velocity) / r
h_vec = np.cross(position, velocity)
h = np.linalg.norm(h_vec)
v_theta = h / r

i = m.acos(h_vec[2] / h)

k = np.array([0, 0, 1])
N_vec = np.cross(k, h_vec)
N = np.linalg.norm(N_vec)

energy = v**2 / 2 - mu / r
a = -mu / (2 * energy)

e_vec = (np.cross(velocity, h_vec) / mu) - position / r
e = np.linalg.norm(e_vec)

Omega = m.acos(N_vec[0]/N) if N_vec[1] >= 0 else 2*m.pi - m.acos(N_vec[0]/N)

omega = m.acos(np.dot(N_vec, e_vec)/(N*e)) if e_vec[2] >= 0 else \
        2*m.pi - m.acos(np.dot(N_vec, e_vec)/(N*e))


theta = np.linspace(0, 2*m.pi, 800)
r_pf = (h**2/mu)/(1 + e*np.cos(theta))

x_pf = r_pf * np.cos(theta)
y_pf = r_pf * np.sin(theta)
z_pf = np.zeros_like(x_pf)

orbit_pf = np.vstack((x_pf, y_pf, z_pf))

# ===============================
# Rotation: Perifocal → ECI
# ===============================
R3_O = np.array([
    [m.cos(Omega), -m.sin(Omega), 0],
    [m.sin(Omega),  m.cos(Omega), 0],
    [0, 0, 1]
])

R1_i = np.array([
    [1, 0, 0],
    [0, m.cos(i), -m.sin(i)],
    [0, m.sin(i),  m.cos(i)]
])

R3_w = np.array([
    [m.cos(omega), -m.sin(omega), 0],
    [m.sin(omega),  m.cos(omega), 0],
    [0, 0, 1]
])

Q = R3_O @ R1_i @ R3_w
orbit_eci = Q @ orbit_pf

# ===============================
# Matplotlib 3D Plot
# ===============================
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(orbit_eci[0], orbit_eci[1], orbit_eci[2], label="Orbit")
ax.scatter(position[0], position[1], position[2], color='r', label="Satellite")
ax.scatter(0, 0, 0, color='y', s=100, label="Earth")

ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")
ax.set_title("3D Orbit (ECI Frame)")
ax.legend()
plt.show()

# ==================================================
# ================= PYGAME ==========================
# ==================================================
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orbit Visualization (3D Projection)")
clock = pygame.time.Clock()

scale = 250 / np.max(np.abs(orbit_eci))

orbit_scaled = orbit_eci * scale

def project(x, y, z):
    distance = 600
    factor = distance / (distance + z)
    px = int(x * factor + WIDTH//2)
    py = int(y * factor + HEIGHT//2)
    return px, py

index = 0
running = True

while running:
    clock.tick(60)
    screen.fill((10, 10, 25))

    pygame.draw.circle(screen, (255, 200, 0), (WIDTH//2, HEIGHT//2), 20)

    for j in range(orbit_scaled.shape[1]):
        px, py = project(orbit_scaled[0][j],
                         orbit_scaled[1][j],
                         orbit_scaled[2][j])
        pygame.draw.circle(screen, (120, 120, 255), (px, py), 2)

    px, py = project(orbit_scaled[0][index],
                     orbit_scaled[1][index],
                     orbit_scaled[2][index])
    pygame.draw.circle(screen, (0, 255, 255), (px, py), 8)

    index = (index + 1) % orbit_scaled.shape[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
print("\n===== ORBITAL ELEMENTS =====")
print(f"Semi-major axis a (km): {a:.4f}")
print(f"Eccentricity vector e: {e_vec}")
print(f"Eccentricity magnitude e: {e:.6f}")
print(f"Inclination i (deg): {m.degrees(i):.4f}")
print(f"RAAN Ω (deg): {m.degrees(Omega):.4f}")
print(f"Argument of perigee ω (deg): {m.degrees(omega):.4f}")
print(f"True anomaly ν (deg): {m.degrees(nu):.4f}")

print(f"Radial velocity v_r (km/s): {v_r:.6f}")
print(f"Transverse velocity v_θ (km/s): {v_theta:.6f}")
print(f"Flight-path angle γ (deg): {m.degrees(gamma):.4f}")
print(f"Specific mechanical energy (km^2/s^2): {energy:.6f}")
print(f"Specific angular momentum h (km^2/s): {h:.6f}")