

#++++++++++++++++++++++++++++++++++++++++Calculate score function ++++++++++++++++++++++
def getscores():


    num=input("How many Test scores are there: ")

    global score
    score=[0]*num
    index=0
    while index<num:
        print('Enter Score#',index+1)
        score[index]=float(input())
        index+=1

#Calculate Average
    total=sum(score)
    global ave
    ave=total/num



#++++++++++++++++++++++++++++++++++++++++Letter Grade Function++++++++++++++++++++++++
def calcletter():

    average=ave
    if    97.0<=average<=100.0:
            letter='A+'
    elif  93.0<=average<=96.0:
            letter='A'
    elif  90.0<=average<=92.0:
            letter='A-'
    elif  87.0<=average<=89.0:
            letter='B+'
    elif  83.0<=average<=86.0:
            letter='B'
    elif  80.0<=average<=82.0:
            letter='B-'
    elif  77.0<=average<=79.0:
            letter='C+'
    elif  73.0<=average<=76.0:
            letter='C'
    elif  70.0<=average<=72.0:
            letter='C-'
    elif  67.0<=average<=69.0:
            letter='D+'
    elif  63.0<=average<=66.0:
            letter='D'
    elif  60.0<=average<=62.0:
            letter='D-'
    elif  0.0<=average<=60.0:
            letter='F'

    global holding
    holding=letter


#+++++++++++++++++++++++++++++++ Get number of students function +++++++++++++++++++++++++++++++
def numstudents():
    print("\n\t\tScore Average Calculator")
    print("\t\t------------------------\n\n")
    global num
    num=input("Enter The number of Students: ")
    i=0
    global names
    names=[]
    global numbers
    numbers=[]
    while i<num:

        #Get Studetns name
            name=raw_input("Enter Students name: ")
            names.append(name)
            getscores()
            calcletter()
            numbers.append(holding)
            i=i+1

#+++++++++++++++++++++++++++ in main ++++++++++++++++++++++++++++
numstudents()

print("\n\t\tLetter Grades of students")
print("\t\t-------------------------")


#display final Result

for value in names:
        print("Students Names: ")
        print("----------------")
        print(value)

for value1 in score:
        print("Students Number Grade: ")
        print("---------------------")
        print(value1)
for value2 in numbers:
        print("Students Letter Grade: ")
        print("---------------------")
        print(value2)
