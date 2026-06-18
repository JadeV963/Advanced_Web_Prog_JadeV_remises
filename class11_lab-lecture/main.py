from course import Course
from status import CourseStatus, DeliveryMode
from student import Student, StudentLevel

course1 = Course("Advanced Programming", 30, CourseStatus.OPEN, DeliveryMode.ONLINE)
course1.display_info()

course1.close_registration()
course1.display_info()

#course1.cancel_course()
#course1.display_info()

#course1.reopen_course()
#course1.display_info()

#test with wrong values
#course2 = Course("Bad Course", 20, "open")
#course3 = Course("Bad Course", 0, CourseStatus.OPEN)
#course4 = Course("Bad Course", 100, CourseStatus.OPEN)

student1 = Student("Jade", StudentLevel.ADVANCED)
student1.display_info()