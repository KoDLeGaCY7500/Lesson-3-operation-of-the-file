file1=open("ax50file.txt","r")
file2=open("updated.txt","w")
for line in file1.readlines():
    if not (line.startswith("Coding")):
        print(line)
        file2.write(line)