
def nForest(n:int) ->None:
    # Write your solution here.
    for i in range(n):
        stars = ""
        for j in range(n - (i + 1)):
            stars += "  "
        for j in range(2 * (i + 1) - 1):
            stars += "* "
        print(stars)
    for i in range(n):
        if(i == 0):
            continue
        rem_stars = 2 * n - (2 * i + 1)
        rem = ""
        for j in range(i):
            rem += "  "
        for j in range(rem_stars):
            rem += "* "
        print(rem)

nForest(10)
print(" ")

def printC(n: int) -> None:
    for i in range(n):
        pattern = ""
        for j in range(i):
            num = n - j
            pattern += str(num) + " "
        for j in range(2 * n - (2 * i + 1)):
            num = n - i
            pattern += str(num) + " "
        for j in range(i):
            num = n - i + ( j + 1)
            pattern += str(num) + " "
        print(pattern)
    for i in range(n):
        pat2 = ""
        for j in range(n - (i + 1)):
            num = n - j 
            pat2 += str(num) + " "
        for j in range(2 * i + 1):
            if(i == n - 1): continue
            num = i + 2
            pat2 += str(num) + " "
        la_pat = n - (i + 1)
        for j in range(la_pat):
            num = n - la_pat + (j + 1)
            pat2 += str(num) + " "
        print(pat2)

printC(9)
