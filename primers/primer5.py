fileptr = open("newfile.txt", "x")
print(fileptr)
if fileptr:
    print("File created successfully")
    # closes the opened file
    fileptr.close()
