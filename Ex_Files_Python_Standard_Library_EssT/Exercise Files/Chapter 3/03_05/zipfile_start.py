# Working with ZIP files in Python
import zipfile


# TODO: Create a new ZIP archive
# zfile = zipfile.ZipFile('sample.zip', 'w')
# zfile.write('file1.txt')
# zfile.write('file2.txt')
# zfile.write('file3.txt')

# TODO: Check validity of the file
print(zipfile.is_zipfile('sample.zip'))


# TODO: Read the properties of a ZIP archive
zfile = zipfile.ZipFile('sample.zip')
# print(zfile.read('file1.txt'))
# print(zfile.namelist())
# print(zfile.infolist())

# TODO: Read the properties of ZIP contents
# file2p = zfile.getinfo('file2.txt')
# print(file2p.file_size)

# TODO: Extract ZIP file contents
zfile.extract("file2.txt")
zfile.extractall()


# TODO: Ensure that the file is closed
zfile.close()