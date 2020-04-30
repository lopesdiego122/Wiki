##https://docs.python.org/2/library/os.html#files-and-directories

##https://www.geeksforgeeks.org/os-module-python-examples/


### Print arquivos do dir modification time maior que 60 dias
import os

directory = '/home/diegols'

os.system("find " + directory + " -mtime +60 -print")

###Print current work directory getcwd
import os 

###print(os.getcwd()) 
##print(os.listdir('.'))
print(os.listdir(os.getcwd())) 

