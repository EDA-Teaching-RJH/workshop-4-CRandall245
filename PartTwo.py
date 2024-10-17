def main():
    z = True
    total = 75
    while z == True:
        coins = int(input("Insert a 5 , 10 , 20 , 50 p coin:"))
        total = total - coins
        if total > 0:
            print("There is " , total , "p left")
        elif total == 0:
            print("payment accepted")
            z = False
        elif total < 0:
            i = 0
            while total < 0:
                total = total + 1
                i = i + 1
                if total == 0:
                    print("you are owed " , i ,"p")
                    z = False
                else:
                    print(f"",end="")
                    
                

main()
        
