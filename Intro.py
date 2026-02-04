import numpy as np
user_1_step = [3900, 4100, 5600, 6700, 7200, 8400, 9500]
steps = np.array(user_1_step)
print(f"Average steps:{np.mean(steps)}")
print(f"Highest steps:{np.max(steps)}")
goal_met = steps >= 7000
days = steps[goal_met]
print(f"Number of days goal met:{len(days)}")