def readFirstLine(fname):
    with open(fname, "r") as f:
        l = f.read()
    return l

##required readFirstLineFunction
def mykey(appname):
    return readFirstLine("C:\\"+appname+".dat")