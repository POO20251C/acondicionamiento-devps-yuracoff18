"""
Yura Hernandez H
Semestre 3
Ingenieria de sistemas    
    
"""

vocals = {"a","e","i","o","u"}


if __name__ == "__main__":
    string = input()
    count = 0
    for i in string:
        if i in vocals:
            count += 1
    print(count)