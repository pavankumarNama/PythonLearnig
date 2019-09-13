# Working with temporary files
import os
import tempfile

# TODO: get information about the temp data environment
# print('tempfile DIR: ', tempfile.gettempdir())
# print('tempfile prefix: ', tempfile.gettempprefix())

# TODO: create a temporary file using mkstemp()

# (temposhandler, tempfp) = tempfile.mkstemp('.tmp', 'tempfileex', None, True)
# f = open(tempfp, 'w+t')
# f.write('In Temp file line one......\n')
# f.seek(0)
# print(f.read())
# f.close()
# print('temposhandler', temposhandler)
# print('tempfp', tempfp)
# f = open(temposhandler, 'r+t')
# f.write('TEMP TEMP TEMP')
# f.seek(0)
# print(f.read())
# print(os.path.abspath(tempfp))
# f.close()
# f = os.fdopen(temposhandler, 'w+t')
# f.write('My Temp File............')
# f.seek(0)
# print(f.read())
# f.close()
# os.remove(tempfp)

# TODO: create a temp file using the TemporaryFile class
# with tempfile.TemporaryFile('w+t') as tfp:
#     tfp.write("In temp file temp data.........")
#     tfp.seek(0)
#     print(tfp.read())


# TODO: create a temporary directory using the TemporaryDirectory class
# with tempfile.TemporaryDirectory() as tfd:
#     dp = os.path.join(tfd, 'tempfile2.txt')
#     fp = open(dp, 'w+t')
#     fp.write('Nothing............')
#     fp.seek(0)
#     print(fp.read())
#     fp.close()
