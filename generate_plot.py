import eight_queens as eightqueen
import numpy as np
import matplotlib.pyplot as plt

best_individual, populations = eightqueen.run_ga(100, 40, 2, 0.3, 1)

min_conflicts = []
average_conflicts = []
max_conflicts = []

for individual in populations:
    conflicts = [eightqueen.evaluate(i) for i in individual]

    min_conflicts.append(np.amin(conflicts))
    max_conflicts.append(np.amax(conflicts))
    average_conflicts.append(np.mean(conflicts))

plt.plot(min_conflicts, "g")
plt.plot(average_conflicts, "b")
plt.plot(max_conflicts, "r")
plt.xlabel("Generations")
plt.ylabel("Conflicts Score")

plt.legend(["Min Conflicts", "Average Conflicts", "Max Conflicts"])
plt.savefig("ga.png")
