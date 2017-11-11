#This script helps rename the episode's files in a way
#to make it easier to extract information from it

import os 
directory="season6"
for filename in sorted(os.listdir(directory)):
    filename=directory+"/"+filename
    print (filename)
    print(filename[32:34]+".srt")    
    os.rename(filename, directory+"/"+filename[32:34]+".srt")