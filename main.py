# from macpath import split

import os
# print(split(data,","))
def takeTest():
    file =open("questions.txt")
    # print(file.readlines())
    data=file.readlines()[0]
    file.close()
    questions = data.split(",")
    totallPoints = 0
    for i in questions:
        l=i.split(";")
        q=l[0]
        options=l[1:-1]
        _,ans,points=l[-1].split(' ')
        print(q)
        print("Your options")
        serial = 97
        for j in options:
            print("({}) {}.".format(chr(serial),j))
            serial+=1
        choice=input("\n Enter your options in (a,b,c,d):  ")
        if(choice==ans):
            totallPoints+=int(points)
        print()
    return totallPoints

def addQuestions():
    q=input("Enter Questions: ")
    print("Enter options")
    serial=97
    options=[]
    for i in range(0,4):
        o=input("Enter option ({}) : ".format(chr(serial+i)))
        options.append(o)
    ans=input("Enter answer: ")
    points = input("Enter Points: ")

    d=","+q+"? ;"+options[0]+ ";"+options[1]+";"+options[2]+";"+options[3]+";"+" {} {}".format(ans,points)
    # s=''
    file=open("questions.txt","a")
    
    file.write(d)
    file.close()

def removeQuestion():
    file =open("questions.txt")
    # print(file.readlines())
    data=file.readlines()[0]
    file.close()
    questions = data.split(",")
    print(questions)
    print("\n\n Questions are: \n\n")
    num=1
    for i in questions:
        print("Question No: ",num)
        num+=1
        l=i.split(";")
        q=l[0]
        options=l[1:-1]
        _,ans,points=l[-1].split(' ')
        print(q)
        print("Your options")
        serial = 97
        for j in options:
            print("({}) {}.".format(chr(serial),j))
            serial+=1
        print("\n")
    q=int(input("Which question do you want to remove: "))
    if(q<num):
        questions.pop(q-1)
        os.remove("questions.txt")

        file=open("questions.txt","w")
        s=""
        for j in questions:
            s=s+j+','
        s=s[:-1]
        print(s)
        file.write(s)

    else:
        print("Question does't exist")


if(__name__=="__main__"):
    while(True):
        print("\n\nWhat do you wanted to do ?\nEnter 1 to Take Test\nEnter 2 to Add Question\nEnter 3 to remove an Question\nEnter 4 to Exit\n")
        a=int(input("Enter (1/2/3/4) : "))
        if(a==1):
            totallPoints=takeTest()
            print("\n\n Your Totall Points are: ",totallPoints)
        elif(a==2):
            addQuestions()
        elif(a==3):
            removeQuestion()
        elif(a==4):
            break
        else:
            print("you have entered incorrect value try again: ")
        
