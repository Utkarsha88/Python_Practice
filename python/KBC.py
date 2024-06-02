welcome= "welcome to Kaun Banega Crorepati"
print("\n")
print(welcome.center(80))

question=["who developed python language?", " Which type of Programming does Python support?" ,"What will be the value of the following Python expression? (4 + 3 % 5)"]
option=[["a. Guido van Rossum","b. Mark Zuckerberg","c. Bjarne Stroustrup","d. Dennis Ritchie"],["a. object-oriented programming","b. structured programming","c. functional programming","d. all of the mentioned"],["a. 2","b. 7","c. 4","d. 1"]]
answer=["a","d","b"]     """Must be hidden right? I will work on it with my flow"""

count=0
cash=10000
prize=0
for i in range(len(question)):

    print(question[i])

    print("\n")
    print("your options are:\n")
    print(option[i])
    print("\n")
    user=input("enter your answer:")
    
    if(user==answer[i]):
        prize=(i+1)*cash
        print("correct answer, you won Rs.",prize)
        print("\n")
        count=count+1
    else:
        print("incorrect answer, sorry you lost")
        print("\n")
        print ("the correct answer was option ",answer[i])

        if(count!=0):
            count=None
            print("Finally you are taking Rs. ",prize,"dhanrashi to your home")
            break
        else:
            print("Better Luck Next Time")
            count=None
            break

if(count!=None):
    print("\n")
    print("Finally you are taking Rs. ",prize,"dhanrashi to your home")
