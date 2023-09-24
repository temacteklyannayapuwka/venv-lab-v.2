# open the file2.txt in append mode. Create a new file if no such file exists.
fileptr = open("file1.txt", "w")
# appending the content to the file
fileptr.write(
"Python is the modern day language. It makes things so simple.\n"
"It is the fastest-growing programing language"
)
# closing the opened the file
fileptr.close()

