def make_ing(s1):
    lst=["be","see","flee","play"]
    if s1 in lst:
        s2=s1+"ing"

    elif s1.endswith("e"):
        if s1.endswith("ie"):
            s2=s1[:-2]+"ying"
        else:
            s2=s1[:-1]+"ing"

    elif s1[-2] in "aeiou":
        if s1[-3] in "bcdfghjklmnpqrstvwxyz":
            if s1[-1] in "bcdfghjklmnpqrstvwxyz":
                s2=s1+s1[-1]+"ing"
    else:
        s2=s1+"ing"
    return s2

s1 = input("Enter String: ")
s2=make_ing(s1)
print(s1,"--->",s2)
