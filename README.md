# Exoplanet-Transit-Model
# Exoplanet Transit Light Curve Analyzer

## Overview
This repository contains a Python-based physical model designed to simulate planetary transits and extract exoplanetary parameters from noisy data environments. By analyzing simulated "light curves," this tool demonstrates the computational methods used to discover and measure planets outside our solar system.

## Physics & Computational Methods
When a planet passes in front of its host star, the star's apparent brightness drops. This script models that theoretical light flux, injects Gaussian noise to simulate telescopic instrument error, and then applies non-linear least-squares optimization to solve the inverse problem.

**Skills Demonstrated:**
* Python (`NumPy`, `SciPy`, `Matplotlib`)
* Non-linear Least-Squares Optimization (`scipy.optimize.curve_fit`)
* Inverse Mathematical Problems
* Data Visualization

## Usage
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the analysis: `python transit_analysis.py`

The script will output calculated orbital periods and transit depths, alongside a plot comparing the noisy telescopic data against the true physics and the computational fit.
