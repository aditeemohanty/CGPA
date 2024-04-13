print("HELLOO!!")
branch=input("Enter your branch")
#branch ke hisab se count of subjects
print("Enter 1 if you want to know pointer for each subject.")
print("Enter 2 if you want to know SGPA for SEMESTER 1.")
print("Enter 3 if you want to know SGPA for SEMESTER 2.")
print("Enter 4 if you want to know CGPA for 1st Year.")
print("Enter 5 if you want to know your pointer in each subject, SGPA for SEMESTER 1,SGPA for SEMESTER 2 and CGPA.")
option = int(input("Enter your choice i.e(1/2/3/4/5): "))
#--------------------------------------------------------------------------------------------------------
if option == 1:
    print("Do you want to know how much grade pointer you got in Semester 1 subjects?")
    print("Or you want to know how much grade pointer you got in Semester 2 subjects?")
    o = int(input("Enter 1 for Semester 1 and Enter 2 for Semester 2: "))
    
    if o == 1:
        print("HEY!! This is for SEMESTER 1")
        count = int(input("Enter the count of subjects you have in this semester: "))
        print("In this section please enter the required details as mentioned")
        print("_" * 80)
        m1 = []
        c1 = []
        s1 = []
        g1 = []
        gr_pt = 0
        
        for i in range(0, count):
            sub = input("Enter your Subject name: ")
            s1.append(sub)
            cre = int(input("Enter the credits you received in that subject: "))
            c1.append(cre)
            print("Assume Internal marks as 55")
            num = int(input("Enter your marks in this subject: "))
            print("Enter 'y' if the above mentioned subject is of 125 marks.")
            print("or Enter 'n' if the above mentioned subject is of 50 marks.")
            choice = input("Enter 'y' or 'n': ")
            print("_" * 80)
            choice = choice.lower()  # Convert choice to lowercase
            
            if choice == 'y':
                num1 = (num / 125) * 100
                m1.append(num1)
            else:
                num1 = (num / 50) * 100
                m1.append(num1)
        
        # Calculate grade pointer for each subject
        for i in m1:
            if i <= 100 and i >= 90:
                gr_pt = 10
                g1.append(gr_pt)
            elif i <= 89 and i >= 80:
                gr_pt = 9
                g1.append(gr_pt)
            elif i <= 79 and i >= 70:
                gr_pt = 8
                g1.append(gr_pt)
            elif i <= 69 and i >= 60:
                gr_pt = 7
                g1.append(gr_pt)
            elif i <= 59 and i >= 50:
                gr_pt = 6
                g1.append(gr_pt)
            elif i <= 49 and i >= 40:
                gr_pt = 5
                g1.append(gr_pt)
            else:
                gr_pt = 0
                g1.append(gr_pt)
#-------------------------------------------------------------------------------------------------        
    else:
        print("HEY!! This is for SEMESTER 2")
        count = int(input("Enter the count of subjects you have in this semester: "))
        print("In this section please enter the required details as mentioned")
        print("_" * 80)
        m1 = []
        c1 = []
        s1 = []
        g1 = []
        gr_pt = 0
        
        for i in range(0, count):
            sub = input("Enter your Subject name: ")
            s1.append(sub)
            cre = int(input("Enter the credits you received in that subject: "))
            c1.append(cre)
            print("Assume Internal marks as 55")
            num = int(input("Enter your marks in this subject: "))
            print("Enter 'y' if the above mentioned subject is of 125 marks.")
            print("or Enter 'n' if the above mentioned subject is of 50 marks.")
            choice = input("Enter 'y' or 'n': ")
            print("_" * 80)
            choice = choice.lower()  # Convert choice to lowercase
            
            if choice == 'y':
                num1 = (num / 125) * 100
                m1.append(num1)
            else:
                num1 = (num / 50) * 100
                m1.append(num1)
        
        # Calculate grade pointer for each subject
        for i in m1:
            if i <= 100 and i >= 90:
                gr_pt = 10
                g1.append(gr_pt)
            elif i <= 89 and i >= 80:
                gr_pt = 9
                g1.append(gr_pt)
            elif i <= 79 and i >= 70:
                gr_pt = 8
                g1.append(gr_pt)
            elif i <= 69 and i >= 60:
                gr_pt = 7
                g1.append(gr_pt)
            elif i <= 59 and i >= 50:
                gr_pt = 6
                g1.append(gr_pt)
            elif i <= 49 and i >= 40:
                gr_pt = 5
                g1.append(gr_pt)
            else:
                gr_pt = 0
                g1.append(gr_pt)
        
print("               REPORT               ")
print("BRANCH : ", branch)
for i in range(0, count):
    print("SUBJECT: ", s1[i], " MARKS: ", m1[i], " CREDITS: ", c1[i], " GRADE POINTER: ", g1[i])
print("Thank you")
print("_" * 80)

#-----------------------------------------------------------------------------------------------------
 elif option==2:
    print("HEY!! This is for SEMESTER 1 ")
    print("Are you ready to know your SGPA for SEMESTER 1 ? :)")
    count = int(input("Enter the count of subjects you have in this semester: "))
    print("In this section please enter the required details as mentioned")
    print("_" * 80)
    m1 = []
    c1 = []
    s1 = []
    g1 = []
    gr_pt = 0
    for i in range(0, count):
        sub = input("Enter your Subject name: ")
        s1.append(sub)
        cre = int(input("Enter the credits you received in that subject: "))
        c1.append(cre)
        print("Assume Internal marks as 55")
        num = int(input("Enter your marks in this subject: "))
        print("Enter 'y' if the above mentioned subject is of 125 marks.")
        print("or Enter 'n' if the above mentioned subject is of 50 marks.")
        choice = input("Enter 'y' or 'n': ")
        print("_" * 80)
        choice = choice.lower()  # Convert choice to lowercase
            
        if choice == 'y':
            num1 = (num / 125) * 100
            m1.append(num1)
        else:
            num1 = (num / 50) * 100
            m1.append(num1)
        
        # Calculate grade pointer for each subject
    for i in m1:
        if i <= 100 and i >= 90:
            gr_pt = 10
            g1.append(gr_pt)
        elif i <= 89 and i >= 80:
            gr_pt = 9
            g1.append(gr_pt)
        elif i <= 79 and i >= 70:
            gr_pt = 8
            g1.append(gr_pt)
        elif i <= 69 and i >= 60:
            gr_pt = 7
            g1.append(gr_pt)
        elif i <= 59 and i >= 50:
            gr_pt = 6
            g1.append(gr_pt)
        elif i <= 49 and i >= 40:
            gr_pt = 5
            g1.append(gr_pt)
        else:
            gr_pt = 0
            g1.append(gr_pt)
    sum1=0
    for i in range(0,count):
        sum1=c1[i]*g1[i]
    total=int(input("Enter the total number of credits you had in this semester : "))
    sgpa=(sum1/total)
    print("YOUR SGPA FOR SEMESTER-1 IS : ",sgpa)
#--------------------------------------------------------------------------------------------------
elif option==3:
    print("HEY!! This is for SEMESTER 2 ")
    print("Are you ready to know your SGPA for SEMESTER 2 ? :)")
    count = int(input("Enter the count of subjects you have in this semester: "))
    print("In this section please enter the required details as mentioned")
    print("_" * 80)
    m1 = []
    c1 = []
    s1 = []
    g1 = []
    gr_pt = 0
    for i in range(0, count):
        sub = input("Enter your Subject name: ")
        s1.append(sub)
        cre = int(input("Enter the credits you received in that subject: "))
        c1.append(cre)
        print("Assume Internal marks as 55")
        num = int(input("Enter your marks in this subject: "))
        print("Enter 'y' if the above mentioned subject is of 125 marks.")
        print("or Enter 'n' if the above mentioned subject is of 50 marks.")
        choice = input("Enter 'y' or 'n': ")
        print("_" * 80)
        choice = choice.lower()  # Convert choice to lowercase
            
        if choice == 'y':
            num1 = (num / 125) * 100
            m1.append(num1)
        else:
            num1 = (num / 50) * 100
            m1.append(num1)
        
        # Calculate grade pointer for each subject
    for i in m1:
        if i <= 100 and i >= 90:
            gr_pt = 10
            g1.append(gr_pt)
        elif i <= 89 and i >= 80:
            gr_pt = 9
            g1.append(gr_pt)
        elif i <= 79 and i >= 70:
            gr_pt = 8
            g1.append(gr_pt)
        elif i <= 69 and i >= 60:
            gr_pt = 7
            g1.append(gr_pt)
        elif i <= 59 and i >= 50:
            gr_pt = 6
            g1.append(gr_pt)
        elif i <= 49 and i >= 40:
            gr_pt = 5
            g1.append(gr_pt)
        else:
            gr_pt = 0
            g1.append(gr_pt)
        sum1=0
        for i in range(0,count):
            sum1=c1[i]*g1[i]
        total=int(input("Enter the total number of credits you had in this semester : "))
        sgpa=(sum1/total)
        print("YOUR SGPA FOR SEMESTER-2 IS : ",sgpa)
#-------------------------------------------------------------------------------------------------
elif option==4:
    print("HEY!! This is for SEMESTER 1 ")
    count = int(input("Enter the count of subjects you had in this semester: "))
    print("In this section please enter the required details as mentioned")
    print("_" * 80)
    m1 = []
    c1 = []
    s1 = []
    g1 = []
    gr_pt = 0
    for i in range(0, count):
        sub = input("Enter your Subject name: ")
        s1.append(sub)
        cre = int(input("Enter the credits you received in that subject: "))
        c1.append(cre)
        print("Assume Internal marks as 55")
        num = int(input("Enter your marks in this subject: "))
        print("Enter 'y' if the above mentioned subject is of 125 marks.")
        print("or Enter 'n' if the above mentioned subject is of 50 marks.")
        choice = input("Enter 'y' or 'n': ")
        print("_" * 80)
        choice = choice.lower()  # Convert choice to lowercase
            
        if choice == 'y':
            num1 = (num / 125) * 100
            m1.append(num1)
        else:
            num1 = (num / 50) * 100
            m1.append(num1)
        
        # Calculate grade pointer for each subject
    for i in m1:
        if i <= 100 and i >= 90:
            gr_pt = 10
            g1.append(gr_pt)
        elif i <= 89 and i >= 80:
            gr_pt = 9
            g1.append(gr_pt)
        elif i <= 79 and i >= 70:
            gr_pt = 8
            g1.append(gr_pt)
        elif i <= 69 and i >= 60:
            gr_pt = 7
            g1.append(gr_pt)
        elif i <= 59 and i >= 50:
            gr_pt = 6
            g1.append(gr_pt)
        elif i <= 49 and i >= 40:
            gr_pt = 5
            g1.append(gr_pt)
        else:
            gr_pt = 0
            g1.append(gr_pt)
    sum1=0
    for i in range(0,count):
        sum1=c1[i]*g1[i]
    total=int(input("Enter the total number of credits you had in this semester : "))
    print("HEYY!! This is for SEMESTER 2")
    num_sub=int(input("Enter the total number of subjects you have in 1st year : "))
    print("Enter the marks in each subjects of SEMESTER 1 first and then of SEMESTER 2 :")
    print("Also enter the corresponding credits for the subjects. ")
    m2=[]
    c2=[]
    g2=[]
    pr=0
    for j in range(0,num_sub):
        n=int(input("Enter your marks in subject ")
        credit=int(input("Enter the credits you received in the subject : "))
        c2.append(credit)
        print("Enter 'y' for 125 marks subject and enter 'n' for 50 marks subject ")
        ch=input("Enter 'y' or 'n'")
        if(ch == 'y'):
              num2=(n/125)*100
              m2.append(num2)
        else:
            num2=(n/50)*100
            m2.append(num2)
    for k in m1:
        if(k<=100 and k>=90):
            pr=10
            g2.append(pr)
        elif(k<=89 and k>=80):
            pr=9
            g2.append(pr)
        elif(k<=79 and k>=70):
            pr=8
            g2.append(pr)
        elif(k<=69 and k>=60):
            pr=7
            g2.append(pr)
        elif(k<=59 and k>=50):
            pr=6
            g2.append(pr)
        elif(k<=49 and k>=40):
            pr=5
            g2.append(pr)
        else:
            pr=0
            g2.append(pr)
    pr=0
    sum2=0
for l in range(0,num_sub):
    sum2=c2[l]*g2[l]
t=int(input("Enter the total number of credits you had in this year i.e (1st sem + 2nd sem) : "))
cgpa=((sum2+sum1)/(t+total))
#print cgpa


