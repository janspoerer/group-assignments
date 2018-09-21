import random
import time

for n in (3:50):
    state = list(range( 1, n ))
    random.shuffle( state )
    print( state )

    start = time.time()
    j = 1
    for j in range(j, len(state)):
        key = state[j]
        i = j - 1
        while i >= 0 and state[i] > key:
          state[i + 1] = state[i]
          i = i - 1
        state[i + 1] = key
    time_consumption = time.time() - start
    print (state)
    print("operation took " + " {0:.9f}".format(time_consumption) + " seconds")
