import numpy as np
import matplotlib.pyplot as plt

# Define the objective function (e.g., a simple quadratic function with a maximum)
def objective_function(x):
    return -x**2 + 4*x + 10 # Parabola opening downwards, max at x=2

# Steepest Ascent Hill Climbing algorithm
def steepest_ascent_hill_climbing(start_point, step_size, max_iterations=100, bounds=None):
    current_point = start_point
    history = [current_point]

    for i in range(max_iterations):
        # Explore neighbors: current_point - step_size and current_point + step_size
        neighbor_left = current_point - step_size
        neighbor_right = current_point + step_size

        # Apply bounds if provided
        if bounds:
            neighbor_left = max(bounds[0], neighbor_left)
            neighbor_right = min(bounds[1], neighbor_right)

        current_value = objective_function(current_point)
        left_value = objective_function(neighbor_left)
        right_value = objective_function(neighbor_right)

        # Determine the steepest ascent
        if left_value > current_value and left_value >= right_value:
            next_point = neighbor_left
        elif right_value > current_value and right_value > left_value:
            next_point = neighbor_right
        else:
            # No neighbor improves the objective function, so we've reached a local maximum
            break

        current_point = next_point
        history.append(current_point)

    return current_point, objective_function(current_point), history

# --- Parameters ---
start_point = 0.0 # Starting point for the search
step_size = 0.1   # How much to move in each step
bounds = (-5.0, 5.0) # Search within these bounds

# Run the algorithm
final_point, final_value, search_history = steepest_ascent_hill_climbing(start_point, step_size, bounds=bounds)

print(f"Starting point: {start_point}")
print(f"Final (local) maximum found at x = {final_point:.2f}")
print(f"Maximum function value: {final_value:.2f}")

# --- Visualization ---
x_vals = np.linspace(bounds[0] - 1, bounds[1] + 1, 400)
y_vals = objective_function(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='Objective Function f(x) = -x^2 + 4x + 10', color='blue')
plt.plot(search_history, [objective_function(p) for p in search_history], 'ro--', label='Search Path')
plt.plot(start_point, objective_function(start_point), 'go', markersize=8, label='Start Point')
plt.plot(final_point, final_value, 'rx', markersize=10, label='Final Local Max')

plt.title('Steepest Ascent Hill Climbing for f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()