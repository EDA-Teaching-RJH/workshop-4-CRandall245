import array

def main():
    camelCase = input("Give me a string of words in camel case:").strip()
    z = list(camelCase)
    i = 0
    length = len(z)
    while i < length:
        Char = z[i]
        i = i + 1
        if Char.islower() == True:
            print(Char,end="")
        elif Char.isupper() == True:
            Char = Char.lower()
            print("_",Char,end="")
            

        

main()
