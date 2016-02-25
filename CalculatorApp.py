def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1/num2

def testInput(num1):
    try:
        int(num1)
    except ValueError:
        return False
    else:
        return True


mathOptions = {'+' : add,
                   '-' : subtract,
                   '*' : multiply,
                   '/' : divide
}


    

def Calculator():
    print("welcom to the calculator!")
    userCmd = raw_input("Please input the type of function you would like to perform (+,-,*,/)")
    
    userNum1 = raw_input("First number?")
    while(testInput(userNum1) == False):
        userNum1 = raw_input("First number?")
    userNum1 = int(userNum1)   

    userNum2 = raw_input("Second number?")
    while(testInput(userNum2) == False):
        userNum1 = raw_input("Second number?")
    userNum2 = int(userNum2)
    
    print("Thank you.....Calculating....")

    mathOptions = {'+' : add,
                       '-' : subtract,
                       '*' : multiply,
                       '/' : divide
    }


    calValue = mathOptions[userCmd](userNum1, userNum2)
    print("The calculated value is: " + str(calValue))
    


def main():
    isRunning = True
    while isRunning:
        Calculator()
        restartMsg = raw_input("Restart?(y/n)")
        if(restartMsg == "n"):
            isRunning = False

main()

















        
