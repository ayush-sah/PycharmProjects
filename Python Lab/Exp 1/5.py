# To Generate a random number between 0 and 100

import random
repeat = True
while repeat:
    print("\n\nRandom number between 0 and 100: ", random.randrange(0,100))
    repeat = input("Do you want to repeat ('Y','N'):  ")
    if repeat in ['y', 'Y', 'yes', 'Yes', 'YES']:
       continue
    else:
        repeat = False
