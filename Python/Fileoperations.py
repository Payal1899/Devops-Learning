
'''#If the file needs to be created newly
with open("example.txt", "w+") as file1:
    #writes into file example.txt
    file1.write("Hello, world!")
    file1.seek(0)  #adjust cursor to original postion
    #inside with block so no need to open the file again as we have opened file in write+read mode
    Read=file1.read() #reads the file
    #print content of the file
    print(Read)

#file1.close-Outside 'with' block so no need to close the file again. 
# it was closed once 'with' block ended
'''

#if file already exists and just need to read content

file1=open("example.txt", "r")
print(file1.read())
file1.close()
'''

#open file example.txt in read mode
file1=open("example.txt", "r")
#read and print the content of the file 
print(file1.read())
#close the file
file1.close()
'''