import time
import os
import tensorflow as tf

with open('/home/zerotwosdev/cron/data.txt', 'a') as outfile:
    timestr = time.strftime("%Y%m%d-%H%M%S")
    outfile.write(timestr)
    outfile.write('\n')

