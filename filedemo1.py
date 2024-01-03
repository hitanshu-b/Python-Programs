with open("empdata.dat") as fh:
    with open("empcopy.dat","w") as fhcopy:
        for line in fh:
            fhcopy.write(line)
            print(line)
