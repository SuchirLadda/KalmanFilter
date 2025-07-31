# Kalman Filter Demonstration in Python
This project demonstrates how a **Kalman Filter** can be used to clean up noisy sensor data using both a hand-coded implementation and a library-based one (FilterPy). It’s designed to help understand how Kalman Filters work and how they reduce noise in measurements.

## What It Does
- Simulates noisy altitude measurements.
- Applies two Kalman Filters:
  - A **1D filter** written from scratch.
  - A **FilterPy-based filter**, which uses a standard Kalman framework.
- Plots the raw vs. filtered data to show how noise is reduced.

## Visualization
(./1D Filter/PlottedData.jpg)

## How to Run
1. **Install Python 3** (preferably 3.8+)
2. **Install dependencies:**
   ```bash
   pip install numpy matplotlib filterpy
3. **Run the Script:**
   python filter.py

The script will generate a plot comparing:

- Raw noisy data
- Filtered data using the simple Kalman filter
- Filtered data using FilterPy

## Further Explanation
Coming soon: A detailed write-up with math and visual intuition for Kalman Filters will be linked here.


