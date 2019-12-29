import os
import random

#lets create a simple code which generates a random number
#and writes it to a file and then exits itself

#Note : this proof of concept will form the entire basis of our commution channel

buffer_file  = open("buffer.txt","w")

random_number = random.randrange(2,2439473423)

buffer_file.write(str(random_number))

exit()
