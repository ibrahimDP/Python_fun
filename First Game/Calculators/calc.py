import re


print("Clac is running")
print("Type quit to exit")

previous =0
run=True

def performMath():
    global run
    global previous
    equation = ""

    if previous==0:
        equation= input("Enter equation:")
    else:
        equation = input(str(previous))
    
    if equation == 'quit':
        print("Goodbye")
        run = False
    else:
        equation = re.sub('[A-Za-z,.():" "]', '', equation)
        
        if previous == 0:
            previous = eval(equation)
        else:
            previous= eval(str(previous)+ equation)

        #print(previous)

while run:
    performMath()
