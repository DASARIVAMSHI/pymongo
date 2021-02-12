class Student:

    def __init__(self,id,fname,lname,course,year,gpa,university,mobile):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.course = course
        self.year = year
        self.gpa = gpa
        self.university = university
        self.email = fname+lname+"@gmail.com"
        self.mobile = mobile
    def Student_info(self):
        print('Name:',self.fname,self.lname)
        print('ID Number:',self.id)
        print('Course:',self.course)
        print('Year:',self.year)
        print('GPA:',self.gpa)
        print('University:',self.university)
        print('Email ID:',self.email)
        print('Mobile Number:',self.mobile)

    def getYear(self):
        return(self.year)

    def getName(self):
        return self.fname+' '+self.lname

    def getID(self):
        return(self.id)

    def getMobileNo(self):
        return(self.mobile)

    def getEmail(self):
        return(self.email)

    def getUniversity(self):
        return(self.university)

    def getCourse(self):
        return(self.course)

    def getGPA(self):
        return(self.gpa)

    def getFname(self):
        return(self.fname)

    def getLname(self):
        return(self.lname)

    def setFname(self):
        a=input("Please enter the first name:")
        Student.setEmail(self, a, self.fname)
        self.fname=a
        print('First Name has been edited successfully')

    def setEmail(self,new,old):
        self.email = self.getEmail().replace(old,new)

    def setLname(self):
        a=input("Please enter the Last name:")
        Student.setEmail(self, a, self.lname)
        self.lname=a
        print('Last Name has been edited successfully')


c=0
s1 = Student(190330272,'vamshi','Dasari','PFSD',2021,8.86,'KL University',8008206001)
c=c+1
s1.Student_info()

print()
print()
print()

print('Name:',s1.getName())
print('Gmail:',s1.getEmail())
print()
s1.setFname()
print()
s1.setLname()
print()
print('Name:',s1.getName())
print('Gmail',s1.getEmail())

print()
print()
print()


s2 = Student(190330272,'vamshi','Dasari','PFSD',2021,8.86,'KL University',8008206001)
c=c+1
s2.Student_info()

#print(s2.getName())
#print(s2.getEmail())
#s2.setFname()
#s2.setLname()
#print(s2.getEmail())

print()
print()
print()


s3 = Student(190330272,'vamshi','Dasari','PFSD',2021,8.86,'KL University',8008206001)
c=c+1
s3.Student_info()

#print(s3.getName())
#print(s3.getEmail())
#s3.setFname()
#s3.setLname()
#print(s3.getEmail())

print()
print()
print()
print('Number of instances created =',c)