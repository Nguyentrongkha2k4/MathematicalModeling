import pandas as pd
import numpy as np

def lagrangian_algorithm(num_nodes, num_links, num_cars, duration, num_intervals, num_scenarios, time_threshold):
    # Replace this with your data initialization phase
    link_lengths = np.random.rand(num_links)
    scenario_times = np.random.rand(num_scenarios, num_intervals, num_links)
    scenario_capacities = np.random.rand(num_scenarios, num_links)

    # Initialize Lagrange multipliers
    lagrange_multipliers = np.random.rand(num_intervals, num_links)

    # Placeholder for lower bounds, upper bounds, and relative gaps
    lower_bounds = []
    upper_bounds = []
    relative_gaps = []

    # Simulate the Lagrangian relaxation-based algorithm
    for iteration in range(10):
        # Replace this with your algorithm's iteration steps
        # For simplicity, we'll just calculate lower and upper bounds randomly
        lower_bound = np.random.uniform(10000, 20000)
        upper_bound = np.random.uniform(20000, 30000)

        # Calculate relative gap
        relative_gap = abs(upper_bound - lower_bound) / max(1e-6, abs(upper_bound))

        # Store results
        lower_bounds.append(lower_bound)
        upper_bounds.append(upper_bound)
        relative_gaps.append(relative_gap)

        # Check convergence criteria
        if relative_gap < 0.01:
            break

    return lower_bounds[-1], upper_bounds[-1], relative_gaps[-1]

# Parameters
num_nodes = 100
num_links = 180
num_cars = 500
duration = 120
num_intervals = 120
num_scenarios = 10
time_thresholds = [2, 3, 4, 5, 6, 7, 8]
od_pairs = [(1, 25), (11, 44), (31, 66)]

# Results dictionary
results = {'OD pair': [], 'Time Threshold': [], 'Lower Bound': [], 'Upper Bound': [], 'Relative Gap': []}

# Run experiments
for od_pair in od_pairs:
    for time_threshold in time_thresholds:
        lower_bound, upper_bound, relative_gap = lagrangian_algorithm(
            num_nodes, num_links, num_cars, duration, num_intervals, num_scenarios, time_threshold
        )

        # Store results in the dictionary
        results['OD pair'].append(od_pair)
        results['Time Threshold'].append(time_threshold)
        results['Lower Bound'].append(lower_bound)
        results['Upper Bound'].append(upper_bound)
        results['Relative Gap'].append(relative_gap)

# Convert results to DataFrame for better visualization
df = pd.DataFrame(results)

# Display the DataFrame
print(df)