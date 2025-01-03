
import timeit
import cProfile
import sys
import os

SCRIPTS = 2
RUNS = 100

script = [None]*SCRIPTS
for i in range(SCRIPTS):
	print(F"TESTING SCRIPT {i} for {RUNS} times...")
	sys.stdout = open(os.devnull, 'w') # Suppress prints
	script[i] = timeit.timeit(f"main{i}()", setup=f"from main{i} import main as main{i}", number=RUNS)
	sys.stdout = sys.__stdout__  # Restore stdout

for i in range(SCRIPTS):
	print(f"Average execution time of SCRIPT {i} with {RUNS} runs: {script[i] / 100}")

"""
for i in range(SCRIPTS):
	sys.stdout = open(os.devnull, 'w') # Suppress prints
	exec(f"from main{i} import main as main{i}")
	sys.stdout = sys.__stdout__  # Restore stdout

	cProfile.run(f"main{i}()")
"""