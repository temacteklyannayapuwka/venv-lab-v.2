# Open the file file2.txt in read mode
with open("file2.txt", "r") as fileptr:
    # Initially, the file pointer is at 0
    print("The file pointer is at byte:", fileptr.tell())

    # Changing the file pointer location to 10
    fileptr.seek(10)

    # tell() returns the location of the file pointer
    print("After reading, the file pointer is at:", fileptr.tell())
