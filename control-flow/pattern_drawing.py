



pattern_number  = int(input("Enter the size of the pattern: "))


row = 0


while row < pattern_number:
   
    for col in range(pattern_number):
        print("*", end="")  
    print()  
    row += 1  


