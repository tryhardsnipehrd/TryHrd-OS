def main():
    
    arg1 = 0
    arg2 = ""
    arg3 = 0
    print("What simple equation would you like to complete? Press enter after every input. Ex: 3 *enter* * *enter* 3 *enter*")
    arg1 = int(input())
    arg2 = input()
    arg3 = int(input())
    if arg2 == "*":
        print(arg1 * arg3)
        
    elif arg2 == "/":
        print(arg1 / arg3)
        
    elif arg2 == "+":
        print(arg1 + arg3)
        
    elif arg2 == "-":
        print(arg1 - arg3)
        
    else:
        print("no...")
        

