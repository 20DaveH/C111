import os
import shutil 

#folder
#os.mkdir("second")

#get current working directory
print(os.getcwd())

#checking if a path exists
print(os.path.exists("second1"))

#splitting the path into root and extension
root = os.path.splitext("test.txt")
print("root: ",root[0])
print("ext: ",root[1])

#Contents of the folder 
print(os.listdir("C110"))

#copying to destination
source = "C:/Users/Preetesh/Desktop/VSC-Python/timer.py"
dest = "C:/Users/Preetesh/Desktop/VSC-Python/second"

shutil.copy(source, dest)

#moving to destination
source = "C:/Users/Preetesh/Desktop/VSC-Python/timer.py"
dest = "C:/Users/Preetesh/Desktop/VSC-Python/third"

shutil.move(source, dest)
