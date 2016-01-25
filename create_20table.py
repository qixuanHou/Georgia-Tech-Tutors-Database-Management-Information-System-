import pymysql


db = pymysql.connect(host = "academic-mysql.cc.gatech.edu",
                     db = "cs4400_Group_51",
                     user = "cs4400_Group_51",
                     passwd = "byYHZf0a")
c = db.cursor()

try:

    c.execute("DROP TABLE Administrator")
    c.execute("DROP TABLE Professor")
    c.execute("DROP TABLE Student")
    c.execute("DROP TABLE Undergrad")
    c.execute("DROP TABLE Grad")
    c.execute("DROP TABLE Tutor")
    c.execute("DROP TABLE Course")
    c.execute("DROP TABLE TutorTimeSlots")
    c.execute("DROP TABLE Recommends")
    c.execute("DROP TABLE Hires")
    c.execute("DROP TABLE Rates")
    c.execute("DROP TABLE Tutors")

except:
    print("had to pass")

c.execute("CREATE TABLE Administrator (AGTID CHAR (9) PRIMARY KEY, APassword VARCHAR (20) NOT NULL);")
c.execute("CREATE TABLE Professor (PGTID CHAR (9) PRIMARY KEY, PPassword VARCHAR (20) NOT NULL);")
c.execute("CREATE TABLE Student (SGTID CHAR (9) PRIMARY KEY, SPassword VARCHAR (20) NOT NULL, FName VARCHAR (20) NOT NULL, LName VARCHAR(20) NOT NULL, Email VARCHAR (20) UNIQUE);")
c.execute("CREATE TABLE Undergrad (UGTID CHAR (9) PRIMARY KEY, FOREIGN KEY (UGTID) REFERENCES Student(SGTID));")
c.execute("CREATE TABLE Grad (GGTID CHAR (9) PRIMARY KEY, FOREIGN KEY (GGTID) REFERENCES Student(SGTID));")
c.execute("CREATE TABLE Tutor (TGTID CHAR(9) PRIMARY KEY, Phone CHAR(10) NOT NULL, GPA DECIMAL(3,2) NOT NULL CHECK (GPA >= 3.00), FOREIGN KEY (TGTID) REFERENCES Student(SGTID));")
c.execute("CREATE TABLE Course (School VARCHAR (4) NOT NULL, Number CHAR (4) NOT NULL, PRIMARY KEY (School, Number));")
c.execute("CREATE TABLE TutorTimeSlots (TSGTID CHAR (9) NOT NULL, Time VARCHAR(2) NOT NULL, Semester VARCHAR (11) NOT NULL, Weekday CHAR (1) NOT NULL, PRIMARY KEY (TSGTID, Time, Semester, Weekday), FOREIGN KEY (TSGTID) REFERENCES Tutor(TGTID));")
c.execute("CREATE TABLE Recommends (PRGTID CHAR (9) NOT NULL, TRGTID CHAR (9) NOT NULL, RNumEvaluation INT CHECK (RNumEvaluation >0 AND RNumEvaluation <5), RDescEvaluation VARCHAR (200), PRIMARY KEY (PRGTID, TRGTID), FOREIGN KEY (PRGTID) REFERENCES Professor(PGTID), FOREIGN KEY (TRGTID) REFERENCES Tutor(TGTID));")
c.execute("CREATE TABLE Hires (UHGTID CHAR(9) NOT NULL, HSchool VARCHAR(4) NOT NULL, HNumber CHAR(4) NOT NULL, HTime VARCHAR(2) NOT NULL, HSemester VARCHAR(11) NOT NULL, HWeekday CHAR(1) NOT NULL, THGTID CHAR(9) NOT NULL, PRIMARY KEY (HTime, HSemester, HWeeKday, THGTID), FOREIGN KEY (UHGTID) REFERENCES Undergrad(UGTID), FOREIGN KEY (HSchool) REFERENCES Course(School), FOREIGN KEY (HNumber) REFERENCES Course (Number), FOREIGN KEY (HTime) REFERENCES TutorTimeSlots (Time), FOREIGN KEY (HSemester) REFERENCES TutorTimeSlots(Semester), FOREIGN KEY (HWeekday) REFERENCES TutorTimeSlots(Weekday), FOREIGN KEY (THGTID) REFERENCES Tutor(TGTID));")
c.execute("CREATE TABLE Rates (UAGTID CHAR(9) NOT NULL, TAGTID CHAR(9) NOT NULL, ASchool VARCHAR(4) NOT NULL, ANumber CHAR(4) NOT NULL, ASemester VARCHAR(11) NOT NULL, ANumEvaluation  INT NOT NULL CHECK (RNumEvaluation >0 AND RNumEvaluation <5), ADescEvaluation VARCHAR (50) NOT NULL, PRIMARY KEY (UAGTID, TAGTID, ASchool, ANumber), FOREIGN KEY (UAGTID) REFERENCES Undergrad (UGTID), FOREIGN KEY (TAGTID) REFERENCES Tutor (TGTID), FOREIGN KEY (ASchool) REFERENCES Course (School), FOREIGN KEY (ANumber) REFERENCES Course (Number));")
c.execute("CREATE TABLE Tutors (TTGTID CHAR(9) NOT NULL, GTA BOOLEAN NOT NULL, TSchool VARCHAR(4) NOT NULL, TNumber CHAR(4) NOT NULL, PRIMARY KEY (TTGTID, TSchool, TNumber), FOREIGN KEY (TTGTID) REFERENCES Tutor (TGTID), FOREIGN KEY (TSchool) REFERENCES Course (School), FOREIGN KEY (TNumber) REFERENCES Course (Number));")

