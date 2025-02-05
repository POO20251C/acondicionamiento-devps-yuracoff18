"""
Yura Hernandez H
Semestre 3
Ingenieria de sistemas    
    
"""


if __name__ == "__main__":
    frase = input()
    
    palabra = ""
    count = 0
    for i in frase:
        if i == " " and palabra != "":
            count += 1
            palabra = ""
        elif i != " ":
            palabra += i
    if palabra != "":
        count += 1
    
    print(count)