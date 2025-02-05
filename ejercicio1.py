"""
Yura Hernandez H
Semestre 3
Ingenieria de sistemas    
    
"""


if __name__ == "__main__":
    
    inInt = input()
    convertion = list(str(inInt)) 
    result = 0
    for i in range(len(convertion)):
        result += int(convertion[i])
    
    print(result)