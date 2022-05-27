import time
import numpy as np

def rand(low=0, high=1, mult=16807, mod=(2**31)-1, seed=None, size=1):
	if(seed == None):
		t = time.perf_counter()
		seed = int(10**9*float(str(t-int(t))[0:]))

	U = np.zeros(size)
	x = (seed * mult + 1) % mod
	U[0] = x / mod

	for y in range(1, size):
		x = (x * mult + 1) % mod
		U[y] = x / mod

	return low + (high - low) * U

x = rand(low=0, high=1, seed=34544564545457, size=500)
print(x)