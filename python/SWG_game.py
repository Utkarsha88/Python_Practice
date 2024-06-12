
def computer_choice():

    set={"Snake","Water","Gun"}
    for item in set:
        print(f"Computer chose: {item}")
        choice=assign(item)
        break
    return choice

def assign(choice):
    if(choice=="Snake"or choice=="snake"):
        return "1"
    elif(choice=="Water"or choice=="water"):
        return "2"
    elif(choice=="Gun" or choice=="gun"):
        return "3"
    else:
        print("Choose correct option")

print("*****Lets Play Snake, Water & Gun Game******\n")
print("What's your choice?\n")
print("1.Snake\n2.Water\n3.Gun\n")

choice1=input("Enter you choice: ")
if(int(choice1)<=0 or int(choice1)>=4):
    print("please select valid option")
else:
    choice2=computer_choice()

    result=choice1+choice2

    if(choice1==choice2):
        print("DRAW")
    else:
        match result:
            case "13":
                print("you lose")
            case "21":
                print("you lose")
            case "32":
                print("you lose")
            case _:
                print("you won")
