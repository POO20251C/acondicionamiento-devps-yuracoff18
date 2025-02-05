"""
Yura Hernandez H
Semestre 3
Ingenieria de sistemas    
    
"""


if __name__ == "__main__":
    frase = input()
    palindrome = frase.lower()
    palindrome = palindrome.replace(" ", "")
    palindromeT = ""
    for i in range(len(palindrome)-1, -1,-1):
        palindromeT += palindrome[i]
    
    if palindrome == palindromeT:
        print("Si")
    else:
        print("No")