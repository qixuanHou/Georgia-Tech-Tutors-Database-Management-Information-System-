import pymysql





db = pymysql.connect(host = "academic-mysql.cc.gatech.edu",

                     db = "cs4400_Group_51",

                     user = "cs4400_Group_51",

                     passwd = "byYHZf0a")

c = db.cursor()



##Administrator 1

c.execute("INSERT INTO Administrator (AGTID, APassword) VALUES (100000000, 'zzzzz');") 



##Course CS4400 / CS2200 / MATH3012 / MUSI4630

c.execute("INSERT INTO Course VALUES('CS', 4400)")

c.execute("INSERT INTO Course VALUES('CS', 2200)")

c.execute("INSERT INTO Course VALUES('MATH', 3012)")

c.execute("INSERT INTO Course VALUES('MUSI', 4630)")



##Professor 2 / 3 / 4

c.execute("INSERT INTO Professor VALUES(200000000, 'zzzzz')")

c.execute("INSERT INTO Professor VALUES(300000000, 'zzzzz')")

c.execute("INSERT INTO Professor VALUES(400000000, 'zzzzz')")



##Student 903997777 / 5 / 6 / 7 / 8 / 9 / 11 / 12

c.execute("INSERT INTO Student VALUES(903997777, 'zzzzz', 'Matt', 'Schofield', 'smatt@gatech.edu')")

c.execute("INSERT INTO Student VALUES(500000000, 'zzzzz', 'Anna', 'Adams', '5@gatech.edu')")

c.execute("INSERT INTO Student VALUES(600000000, 'zzzzz', 'Bobby', 'Brown', '6@gatech.edu')")

c.execute("INSERT INTO Student VALUES(700000000, 'zzzzz', 'Conner', 'Coone', '7@gatech.edu')")

c.execute("INSERT INTO Student Values(800000000, 'zzzzz', 'Don', 'Dodger', '8@gatech.edu')")

c.execute("INSERT INTO Student VALUES(900000000, 'zzzzz', 'Elle', 'Elhart', '9@gatech.edu')")

c.execute("INSERT INTO Student VALUES(110000000, 'zzzzz', 'Frank', 'Fitzgerald', '11@gatech.edu')")

c.execute("INSERT INTO Student VALUES(120000000, 'zzzzz', 'Gerald', 'Good', '12@gatech.edu')")

c.execute("INSERT INTO Student VALUES(130000000, 'zzzzz', 'Homer', 'Hart', '13@gatech.edu')")

c.execute("INSERT INTO Student VALUES(140000000, 'zzzzz', 'Jackie', 'Jacobs', '14@gatech.edu')")

c.execute("INSERT INTO Student VALUES(180000000, 'zzzzz', 'Frosty', 'thesnowman', 'IAMTHESNOWMAN@gatech.edu')")



##Grad 5 / 13

c.execute("INSERT INTO Grad VALUES(500000000)")

c.execute("INSERT INTO Grad VALUES(140000000)")





##Undergrad 6 / 7 / 8 / 9 / 11 / 12

c.execute("INSERT INTO Undergrad VALUES(600000000)")

c.execute("INSERT INTO Undergrad VALUES(700000000)")

c.execute("INSERT INTO Undergrad VALUES(800000000)")

c.execute("INSERT INTO Undergrad VALUES(900000000)")

c.execute("INSERT INTO Undergrad VALUES(110000000)")

c.execute("INSERT INTO Undergrad VALUES(120000000)")

c.execute("INSERT INTO Undergrad VALUES(180000000)")





##Tutor 5 / 6 / 7 / 8

c.execute("INSERT INTO Tutor VALUES(500000000, 0000000000, 3.50)")

c.execute("INSERT INTO Tutor VALUES(600000000, 0000000000, 3.60)")

c.execute("INSERT INTO Tutor VALUES(700000000, 0000000000, 3.20)")

c.execute("INSERT INTO Tutor VALUES(800000000, 0000000000, 3.90)")

c.execute("INSERT INTO Tutor VALUES(140000000, 0000000000, 4.00)")

c.execute("INSERT INTO Tutor VALUES(903997777, 2144049500, 3.95)")




##Recommends 

c.execute("INSERT INTO Recommends VALUES(200000000, 500000000, 3, 'Good')")

c.execute("INSERT INTO Recommends VALUES(300000000, 500000000, 4, 'Very good')")

c.execute("INSERT INTO Recommends VALUES(400000000, 500000000, 4, 'Will be a good tutot')")



c.execute("INSERT INTO Recommends VALUES(200000000, 600000000, 3, 'Okay student')")

c.execute("INSERT INTO Recommends VALUES(300000000, 600000000, 4, 'Great')")



c.execute("INSERT INTO Recommends VALUES(200000000, 700000000, 3, 'Very good student')")



c.execute("INSERT INTO Recommends VALUES(200000000, 800000000, 2, 'Ok')")



##TutorTimeSlots

#fall2014

c.execute("INSERT INTO TutorTimeSlots VALUES(500000000,9 , 'FALL2014', 'W')")

c.execute("INSERT INTO TutorTimeSlots VALUES(500000000,9 , 'FALL2014', 'M')")

c.execute("INSERT INTO TutorTimeSlots VALUES(500000000,9 , 'FALL2014', 'F')")



c.execute("INSERT INTO TutorTimeSlots VALUES(600000000,12 , 'FALL2014', 'W')")

c.execute("INSERT INTO TutorTimeSlots VALUES(600000000,12 , 'FALL2014', 'M')")

c.execute("INSERT INTO TutorTimeSlots VALUES(600000000,15 , 'FALL2014', 'T')")

c.execute("INSERT INTO TutorTimeSlots VALUES(600000000,15 , 'FALL2014', 'F')")



c.execute("INSERT INTO TutorTimeSlots VALUES(700000000,10 , 'FALL2014', 'R')")

c.execute("INSERT INTO TutorTimeSlots VALUES(700000000,10 , 'FALL2014', 'T')")

c.execute("INSERT INTO TutorTimeSlots VALUES(700000000,16 , 'FALL2014', 'F')")

c.execute("INSERT INTO TutorTimeSlots VALUES(700000000,16 , 'FALL2014', 'M')")

c.execute("INSERT INTO TutorTimeSlots VALUES(700000000,16 , 'FALL2014', 'W')")



c.execute("INSERT INTO TutorTimeSlots VALUES(800000000,11 , 'FALL2014', 'W')")

c.execute("INSERT INTO TutorTimeSlots VALUES(800000000,11 , 'FALL2014', 'F')")



#spring2014

c.execute("INSERT INTO TutorTimeSlots VALUES(800000000,9 , 'SPRING2014', 'W')")

c.execute("INSERT INTO TutorTimeSlots VALUES(800000000,9 , 'SPRING2014', 'M')")

c.execute("INSERT INTO TutorTimeSlots VALUES(800000000,9 , 'SPRING2014', 'F')")



c.execute("INSERT INTO TutorTimeSlots VALUES(700000000,12 , 'SPRING2014', 'W')")

c.execute("INSERT INTO TutorTimeSlots VALUES(700000000,12 , 'SPRING2014', 'M')")

c.execute("INSERT INTO TutorTimeSlots VALUES(700000000,15 , 'SPRING2014', 'T')")

c.execute("INSERT INTO TutorTimeSlots VALUES(700000000,15 , 'SPRING2014', 'F')")



c.execute("INSERT INTO TutorTimeSlots VALUES(600000000,10 , 'SPRING2014', 'R')")

c.execute("INSERT INTO TutorTimeSlots VALUES(600000000,10 , 'SPRING2014', 'T')")

c.execute("INSERT INTO TutorTimeSlots VALUES(600000000,16 , 'SPRING2014', 'F')")

c.execute("INSERT INTO TutorTimeSlots VALUES(600000000,16 , 'SPRING2014', 'M')")

c.execute("INSERT INTO TutorTimeSlots VALUES(600000000,16 , 'SPRING2014', 'W')")



c.execute("INSERT INTO TutorTimeSlots VALUES(500000000,11 , 'SPRING2014', 'W')")

c.execute("INSERT INTO TutorTimeSlots VALUES(500000000,11 , 'SPRING2014', 'F')")



#summer2014

c.execute("INSERT INTO TutorTimeSlots VALUES(700000000,9 , 'SUMMER2014', 'W')")

c.execute("INSERT INTO TutorTimeSlots VALUES(700000000,9 , 'SUMMER2014', 'M')")

c.execute("INSERT INTO TutorTimeSlots VALUES(700000000,9 , 'SUMMER2014', 'F')")



c.execute("INSERT INTO TutorTimeSlots VALUES(800000000,12 , 'SUMMER2014', 'W')")

c.execute("INSERT INTO TutorTimeSlots VALUES(800000000,12 , 'SUMMER2014', 'M')")

c.execute("INSERT INTO TutorTimeSlots VALUES(800000000,15 , 'SUMMER2014', 'T')")

c.execute("INSERT INTO TutorTimeSlots VALUES(800000000,15 , 'SUMMER2014', 'F')")



c.execute("INSERT INTO TutorTimeSlots VALUES(500000000,10 , 'SUMMER2014', 'R')")

c.execute("INSERT INTO TutorTimeSlots VALUES(500000000,10 , 'SUMMER2014', 'T')")

c.execute("INSERT INTO TutorTimeSlots VALUES(500000000,16 , 'SUMMER2014', 'F')")

c.execute("INSERT INTO TutorTimeSlots VALUES(500000000,16 , 'SUMMER2014', 'M')")

c.execute("INSERT INTO TutorTimeSlots VALUES(500000000,16 , 'SUMMER2014', 'W')")



c.execute("INSERT INTO TutorTimeSlots VALUES(600000000,11 , 'SUMMER2014', 'W')")

c.execute("INSERT INTO TutorTimeSlots VALUES(600000000,11 , 'SUMMER2014', 'F')")



##Tutors

c.execute("INSERT INTO Tutors VALUES(600000000, False, 'CS', 4400)")

c.execute("INSERT INTO Tutors VALUES(700000000, False, 'CS', 4400)")



c.execute("INSERT INTO Tutors VALUES(500000000, True, 'MATH', 3012)")



c.execute("INSERT INTO Tutors VALUES(600000000, False, 'MUSI', 4630)")

c.execute("INSERT INTO Tutors VALUES(800000000, False, 'MUSI', 4630)")

c.execute("INSERT INTO Tutors VALUES(500000000, True, 'MUSI', 4630)")





##Hires

##FALL2014

c.execute("INSERT INTO Hires VALUES(900000000, 'CS', 4400, 12, 'FALL2014', 'W', 600000000)")

c.execute("INSERT INTO Hires VALUES(110000000, 'CS', 4400, 15, 'FALL2014', 'F', 600000000)")

c.execute("INSERT INTO Hires VALUES(120000000, 'CS', 4400, 12, 'FALL2014', 'M', 600000000)")





c.execute("INSERT INTO Hires VALUES(900000000, 'MUSI', 4630, 9, 'FALL2014', 'M', 500000000)")

c.execute("INSERT INTO Hires VALUES(110000000, 'MUSI', 4630, 9, 'FALL2014', 'F', 500000000)")

c.execute("INSERT INTO Hires VALUES(130000000, 'MUSI', 4630, 11, 'FALL2014', 'F', 800000000)")

c.execute("INSERT INTO Hires VALUES(120000000, 'MUSI', 4630, 15, 'FALL2014', 'T', 600000000)")

c.execute("INSERT INTO Hires VALUES(700000000, 'MUSI', 4630, 11, 'FALL2014', 'W', 800000000)")



c.execute("INSERT INTO Hires VALUES(120000000, 'MATH', 3012, 9, 'FALL2014', 'W', 500000000)")





##SPRING2014

c.execute("INSERT INTO Hires VALUES(900000000, 'CS', 4400, 10, 'SPRING2014', 'T', 600000000)")

c.execute("INSERT INTO Hires VALUES(110000000, 'CS', 4400, 10, 'SPRING2014', 'R', 600000000)")

c.execute("INSERT INTO Hires VALUES(120000000, 'CS', 4400, 16, 'SPRING2014', 'F', 600000000)")





c.execute("INSERT INTO Hires VALUES(900000000, 'MUSI', 4630, 11, 'SPRING2014', 'M', 500000000)")

c.execute("INSERT INTO Hires VALUES(110000000, 'MUSI', 4630, 16, 'SPRING2014', 'W', 600000000)")

c.execute("INSERT INTO Hires VALUES(120000000, 'MUSI', 4630, 16, 'SPRING2014', 'M', 600000000)")

c.execute("INSERT INTO Hires VALUES(130000000, 'MUSI', 4630, 9, 'SPRING2014', 'M', 800000000)")

c.execute("INSERT INTO Hires VALUES(700000000, 'MUSI', 4630, 9, 'SPRING2014', 'W', 800000000)")



c.execute("INSERT INTO Hires VALUES(120000000, 'MATH', 3012, 11, 'SPRING2014', 'F', 500000000)")



##SUMMER2014

c.execute("INSERT INTO Hires VALUES(900000000, 'CS', 4400, 11, 'SUMMER2014', 'W', 600000000)")

c.execute("INSERT INTO Hires VALUES(110000000, 'CS', 4400, 9, 'SUMMER2014', 'W', 700000000)")

c.execute("INSERT INTO Hires VALUES(120000000, 'CS', 4400, 9, 'SUMMER2014', 'M', 700000000)")





c.execute("INSERT INTO Hires VALUES(900000000, 'MUSI', 4630, 11, 'SUMMER2014', 'F', 600000000)")

c.execute("INSERT INTO Hires VALUES(110000000, 'MUSI', 4630, 10, 'SUMMER2014', 'T', 500000000)")

c.execute("INSERT INTO Hires VALUES(120000000, 'MUSI', 4630, 10, 'SUMMER2014', 'R', 500000000)")

c.execute("INSERT INTO Hires VALUES(130000000, 'MUSI', 4630, 12, 'SUMMER2014', 'M', 800000000)")

c.execute("INSERT INTO Hires VALUES(700000000, 'MUSI', 4630, 12, 'SUMMER2014', 'W', 800000000)")



c.execute("INSERT INTO Hires VALUES(120000000, 'MATH', 3012, 16, 'SUMMER2014', 'F', 500000000)")







##Rates

c.execute("INSERT INTO Rates VALUES(700000000, 800000000, 'MUSI', 4630, 'SUMMER2014', '4', 'Good')")



c.execute("INSERT INTO Rates VALUES(120000000, 600000000, 'MUSI', 4630, 'SPRING2014', '2', 'Ehh')")

c.execute("INSERT INTO Rates VALUES(110000000, 600000000, 'CS', 2200, 'SPRING2014', '4', 'GREAT')")



c.execute("INSERT INTO Rates VALUES(110000000, 500000000, 'MUSI', 4630, 'FALL2014', '1', 'Bad')")

c.execute("INSERT INTO Rates VALUES(120000000, 500000000, 'MATH', 3012, 'SUMMER2014', '2', 'Ok')")

c.execute("INSERT INTO Rates VALUES(900000000, 500000000, 'MUSI', 4630, 'FALL2014', '3', 'Helpful')")















