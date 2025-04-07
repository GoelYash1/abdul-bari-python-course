import datetime
import time

start_time = datetime.datetime.now()

"""
    The commented part is for time.time()
"""
# start_time = time.time()

for i in range(100000000):
    pass

end_time = datetime.datetime.now()
# end_time = time.time()

execution_time = end_time - start_time
print("Execution TIme:",execution_time.seconds, execution_time.microseconds)
# print("Execution TIme:",execution_time)
