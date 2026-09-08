c = 0
a = input("number A:")

try:
    X = float(a)
except ValueError:
    print("Error A")
    c = 1

b = input("number B:")

try:
    Y = float(b)
except ValueError:
    print("Error B")
    c = 1

if c == 1:
    c = 1
else:
    
    if X == Y:#hikaku
        print("a = b")
    else:
        if X < Y:
            print("A < B")
        else:
            print("A > B")