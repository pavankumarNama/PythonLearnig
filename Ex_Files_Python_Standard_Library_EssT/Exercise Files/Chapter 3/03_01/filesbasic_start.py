# Basic file operations in Python


# TODO: open a file for writing data
# "w" means write, "r" means read, "a" means append, "r+" means read and write
# fp = open('testfile.txt', 'w')
# fp.write('Write some text.......\n')
# fp.close()

# TODO: read a file's data
# with open('testfile.txt', 'r') as fp:
#     print(fp.read())

# TODO: Add data to an existing file
with open('testfile.txt', 'a+') as fp:
    fp.write("Secondline in text file\n")
    fp.seek(100)
    data = fp.read()
    print("File Contains", data)
