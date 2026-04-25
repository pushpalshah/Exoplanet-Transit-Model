import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. Define the Physics Model (A simplified box-transit model)
def transit_model(time, period, transit_depth, transit_duration, phase_shift):
    """Calculates the theoretical light flux of a star during a planetary transit."""
    flux = np.ones_like(time)
    
    # Calculate where the planet is in its orbit (phase)
    phase = (time - phase_shift) % period
    
    # Determine if the planet is currently blocking the star
    in_transit = np.abs(phase - period/2) < transit_duration/2
    flux[in_transit] -= transit_depth
    
    return flux

# 2. Generate Synthetic Telescopic Data
np.random.seed(42) # For reproducibility
time_days = np.linspace(0, 20, 1000) # 20 days of observation

# True parameters of our "hidden" exoplanet
true_period = 4.5       # days
true_depth = 0.02       # 2% drop in brightness (roughly a Jupiter-sized planet)
true_duration = 0.3     # days
true_phase = 1.0        # offset

# Generate the theoretical curve and add random Gaussian noise (simulating instrument error)
clean_flux = transit_model(time_days, true_period, true_depth, true_duration, true_phase)
noise = np.random.normal(0, 0.005, len(time_days))
observed_flux = clean_flux + noise

# 3. Analyze the Data (The Inverse Problem)
# We provide initial guesses for the algorithm to start hunting for the planet
initial_guesses = [4.0, 0.01, 0.2, 0.0]

# Use non-linear least squares to fit our model to the noisy data
optimized_params, covariance = curve_fit(
    transit_model, 
    time_days, 
    observed_flux, 
    p0=initial_guesses
)

fitted_period, fitted_depth, fitted_duration, fitted_phase = optimized_params

# 4. Visualize the Results
plt.figure(figsize=(10, 6))
plt.scatter(time_days, observed_flux, color='gray', s=10, alpha=0.6, label='Telescope Data (Noisy)')
plt.plot(time_days, clean_flux, color='blue', linewidth=2, linestyle='--', label='True Physics')
plt.plot(time_days, transit_model(time_days, *optimized_params), color='red', linewidth=2, label='Computational Fit')

plt.title("Exoplanet Transit Light Curve Analysis", fontsize=14)
plt.xlabel("Time (Days)", fontsize=12)
plt.ylabel("Relative Flux (Brightness)", fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"--- Analysis Results ---")
print(f"Calculated Orbital Period: {fitted_period:.3f} days (True: {true_period})")
print(f"Calculated Transit Depth: {fitted_depth:.4f} (True: {true_depth})")