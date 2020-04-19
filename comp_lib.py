def printb(b):
    for i in range(int(len(b)/4)):
        print("{4:04x}: {0:02x}{1:02x}{2:02x}{3:02x}".format(b[4*i+3], b[4*i+2], b[4*i+1], b[4*i], 4*i))
def printASCII(b):
    for i in range(int(len(b)/4)):
        print("{4:04x}: {0:s}{1:s}{2:s}{3:s}".format(chr(b[4*i+3]), chr(b[4*i+2]), chr(b[4*i+1]), chr(b[4*i]), 4*i))
