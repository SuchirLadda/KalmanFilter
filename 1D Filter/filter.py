import numpy as np
import matplotlib.pyplot as plt
from filterpy.kalman import KalmanFilter as FilterPyKalman


# True altitude
true_alt = 100.0

# Simulated noisy readings
np.random.seed(0) # We simulate sensor measurements by adding random noise to the true value
noise = np.random.normal(0, 1, 100)
raw_measurements = true_alt + noise

class SimpleKalmanFilter:
    """A minimal 1D Kalman Filter implementation for scalar measurements.
    Think of it like a smart average that adjusts itself over time."""
    def __init__(self, q=0.01, r=1.0, p=1.0, x=0.0):
        self.q = q  # Process noise
        self.r = r  # Measurement noise
        self.p = p  # Estimate error
        self.x = x  # Initial estimate

    def update(self, measurement):
        # Predict phase: increase our uncertainty slightly
        self.p += self.q

        # Kalman gain: how much we should trust this new measurement
        k = self.p / (self.p + self.r)

        # Correction phase: update estimate using the new measurement
        self.x += k * (measurement - self.x)
        self.p *= (1 - k)
        return self.x


simple_kf = SimpleKalmanFilter(q=0.01, r=1.0, p=1.0, x=raw_measurements[0])
filtered_simple = [simple_kf.update(z) for z in raw_measurements]

# --- FilterPy Kalman filter ---


# This uses the more advanced library (FilterPy), but does the same thing

kf = FilterPyKalman(dim_x=1, dim_z=1)
kf.x = np.array([[raw_measurements[0]]])
kf.F = np.array([[1]])   # No motion model
kf.H = np.array([[1]])   # Direct measurement
kf.R = np.array([[1]])   # Measurement noise
kf.Q = np.array([[0.01]])  # Process noise
kf.P = np.array([[1]])   # Initial uncertainty

filtered_filterpy = []
for z in raw_measurements:
    kf.predict()
    kf.update(z)
    filtered_filterpy.append(kf.x[0, 0])


# Standard deviation = how "noisy" the signal is
raw_std = np.std(raw_measurements)
filtered_std = np.std(filtered_simple)
print(f"Noise reduction: {raw_std:.2f} -> {filtered_std:.2f}")

# --- Plotting ---
plt.plot(raw_measurements, label="Raw", alpha=0.5)
plt.plot(filtered_simple, label="Simple Kalman Filter", linestyle='--')
plt.plot(filtered_filterpy, label="FilterPy Kalman Filter", linestyle='-.')
plt.axhline(y=true_alt, color='g', linestyle=':', label="True Altitude")
plt.legend()
plt.title("Simulated Altitude with Kalman Filtering (1D)")
plt.xlabel("Time")
plt.ylabel("Altitude (m)")
plt.grid(True)
plt.show()