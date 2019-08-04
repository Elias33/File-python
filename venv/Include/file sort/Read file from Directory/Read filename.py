import glob
import errno
path = 'F:\GGR\process\*.txt'
files = glob.glob(path)

for name in files:
    try:
        with open(name) as f:
            print(name)
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
