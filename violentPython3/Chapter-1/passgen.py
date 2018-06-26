import itertools
import os
from datetime import datetime
startTime = datetime.now()
import time
end = time.time() + 60*60*2
######### NOTE ############

# So this program creates a list of every single
# Possible password of alpha numeric and special character
# combination for brute force attack. This is terribly intensive
# and running this for 1 to 7 length character takes 2 hours and
# is ~82Gb of memory for a .txt file

f = open("passgen.txt",'w')
chrs = 'abcdefghijklmnopqrstuvwxyz#1234567890%&$#!*'
min_length, max_length = 1, 7
for n in range(min_length, max_length+1):
    for xs in itertools.product(chrs, repeat=n):
        f.write(''.join(xs)+'\n')
        if time.time() > end:
            break

print(datetime.now()-startTime)