# name=["Antar","Keya"]
# result=f"{' '.join(name)} love each other"
# print(result)

def attending(names):
    if not names:
        return "no one is attending"
    elif len(names)==1:
        return f"{names[0]} is attending"
    elif len(names)==2:
        return f"{' and '.join(names)} are attending"
    elif len(names)==3:
        return f"{' '.join(names[:-1])} and {names[-1]} are attending"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} are attending"

names=["Antar","Keya"]
print(attending(names))

