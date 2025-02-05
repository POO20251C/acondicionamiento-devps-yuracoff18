"""
Yura Hernandez H
Semestre 3
Ingenieria de sistemas    
    
"""


if __name__ == "__main__":
    listInt = str(input())
    out = ""
    for i in range(len(listInt)-1, -1, -1):
        out += listInt[i]
    print(out)