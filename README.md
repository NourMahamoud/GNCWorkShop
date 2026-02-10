Orbit Visualization & Orbital Elements Calculator

This project computes classical orbital elements from a given satellite position and velocity vectors, visualizes the orbit in 3D using Matplotlib, and animates the satellite motion using Pygame with a simple 3D perspective projection.

It’s designed as an educational tool for astrodynamics / orbital mechanics students and enthusiasts.

✨ Features

Compute orbital elements from state vectors:

Semi-major axis (a)

Eccentricity (vector & magnitude)

Inclination (i)

Right Ascension of Ascending Node (RAAN, Ω)

Argument of Perigee (ω)

True anomaly (ν)

Radial & transverse velocities

Specific angular momentum

Specific mechanical energy

3D orbit plotting in ECI frame (Matplotlib)

Real-time animated orbit visualization using Pygame

Simple 3D → 2D perspective projection

Earth and satellite clearly visualized

🧮 Physics Background

Central body: Earth

Gravitational parameter:

μ = 398600 km³/s²


Orbit is generated in the Perifocal (PQW) frame and rotated into the ECI frame using:

RAAN (Ω)

Inclination (i)

Argument of perigee (ω)

Rotation sequence:

ECI = R3(Ω) · R1(i) · R3(ω) · PQW

🛠️ Requirements

Make sure you have Python 3.8+ installed.

Install dependencies:

pip install numpy matplotlib pygame

▶️ How to Run

Clone the repository:

git clone https://github.com/your-username/orbit-visualization.git
cd orbit-visualization


Run the script:

python orbit_visualization.py


Enter satellite state vectors when prompted:

Enter position r (x,y,z) km: 7000,0,0
Enter velocity v (vx,vy,vz) km/s: 0,7.5,1

📊 Output
1️⃣ Matplotlib 3D Plot

Full orbit in ECI frame

Satellite position

Earth at the origin

2️⃣ Pygame Animation

Animated satellite motion along the orbit

Perspective projection for depth feeling

Real-time rendering at ~60 FPS

3️⃣ Console Output

Example:

===== ORBITAL ELEMENTS =====
Semi-major axis a (km): 7032.1234
Eccentricity magnitude e: 0.012345
Inclination i (deg): 7.5946
RAAN Ω (deg): 45.1234
Argument of perigee ω (deg): 120.5678
Specific angular momentum h (km^2/s): 52822.34

📂 Project Structure
orbit-visualization/
│
├── orbit_visualization.py   # Main script
├── README.md                # Project documentation
└── requirements.txt         # (Optional)

🚀 Future Improvements

True anomaly calculation & real-time update

Time-accurate propagation (Kepler / numerical integration)

Camera rotation & zoom in Pygame

Earth texture & coordinate axes

Support for hyperbolic & parabolic orbits

GUI input instead of terminal input

🎓 Educational Use

This project is ideal for:

Orbital Mechanics courses

Aerospace / Space Systems students

Visualization of Keplerian orbits

Learning coordinate frame transformations

📜 License

This project is open-source and available under the MIT License.
Feel free to use, modify, and share.
