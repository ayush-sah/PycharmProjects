# file operations
fread = open("file.txt","r")
print(fread.read())

fwrite = open("file.txt","w")
fwrite.write("These text is being written to the file.")
fwrite.write("Author - Ayush Sah")
fwrite.close()