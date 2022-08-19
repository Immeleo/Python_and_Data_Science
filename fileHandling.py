import os
#opening a file and appending/adding more content into it
f = open("demofile.txt", "a") #opening existing file and w in itrite mode
f.write("Hello! Welcome to demofile.txt \nThis file is for testing purposes.\nGood Luck!") #writing into the file
f.close() # closing the file

#Open the file "demofile3.txt" and overwrite the content
f = open("demofile3.txt", "w") #opening in write mode
f.write("Woops! I have deleted the content!")
f.close()


#open  a file for reading it
'''Note: This file are in the same folder as the python code otherwise
the absolute location should be typed instead of the file name '''

'''
#1
print("Opening the First File ...")
f = open("demofile.txt", "r") #opening the file in read mode
print(f.read()) #displaying the read content of the file
print("\n")
#2
print("Opening the Second File ...")
f = open("URLs.txt", "r")
print(f.read()) #reading the first 10 lines
print("\n")

#3
#Opening a file using its directory path/ location
print("Opening the Third File ...")
f = open("C:/Users/Matrix_Leo/Desktop/URLs/Mixed URLs/mixed_urls.txt", "r")
print(f.read())

'''
#Deleting Files
if os.path.exists("demofile.txt"): #check if file exists
  os.remove("demofile3.txt") #remove it
else:
  print("The file does not exist")
