#If the file needs to be created newly
with open("example.txt", "w") as file1:
    file1.write("Hello, world!")
#file1=open("example.txt","r") - inside with block so no need to open the file again
    Read=file1.read()
    print(Read)

#file1.close-Outside 'with' block so no need to close the file again. 
# it was closed once 'with' block ended


'''
if file already exists and just need to read content

file1=open("example.txt", "r")
print(file1.read())
file1.close()
'''