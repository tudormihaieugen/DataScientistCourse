import numpy as np
from datetime import datetime

def running_time(big_array):
    now1 = datetime.now()
    print(np.sum(big_array))
    print(np.max(big_array))
    print(np.min(big_array))
    now2 = datetime.now()
    now = now2 - now1
    return now

array = np.random.random(100000000)

time = running_time(array)
print(time)

