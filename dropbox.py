        
classes={}
students={}

def addClass(id, capacity, time):

    if id in classes:
    	return "Error adding class ID"
    else: 
    	enrolled_students=[]
    	classes[id]={"capacity":capacity, "max": capacity, "time":time,"list":enrolled_students} 
    	return "Successfully added class ID"
      
  
def removeClass(id):
    
    if classes.pop(id) != None:
        return "Successfully removed class ID"
    else:
        return "Error removing class ID"
  

def infoClass(id):
    
     if id in classes:
     	enroll_class=classes[id]
     	capacity=enrolled_class["capacity"]
     	max_capacity=enroll_class["max"]
     	if capacity==max_capacity:
     		return "Class ID is empty"
     	else:
     		enrolled_students=enrolled_class["list"]
     		return "Class ID has the following students:" + enrolled_class


     else:
         return "Class ID does not exist"    
         

  
def addStudent(id, capacity, start, end):
    
    if id in students:
    	return "Error adding student ID"
    else: 
    	enroll_classes=[]
    	students[id]={"capacity":capacity, "start":start, "end":end, "list":enroll_classes} 
    	return  "Successfully added student ID"

def removeStudent(id):
    if students.pop(id) != None:
        return "Successfully removed student ID"
    else:
        return "Error removing student ID"

  
def infoStudent(id):
     if id in students:
     	student=students[id]
     	enrolled_classes=student["list"]
     	if len(enrolled_classes)==0:
     		return  "Student ID is not taking any classes"
     	else:
     		enroll_classes.sort()
     		return "Student ID is taking the following classes:" + enrolled_classes

     else:
         return "Student ID does not exist"   
 

	
  
def enrollStudent(studentId, classId):
	if studentId in students and classId in classes:
		enroll_student=students[studentId]
		enroll_class=classes[classId]
		capacity=enroll_class["capacity"]
		time=enroll_class["time"]
		max_capacity=enroll_class["max"]
		start=enroll_student["start"]
		end=enroll_student["end"]

		print capacity

		if capacity == 0 or time<start or time>end:
			return "Enrollment of student STUDENTID in class CLASSID failed"
		else:
			enrolled_students=enroll_class["list"]
			enrolled_students.append(studentId)
			max_capacity=enroll_class["max"]
			capacity=capacity-1
			if capacity<=0:
				capacity=0

			classes[id]={"capacity":capacity, "max": capacity, "time":time,"list":enrolled_students} 
    		return "Number of free spots left in class " + str(classId)+ " : " +str(capacity)

	else:
         return "Enrollment of student STUDENTID in class CLASSID failed" 
  

def unenrollStudent(studentId, classId):
	if studentId in students and classId in classes:

		
		enroll_class=classes[classId]
		enrolled_students=enroll_class["list"]
		
		#check if this student is taking this class
		if studentId in enrolled_students:
			enrolled_students.remove(studentId)
			capacity=enroll_class["capacity"]
			max_capacity=enroll_class["max"]
			capacity=capacity+1
			if capacity>=max_capacity:
				capacity=max_capacity
			time=enroll_class["time"]
			classes[classId]={"capacity":capacity, "time":time,"list":enrolled_students} 
			return "Number of free spots left in class " + str(classId)+ " : " +str(capacity)
		else:
			return "Unenrollment of student STUDENTID in class CLASSID failed"



	else:
		return "Unenrollment of student STUDENTID in class CLASSID failed"

  
 


print addClass(1,2,3)
print addClass(1,2,3)
print addClass(2,2,3)

print addStudent(1232,2,1,5)

print enrollStudent(1232,1)

print unenrollStudent(1232,1)


