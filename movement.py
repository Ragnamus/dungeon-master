import numpy as np

def reduced_speed(base_speed):
    reduced_speed = int(np.ceil((float(base_speed)) / 7.5))
    reduced_speed *= 5
    print("reduced speed is %i" % (reduced_speed))
    return reduced_speed
