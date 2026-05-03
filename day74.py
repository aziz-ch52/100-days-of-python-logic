# Program: Dice Roll Simulation (1000 times)

import random

# Step 1: Initialize frequency dictionary for dice faces (1 to 6)
frequency = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

# Step 2: Simulate 1000 dice rolls
for i in range(1000):
    roll = random.randint(1, 6)   # Generate random number between 1 and 6
    frequency[roll] += 1          # Increase count for that face

# Step 3: Print results
print("Dice Roll Frequencies (1000 simulations):")
for face in frequency:
    print("Face", face, "->", frequency[face])

# End of Program