file=open('Notes.txt')
#print(file.read())
print(file.readline())
file.seek(0)
print(file.read(10))

newFile=open("NewNotes.txt","w")
newFile.write("This is example of file handling \n Demo")
newFile.close()

with open("NewNotes.txt","w") as fileWriting:
    fileWriting.write("New Content")

newFile1=open("NewNotes.txt")
print(newFile1.read())

appendFile=open("NewNotes.txt","a")
appendFile.write("appended text")