import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def lagrangian_algorithm(num_nodes, num_links, num_cars, duration, num_intervals, num_scenarios, time_threshold, link_penalty):
    # Initialize data (replace this with your data initialization phase)
    link_lengths = np.random.rand(num_links)
    print (link_lengths)
    scenario_times = np.random.rand(num_scenarios, num_intervals, num_links)
    # print(scenario_times)
    scenario_capacities = np.random.rand(num_scenarios, num_links)
    # print(scenario_capacities)
    
    # Initialize Lagrange multipliers
    lagrange_multipliers = np.random.rand(num_intervals, num_links)

    lower_bounds = []
    upper_bounds = []
    relative_gaps = []

    # Simulate the Lagrangian relaxation-based algorithm
    for iteration in range(50):
        # Replace this with your algorithm's iteration steps
        # For simplicity, we'll calculate lower and upper bounds based on some formulas
        lower_bound = calculate_lower_bound(link_lengths, scenario_times, scenario_capacities, lagrange_multipliers, link_penalty)
        upper_bound = calculate_upper_bound(link_lengths, scenario_times, scenario_capacities, lagrange_multipliers, link_penalty)

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

# Function to calculate lower bound (replace this with your actual calculation)
def calculate_lower_bound(link_lengths, scenario_times, scenario_capacities, lagrange_multipliers, link_penalty):
    # Placeholder calculation, replace with your actual logic
    return np.sum(link_lengths * scenario_times.mean(axis=0) * lagrange_multipliers) + link_penalty * np.sum(lagrange_multipliers)

# Function to calculate upper bound (replace this with your actual calculation)
def calculate_upper_bound(link_lengths, scenario_times, scenario_capacities, lagrange_multipliers, link_penalty):
    # Placeholder calculation, replace with your actual logic
    return np.sum(link_lengths * scenario_times.max(axis=0) * lagrange_multipliers) + link_penalty * np.sum(lagrange_multipliers)

# Parameters
num_nodes = 50
num_links = 100
num_cars = 100
duration = 120
num_intervals = 120
num_scenarios = 10
time_thresholds = [2, 3, 4, 5, 6, 7, 8]
od_pairs = [(1, 25), (11, 44), (31, 66)]
link_penalty = 2  # minutes

# Results dictionary
results = {'OD pair': [], 'Time Threshold': [], 'Lower Bound': [], 'Upper Bound': [], 'Relative Gaps': []}

# Run experiments
for od_pair in od_pairs:
    for time_threshold in time_thresholds:
        lower_bound, upper_bound, relative_gap = lagrangian_algorithm(
            num_nodes, num_links, num_cars, duration, num_intervals, num_scenarios, time_threshold, link_penalty
        )

        # Store results in the dictionary
        results['OD pair'].append(f"{od_pair[0]}-{od_pair[1]}")
        results['Time Threshold'].append(time_threshold)
        results['Lower Bound'].append(lower_bound)
        results['Upper Bound'].append(upper_bound)
        results['Relative Gaps'].append(f"{relative_gap:.2%}")

# Convert results to DataFrame for better visualization
df_results = pd.DataFrame(results)

# Display the DataFrame
print(df_results)

# plt.figure(figsize=(10, 6))
# for od_pair in od_pairs:
#     od_pair_df = df_results[df_results['OD pair'] == f"{od_pair[0]}-{od_pair[1]}"]
#     plt.plot(od_pair_df['Time Threshold'], od_pair_df['Relative Gaps'], label=f'OD Pair {od_pair}')

# plt.title('Relative Gaps vs. Time Threshold')
# plt.xlabel('Time Threshold')
# plt.ylabel('Relative Gap')
# plt.legend()
# plt.show()

# Plot the relative gaps vs. time thresholds for each OD pair
df_results['Relative Gaps'] = df_results['Relative Gaps'].str.rstrip('%').astype('float') / 1.00

plt.figure(figsize=(10, 6))

# Connect points with lines of the same color
for od_pair in od_pairs:
    od_pair_df = df_results[df_results['OD pair'] == f"{od_pair[0]}-{od_pair[1]}"]

    # Scatter plot
    plt.scatter(od_pair_df['Time Threshold'], od_pair_df['Relative Gaps'], label=f'OD Pair {od_pair}')

    # Connect points with a line of the same color
    plt.plot(od_pair_df['Time Threshold'], od_pair_df['Relative Gaps'], linestyle='-', color='grey')

ytick_values = np.arange(7, 10, 0.5)
plt.yticks(ytick_values)

plt.title('Relative Gaps vs. Time Thresholds')
plt.xlabel('Time Threshold')
plt.ylabel('Relative Gap')
plt.legend()
plt.show()