with open("test.dat") as fh:
    print(fh.tell())
    print(fh.read(4))
    print(fh.tell())
    print(fh.read(3))
    print(fh.tell())
    fh.seek(2)
    print(fh.read(4))
    print(fh.tell())
