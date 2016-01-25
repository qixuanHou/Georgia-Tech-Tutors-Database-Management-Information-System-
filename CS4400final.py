#CS 4400
#Group 51
#Ryan Youngblood
#April Hsieh
#Qixuan Hou
#Qiran Zhu


from tkinter import *
import pymysql
import urllib.request

class CS4400database:

    def __init__(self,win):
        self.LoginPage(win)
        self.win = win
        self.x = 0
        self.value = IntVar()
        self.fall = IntVar()
        self.spring = IntVar()
        self.summer = IntVar()
                
        self.searcht = Toplevel()
        self.searcht.withdraw()
        self.searcht.title("Search/schedule tutor")
        self.schedulet = Toplevel()
        self.schedulet.withdraw()
    


    def LoginPage(self, win):

        url = "http://content.sportslogos.net/logos/31/690/thumbs/2491.gif"
        response = urllib.request.urlopen(url)
        pic = response.read()
        import base64
        b64_data = base64.encodebytes(pic)
        self.photologin = PhotoImage(data=b64_data)
        self.label = Label(win, image = self.photologin)
        self.label.grid(row = 0, column = 3, sticky = W )
        self.empty = Label(win, text = "")
        self.empty.grid(row=1)
        
        win.title("Login")
        self.label1 = Label(win, text = "Username")
        self.label2 = Label(win, text = "Password")
        self.entry = Entry(win, width = 30, state = NORMAL)
        self.entry1 = Entry(win, width = 30, state = NORMAL)
        self.button1 = Button(win, text = "Okay", command = self.LoginCheck)
        self.emptylabel = Label(win, text = "")

        self.label1.grid(row = 3, column = 0)
        self.label2.grid(row = 4, column = 0)
        self.entry.grid(row = 3, column =1, columnspan = 3, sticky = W)
        self.entry1.grid(row = 4, column = 1, columnspan = 3, sticky = W)
        self.emptylabel.grid(row = 5)
        self.button1.grid(row = 6, column = 4)
        
    





    def BacktoLogin(self):
        self.rootwin.withdraw()
        self.win.deiconify()
        
        
    def Connect(self):
        try:
            self.database = pymysql.connect(host = "academic-mysql.cc.gatech.edu", passwd = "byYHZf0a", user = "cs4400_Group_51", db = 'cs4400_Group_51')
            return(self.database)
        except:
            messagebox.showerror("Error","Check Internet Connection!")

    

    def LoginCheck(self):
        login = 0
        while login == 0:
            
            self.database = self.Connect()
            self.cursor = self.database.cursor()
            username = self.entry.get()
            self.usename = username
            password = self.entry1.get()
            SQL = "SELECT * FROM Administrator Where AGTID = %s and APassword = %s"
            self.cursor.execute(SQL ,(username, password))
            self.admin = []
            for x in self.cursor:
                self.admin.append(x)
            if len(self.admin) == 0:
                SQL = "SELECT * FROM Professor Where PGTID = %s and PPassword = %s"
                self.cursor.execute(SQL ,(username, password))
                self.professor = []
                for x in self.cursor:
                    self.professor.append(x)
                    
                if len(self.professor) == 0:
                    SQL = "SELECT * FROM Student Where SGTID = %s and SPassword = %s"
                    self.cursor.execute(SQL ,(username, password))
                    self.student = []
                    for x in self.cursor:
                        self.student.append(x)
                    if len(self.student) == 0:
                        messagebox.showerror("Error", "Username/Password combination not recognized!")
                        login = 1
                    else:
                        SQL = "SELECT * FROM Tutor WHERE TGTID = %s"
                        self.cursor.execute(SQL, (username))
                        self.tutor = []
                        for x in self.cursor:
                            self.tutor.append(x)
                        if len(self.tutor) == 0:
                            
                            messagebox.showinfo("Congratulations!", "Student " + username +" is successfully logged in")
                            self.win.withdraw()
                            self.x = 0
                            self.usernametype =0
                            self.Homepage()
                            login = 1
                        else:
                            messagebox.showinfo("Congratulations", "Tutor " + username + " is successfully logged in")
                            self.win.withdraw()
                            self.x = 0
                            self.usernametype =1
                            self.Homepage()
                            login = 1
                else:
                    messagebox.showinfo("Congratulations!", "Professor " + username +" is successfully logged in")
                    self.win.withdraw()
                    self.x = 0
                    self.usernametype = 3
                    self.Homepage()
                    login = 1
                        
            else:
                messagebox.showinfo("Congratulations!", "Administrator " + username +" is successfully logged in")
                self.win.withdraw()
                self.x = 0
                self.usernametype =2
                self.Homepage()
                login = 1

        self.database.commit()

    def Homepage(self):
        print(self.usernametype)
        self.thirdwin = Toplevel()

        
        self.thirdwin.title("Main Menu")
        lab = Label(self.thirdwin, text = "Academic Year 2014")
        lab.grid(row = 0, columnspan = 3, sticky = E+W)
        empty = Label(self.thirdwin, text = "")
        empty.grid(row =1, column = 0 , sticky = E)
        empty2 = Label(self.thirdwin, text = "          ")
        empty2.grid(row =1, column = 1)



        if self.usernametype == 0:
            label = Label(self.thirdwin, text = "Student Options")
            label.grid(row = 2 , column = 0, columnspan = 3, sticky = W)
            button3 = Button(self.thirdwin, text = "Rate a Tutor", command = self.ratesatutor )
            button3.grid(row = 4, column = 2, sticky = W)
            button4 =Button(self.thirdwin, text = "Search/Schedule Tutor", command = self.searchtutorpage)
            button4.grid(row = 4, column = 0, sticky = W)
            empty1 = Label(self.thirdwin, text = "")
            empty1.grid(row = 3)
        if self.usernametype == 1:
            label1 = Label(self.thirdwin, text = "Tutor Options")
            label1.grid(row = 5, column = 0, columnspan = 3, sticky = W)
            empty3 = Label(self.thirdwin, text = "")
            empty3.grid(row=6)
            button = Button(self.thirdwin, text = "Apply", command = self.tutorApplies)
            button.grid(row = 7, column = 0, sticky = W)
            button5 =Button(self.thirdwin, text = "Find My Schedule", command = self.findTutorSchedule)
            button5.grid(row = 7, column = 2, sticky = W)
        if self.usernametype == 2:
            labelad = Label(self.thirdwin, text = "Administrator Options")
            labelad.grid(row = 11, column = 0, columnspan = 3 ,sticky = W)
            empty5 =Label(self.thirdwin, text = "")
            empty5.grid(row=12)
            button2 = Button(self.thirdwin, text = "Summary 1", command = self.adminsummaryreport1)
            button2.grid(row = 13, column = 0, sticky = W)
            button6 = Button(self.thirdwin, text = "Summary 2", command = self.adminsummaryreport2)
            button6.grid(row = 13, column = 2, sticky = W)
        if self.usernametype == 3:
            label2 = Label(self.thirdwin, text = "Professor Options")
            label2.grid(row = 8, column = 0, columnspan = 3, sticky = W)
            empty4 =Label(self.thirdwin, text = "")
            empty4.grid(row = 9)
            button1 = Button(self.thirdwin, text = "Add Recommendation", command = self.recommendatutor)
            button1.grid(row = 10, column = 0,  sticky = W)
            


        emptyforlogexit = Label(self.thirdwin, text = "")
        emptyforlogexit.grid(row = 14)
        self.logoutbutton = Button(self.thirdwin, text = "logout", command = self.logout)
        self.logoutbutton.grid(row = 15, column = 1, sticky = W)
        button10 = Button(self.thirdwin, text = "Exit", command= self.homepagehelper )
        button10.grid(row = 15, column = 0, sticky = E)

        #Check to make sure the views work


    def homepagehelper(self):
        self.win.destroy()

    def logout(self):
        self.thirdwin.destroy()
        self.win.deiconify()




    def recommendatutor(self):
        self.thirdwin.withdraw()
        self.eightwin = Toplevel()
        self.values = IntVar()
        self.values.set(5)


        self.eightwin.title("Professor Recommendation")
        label1 = Label(self.eightwin, text = "Student GTID")
        label3 = Label(self.eightwin, text  = "Descriptive Evaluation")
        label4 = Label(self.eightwin, text  = "Numeric Evaluation")
        button = Button(self.eightwin, text = "Okay", command = self.recommendtutorhelper)

        empty = Label(self.eightwin, text = "     ")

        
        self.entrytutorids = Entry(self.eightwin, width = 9, state = NORMAL)
        self.entrydesc1 = Entry(self.eightwin, width = 120,  state = NORMAL)

        button1 = Button(self.eightwin, text = "Back", command = self.recommendatutorback)
        button1.grid(row = 12, column = 2)
        

        radio4 = Radiobutton(self.eightwin, text = "4 Highly Recommend", variable = self.values, value = 4)
        radio3 = Radiobutton(self.eightwin, text = "3 Recommend", variable = self.values, value =3)
        radio2 = Radiobutton(self.eightwin, text = "2 Recommend with Reservation", variable = self.values, value =2)
        radio1 = Radiobutton(self.eightwin, text = "1 Do Not Recommend", variable = self.values, value =1 )

        label1.grid(row = 0, column = 0)
        self.entrytutorids.grid(row = 0, column = 1)
        empty.grid(row = 0, column = 3)
        label3.grid(row = 2, column = 0, columnspan = 2)
        self.entrydesc1.grid(row = 4, column = 0, columnspan =6)
        label4.grid(row = 6, column = 0, columnspan = 2)

        
        radio4.grid(row = 8, column = 0 , columnspan = 3, sticky = W)
        radio3.grid(row = 9, column=  0 , columnspan = 3, sticky = W)
        radio2.grid(row = 10, column= 0 , columnspan = 3, sticky = W)
        radio1.grid(row = 11, column= 0 , columnspan = 3, sticky = W)

        button.grid(row = 12, column = 1)

    def recommendatutorback(self):
        self.thirdwin.deiconify()
        self.eightwin.destroy()
        
        

    def recommendtutorhelper(self):

        value = self.values.get()
        if value == 5:
            messagebox.showerror("Error" , "Please pick a numeric evaluation")
            return
        entrydesc1 = self.entrydesc1.get()
        entrytutorids = self.entrytutorids.get()



        if entrytutorids == "" or entrydesc1 == "":
            messagebox.showerror("Error", "Please fill in all fields")

        elif len(entrytutorids) != 9:
            messagebox.showerror("Error", "Student GTID must be 9 digits")

        else:
            
            sql = "SELECT TGTID FROM Tutor Where TGTID = %s "
            self.cursor.execute(sql, (entrytutorids))
            self.tutorgtid = []
            for item in self.cursor:
                self.tutorgtid.append(item)
            if len(self.tutorgtid) > 0:

                try:

                    sql2 = "Insert into Recommends values (%s, %s, %s, %s)"
                    self.cursor.execute(sql2, (self.usename, entrytutorids,value, entrydesc1 ))
                    self.database.commit()
                    messagebox.showerror("Congratulations!", "Data has been successfully entered into the database")

                except:
                    try:

                        messagebox.showerror("Note",  "Previous recommendation will been replaced by the new one")#edit the wording of this late

                        sqlupdate = "update Recommends set RNumEvaluation = %s , RDescEvaluation = %s where PRGTID = %s and TRGTID = %s"
                        self.cursor.execute(sqlupdate, (value, entrydesc1, self.usename, entrytutorids))
                        self.database.commit()
                        messagebox.showerror("Congratulations!", "Data has been successfully entered into the database")
                        


                    except:
                        messagebox.showerror("Error", "Recommendation could not be entered into the Database")
                    
            else:
                messagebox.showerror("Error", "Please enter a valid tutor gtid")
                
            




    def ratesatutor(self):
        self.thirdwin.withdraw()
        self.secondwin = Toplevel()
        self.value.set(0)


        self.secondwin.title("Tutor Evaluation by Student")
        label1 = Label(self.secondwin, text = "Course")
        label1a = Label(self.secondwin, text = "School")
        label1b = Label(self.secondwin, text = "Number")
        label2 = Label(self.secondwin, text  = "Tutor Name")
        label3 = Label(self.secondwin, text  = "Descriptive Evaluation")
        label4 = Label(self.secondwin, text  = "Numeric Evaluation")
        button = Button(self.secondwin, text = "Okay", command = self.rateatutorhelper)
        buttonexit = Button(self.secondwin, text = "Back", command = self.ratesatutorback)

        empty = Label(self.secondwin, text = "     ")


        self.cursor.execute("SELECT * FROM Course")
        courses = []
        for x in self.cursor:
            courses.append(str(x[0])+" "+str(x[1]))     
        self.courseVar = StringVar(self.secondwin)
        OptionMenu(self.secondwin, self.courseVar,*courses).grid(row=1,column=1,columnspan=2,sticky=EW)


        self.entrytutor = Entry(self.secondwin, width = 30, state = NORMAL)
        self.entrydesc = Entry(self.secondwin, width = 120,  state = NORMAL)
        

        radio4 = Radiobutton(self.secondwin, text = "4 Highly Recommend", variable = self.value, value = 4)
        radio3 = Radiobutton(self.secondwin, text = "3 Recommend", variable = self.value, value =3)
        radio2 = Radiobutton(self.secondwin, text = "2 Recommend with Reservation", variable = self.value, value =2)
        radio1 = Radiobutton(self.secondwin, text = "1 Do Not Recommend", variable = self.value, value =1 )

        label1.grid(row = 0, column = 0, rowspan = 2)
        label1a.grid(row = 0, column = 1 )
        label1b.grid(row = 0, column = 2)
        empty.grid(row = 0, column = 3)
        label2.grid(row = 0 , column = 4)
        self.entrytutor.grid(row = 0, column = 5)
        label3.grid(row = 3, column = 0, columnspan = 2)
        self.entrydesc.grid(row = 5, column = 0, columnspan =6)
        label4.grid(row = 7, column = 0, columnspan = 2)

        
        radio4.grid(row = 9, column = 0 , columnspan = 3, sticky = W)
        radio3.grid(row = 10, column=  0 , columnspan = 3, sticky = W)
        radio2.grid(row = 11, column= 0 , columnspan = 3, sticky = W)
        radio1.grid(row = 12, column= 0 , columnspan = 3, sticky = W)

        button.grid(row = 13, column = 0)
        buttonexit.grid(row = 13, column = 1)

    def ratesatutorback(self):
        self.thirdwin.deiconify()
        self.secondwin.destroy()
        
        

    def rateatutorhelper(self):

        entrydesc = self.entrydesc.get()
        entrytutor = self.entrytutor.get()

        tutor = entrytutor.split(" ")

        value = self.value.get()


        if value == 0 or self.courseVar.get()=="" or entrydesc == "":
            messagebox.showerror("Error", "Please fill in all fields")

        elif len(tutor) < 2:
            messagebox.showerror("Error", "Please fill in first and last name of tutor seperated by a space")

        else:
            try:
                sql = "SELECT  SGTID FROM Student WHERE FName = %s and LName = %s"
                self.cursor.execute(sql, (tutor[0],tutor[1]))
                self.tutorgtid = []
                for item in self.cursor:
                    self.tutorgtid.append(item)

                a = self.courseVar.get()
                b=a.split(" ")


                sqlstatement = "Select * From Hires where UHGTID = %s and HSchool = %s and HNumber = %s and HSemester = %s and THGTID = %s"
                self.cursor.execute(sqlstatement, (self.usename, b[0], b[1], 'SUMMER2014', self.tutorgtid[0]))
                self.tryit = []
                for item in self.cursor:
                    self.tryit.append(item)

                print(self.tryit)

                if len(self.tryit) == 0:
                    messagebox.showerror("Error", "You have to have this tutor for this class during the current semester")
                    return

                else:
                
                    try:
                        try:
                            sql2 = ("Insert into Rates values (%s, %s, %s, %s, %s, %s, %s)")
                            self.cursor.execute(sql2, (self.usename, self.tutorgtid[0], b[0], b[1], 'SUMMER2014',  value, entrydesc))
                            self.database.commit()
                            messagebox.showerror("Congrats","Your evaluation was successfully sent!")

                        except:
                             try:

                                messagebox.showerror("Note",  "Previous Rating will been replaced by the new one")#edit the wording of this late

                                sqlupdate = "update Rates set ANumEvaluation = %s , ADescEvaluation = %s where UAGTID= %s and TAGTID= %s and ASchool = %s and ANumber = %s and ASemester = %s"  
                                self.cursor.execute(sqlupdate, (value, entrydesc, self.usename, self.tutorgtid[0], b[0], b[1], "SUMMER2014"))
                                self.database.commit()
                                messagebox.showerror("Congratulations!", "Data has been successfully entered into the database")
                                


                             except:
                                messagebox.showerror("Error", "Rating could not be entered into the Database")
                            



                    except:
                        messagebox.showerror("Error",  "Rating could not enter data into the database") #edit the wording of this later
            except:
                messagebox.showerror("Error", "Please enter a valid tutor name")
                
    def adminsummaryreport1(self):
        self.fourthwin = Toplevel()
        self.thirdwin.withdraw()
        self.fall.set(0)
        self.spring.set(0)
        self.summer.set(0)
    

        self.fourthwin.title("List of Courses with Student/Tutor Summary Data")

        label = Label(self.fourthwin, text = "Academic Year 2014")
        radiobutton = Radiobutton(self.fourthwin, text = "Fall", variable = self.fall, value = 1)
        radiobutton1 =  Radiobutton(self.fourthwin, text = "Spring", variable = self.spring, value = 1)
        radiobutton2 =  Radiobutton(self.fourthwin, text = "Summer", variable = self.summer, value = 1)
        button = Button(self.fourthwin, text = "Okay", command = self.adminsummreporthelper)
        button2 = Button(self.fourthwin, text = "Okay", command = self.backtohomepage)

        label.grid(row = 0, column = 0, columnspan = 2)
        radiobutton.grid(row = 0, column =2)
        radiobutton1.grid(row = 0, column = 3)
        radiobutton2.grid(row = 0, column =4)
        button.grid(row = 0 , column = 5)
        button2.grid(row = 100)

        
       

    def backtohomepage(self):
        self.thirdwin.deiconify()
        self.fourthwin.destroy()
        

        
    def adminsummreporthelper(self):

    
        
        course = Label(self.fourthwin, text = "Course")
        semester = Label(self.fourthwin, text = "Semester")
        students = Label(self.fourthwin, text = "# Students")
        tutors = Label(self.fourthwin, text = "# Tutors")
        course.grid(row = 1, column = 0, sticky = E+W)
        semester.grid(row = 1, column = 1, sticky = E+W)
        students.grid(row = 1, column = 2, sticky = E+W)
        tutors.grid(row = 1, column = 3, sticky = E+W)
        
        fall = self.fall.get()
        spring = self.spring.get()
        summer = self.summer.get()


        if fall == 0 and spring == 0 and summer == 0:
            messagebox.showerror("Error", "Please select atleast one semester")

        else:

            semester = ""
            semestercount = 0
            if fall == 0:
                pass
            elif fall != 0 :
                semester = semester + "(FALL2014"
                semestercount = 1
                
            if spring == 0:
                pass
            elif spring == 1:
                if semestercount == 1:
                    semester = semester +" or SPRING2014"
                if semestercount == 0:
                    semester = semester + "(SPRING2014"

            if summer == 0:
                pass
            elif summer == 1:
                if semestercount == 1:
                    semester = semester + " or SUMMER2014"
                elif semestercount == 0:
                    semester = semester + "(SUMMER2014"
            semester = semester + ")"
        
                
            
        biglist = []

        sql = "Select * From Course"
        self.cursor.execute(sql)
        coursenumlist = []
        for item in self.cursor:
            coursenumlist.append(item)
        
        iteratorforgui = 2

        coursenumlist.sort()

        grandtotalstudents = 0
        grandtotaltutors = 0
            

        for item in coursenumlist:
            totalstudents = 0
            totaltutors = 0

            listfall = []
            listspring = []
            listsummer = []
            x = item[:]

            if fall != 0:
                fallsql = "Select Count( distinct UHGTID), Count(distinct THGTID) From Hires Where HSchool = %s and  HNumber = %s  and HSemester = %s"
                self.cursor.execute(fallsql, (x[0], x[1], "FALL2014"))
                for item in self.cursor:
                    listfall.append(item)
                                                   
            if spring != 0:
                springsql = "Select Count(distinct UHGTID), Count(distinct THGTID) From Hires Where HSchool = %s and  HNumber = %s  and HSemester = %s"
                self.cursor.execute(springsql, (x[0], x[1], "SPRING2014"))
                for item in self.cursor:
                    listspring.append(item)

            if summer != 0:
                summersql = "Select Count(distinct UHGTID), Count(distinct THGTID) From Hires Where HSchool = %s and  HNumber = %s  and HSemester = %s"
                self.cursor.execute(summersql, (x[0], x[1], "SUMMER2014"))
                for item in self.cursor:
                    listsummer.append(item)
                


            if fall != 0:
                biglist.append((x[0]  + " " + x[1], "fall", listfall[0][0], listfall[0][1]))
                totalstudents = totalstudents + listfall[0][0]
                totaltutors = totaltutors +  listfall[0][1]
            if spring !=0 and fall != 0:
                biglist.append((" ", "spring", listspring[0][0], listspring[0][1]))
                totalstudents = totalstudents + listspring[0][0]
                totaltutors = totaltutors +  listspring[0][1]
            if spring !=0 and fall == 0:
                biglist.append((x[0]  + " " + x[1], "spring", listspring[0][0], listspring[0][1]))
                totalstudents = totalstudents + listspring[0][0]
                totaltutors = totaltutors +  listspring[0][1]
            if summer != 0 and (fall != 0 or spring != 0):
                biglist.append(("" , "summer", listsummer[0][0], listsummer[0][1]))
                totalstudents = totalstudents + listsummer[0][0]
                totaltutors = totaltutors +  listsummer[0][1]
            if summer != 0 and fall ==0 and spring == 0:
                biglist.append((x[0]  + " " + x[1], "summer", listsummer[0][0], listsummer[0][1]))
                totalstudents = totalstudents + listsummer[0][0]
                totaltutors = totaltutors +  listsummer[0][1]

            biglist.append(( "", "Total", totalstudents, totaltutors))
            grandtotalstudents = grandtotalstudents + totalstudents
            grandtotaltutors = grandtotaltutors + totaltutors
            
        biglist.append((" ", "Grand Total", grandtotalstudents, grandtotaltutors))

        for items in biglist:
            counter = 0
            for item in items:
                Label(self.fourthwin, text = item).grid(row = iteratorforgui, column = counter)
                counter = counter + 1
            iteratorforgui = iteratorforgui + 1



    def adminsummaryreport2(self):
            self.thirdwin.withdraw()
            self.tenthwin = Toplevel()
            self.fall.set(0)
            self.spring.set(0)
            self.summer.set(0)
        

            self.tenthwin.title("Tutor Summary Data for Grad TAs/nonTAs current Academic Year")

            label = Label(self.tenthwin, text = "Academic Year 2014")
            radiobutton = Radiobutton(self.tenthwin, text = "Fall", variable = self.fall, value = 1)
            radiobutton1 =  Radiobutton(self.tenthwin, text = "Spring", variable = self.spring, value = 1)
            radiobutton2 =  Radiobutton(self.tenthwin, text = "Summer", variable = self.summer, value = 1)
            button = Button(self.tenthwin, text = "Okay", command = self.adminsummreporthelper2)
            button2 = Button(self.tenthwin, text = "Okay", command = self.backtohomepage2)

            label.grid(row = 0, column = 0, columnspan = 2)
            radiobutton.grid(row = 0, column =2)
            radiobutton1.grid(row = 0, column = 3)
            radiobutton2.grid(row = 0, column =4)
            button.grid(row = 0 , column = 5)
            button2.grid(row = 100)


    def backtohomepage2(self):
            self.thirdwin.deiconify()
            self.tenthwin.destroy()


    def adminsummreporthelper2(self):


        
        course = Label(self.tenthwin, text = "Course")
        semester = Label(self.tenthwin, text = "Semester")
        students = Label(self.tenthwin, text = "TA")
        tutors = Label(self.tenthwin, text = "Avg Rating")
        nonta = Label(self.tenthwin, text = "non TA")
        avgrating = Label(self.tenthwin, text = "Avg Rating")
        course.grid(row = 1, column = 0, sticky = E+W)
        semester.grid(row = 1, column = 1, sticky = E+W)
        students.grid(row = 1, column = 2, sticky = E+W)
        tutors.grid(row = 1, column = 3, sticky = E+W)
        nonta.grid(row = 1, column = 4, sticky = E+W)
        avgrating.grid(row =1, column = 5, sticky = E+W)
        
        fall = self.fall.get()
        spring = self.spring.get()
        summer = self.summer.get()


        if fall == 0 and spring == 0 and summer == 0:
            messagebox.showerror("Error", "Please select atleast one semester")
        
                
            
        biglist = []

        sql = "Select * From Course"
        self.cursor.execute(sql)
        coursenumlist = []
        for item in self.cursor:
            coursenumlist.append(item)
        
        iteratorforgui = 2

        coursenumlist.sort()


        gradavglist = []
        ugavglist = []
        gradavgbig = 0
        ugradavgbig = 0

        for item in coursenumlist:

            varg = []
            varu = []
            gradx = 0
            ugrady = 0

            listfallnongt = []
            listspringnongt = []
            listsummernongt = []
            listfallgt = []
            listspringgt = []
            listsummergt = []
            listfallGTrate = []
            listfallTArate = []
            listspringGTrate = []
            listspringTArate = []
            listsummerGTrate = []
            listsummerTArate =[]
            x = item[:]

            if fall != 0:
                fallsql = "Select distinct THGTID From Hires , Undergrad Where HSchool = %s and  HNumber = %s  and HSemester = %s and UGTID = THGTID"
                self.cursor.execute(fallsql, (x[0], x[1], "FALL2014"))
                for item in self.cursor: 
                    listfallnongt.append(item)

                print("Fall non GT = ", listfallnongt)
                    
                fallsqlta = "Select distinct THGTID From Hires, Grad Where Hschool = %s and Hnumber = %s and HSemester  = %s and THGTID = GGTID"
                self.cursor.execute(fallsqlta, (x[0], x[1], "FALL2014"))
                for item in self.cursor:
                    listfallgt.append(item)

                print("Fall GT =  ", listfallgt)


                fallcountnongt = int(len(listfallnongt))
                fallcountgt = int(len(listfallgt))
                
                nongtlist = ""
                for item in listfallnongt:
                    nongtlist = nongtlist + item[0] + " or TAGTID = "

                nongtlist = nongtlist[:-13]
                


                gtlist = ""
                for item in listfallgt:
                    gtlist = gtlist + item[0] + " or TAGTID = " 

                gtlist = gtlist[:-13]


                
                try:
                    avgofnongt = []
                    nongtavgsql = "Select Avg(ANumEvaluation) from Rates where TAGTID = " + nongtlist
                    self.cursor.execute(nongtavgsql)
                    for newitem in self.cursor:
                        avgofnongt.append(newitem)

                        
                    try:

                        fallavgofnongtactual = float(avgofnongt[0][0])
                        ugavglist.append(fallavgofnongtactual)
                        varu.append(fallavgofnongtactual)
                    except:
                        fallavgofnongtactual = 0
                        ugavglist.append(fallavgofnongtactual)
                        varu.append(fallavgofnongtactual)
                except:
                    fallavgofnongtactual = 0
                    ugavglist.append(fallavgofnongtactual)
                    varu.append(fallavgofnongtactual)

                try:

                    avgofgt = []

                    gtavgsql = "Select Avg(ANumEvaluation) from Rates where TAGTID = " +gtlist
                    self.cursor.execute(gtavgsql)
                    for item in self.cursor:
                        avgofgt.append(item)

                    try:

                        fallavgofgtactual = float(avgofgt[0][0])
                        gradavglist.append(fallavgofgtactual)
                        varg.append(fallavgofgtactual)
                        

                    except:

                        fallavgofgtactual = 0
                        gradavglist.append(fallavgofgtactual)
                        varg.append(fallavgofgtactual)
                except:
                    fallavgofgtactual = 0
                    gradavglist.append(fallavgofgtactual)
                    varg.append(fallavgofgtactual)
                    

            if spring != 0:
                springsql = "Select distinct THGTID From Hires , Undergrad Where HSchool = %s and  HNumber = %s  and HSemester = %s and UGTID = THGTID"
                self.cursor.execute(springsql, (x[0], x[1], "SPRING2014"))
                for item in self.cursor: 
                    listspringnongt.append(item)

                print("Spring non GT = ", listspringnongt)
                    
                springsqlta = "Select distinct THGTID From Hires, Grad Where Hschool = %s and Hnumber = %s and HSemester  = %s and THGTID = GGTID"
                self.cursor.execute(springsqlta, (x[0], x[1], "SPRING2014"))
                for item in self.cursor:
                    listspringgt.append(item)

                print("Spring GT = ", listspringgt)

                springcountnongt = int(len(listspringnongt))
                springcountgt = int(len(listspringgt))
                
                nongtlist = ""
                for item in listspringnongt:
                    nongtlist = nongtlist + item[0] + " or TAGTID = "

                nongtlist = nongtlist[:-13]
                


                gtlist = ""
                for item in listspringgt:
                    gtlist = gtlist + item[0] + " or TAGTID = " 

                gtlist = gtlist[:-13]



                
                try:
                    avgofnongt = []
                    nongtavgsql = "Select Avg(ANumEvaluation) from Rates where TAGTID = " + nongtlist

                    self.cursor.execute(nongtavgsql)
                    for newitem in self.cursor:
                        avgofnongt.append(newitem)

                        
                    try:


                        springavgofnongtactual = float(avgofnongt[0][0])
                        ugavglist.append(springavgofnongtactual)
                        varu.append(springavgofnongtactual)
                    except:
                        springavgofnongtactual = 0
                        ugavglist.append(springavgofnongtactual)
                        varu.append(springavgofnongtactual)
                except:
                    springavgofnongtactual = 0
                    ugavglist.append(springavgofnongtactual)
                    varu.append(springavgofnongtactual)

                try:

                    avgofgt = []

                    gtavgsql = "Select Avg(ANumEvaluation) from Rates where TAGTID = " +gtlist
                    self.cursor.execute(gtavgsql)
                    for item in self.cursor:
                        avgofgt.append(item)

                    try:
   

                        springavgofgtactual = float(avgofgt[0][0])
                        gradavglist.append(springavgofgtactual)
                        varg.append(springavgofgtactual)
                        

                    except:

                        springavgofgtactual = 0
                        gradavglist.append(springavgofgtactual)
                        varg.append(springavgofgtactual)
                except:
                    springavgofgtactual = 0
                    gradavglist.append(springavgofgtactual)
                    varg.append(springavgofgtactual)
                    

            if summer!= 0:
                summersql = "Select distinct THGTID From Hires , Undergrad Where HSchool = %s and  HNumber = %s  and HSemester = %s and UGTID = THGTID"
                self.cursor.execute(summersql, (x[0], x[1], "SUMMER2014"))
                for item in self.cursor: 
                    listsummernongt.append(item)

                print("Summer non GT = ", listsummernongt)
                    
                summersqlta = "Select distinct THGTID From Hires, Grad Where Hschool = %s and Hnumber = %s and HSemester  = %s and THGTID = GGTID"
                self.cursor.execute(summersqlta, (x[0], x[1], "SUMMER2014"))
                for item in self.cursor:
                    listsummergt.append(item)

                print("Summer GT = ", listsummergt)

                summercountnongt = int(len(listsummernongt))
                summercountgt = int(len(listsummergt))
                
                nongtlist = ""
                for item in listsummernongt:
                    nongtlist = nongtlist + item[0] + " or TAGTID = "

                nongtlist = nongtlist[:-13]
                


                gtlist = ""
                for item in listsummergt:
                    gtlist = gtlist + item[0] + " or TAGTID = " 

                gtlist = gtlist[:-13]



                
                try:
                    avgofnongt = []
                    nongtavgsql = "Select Avg(ANumEvaluation) from Rates where TAGTID = " + nongtlist
                    self.cursor.execute(nongtavgsql)
                    for newitem in self.cursor:
                        avgofnongt.append(newitem)

                        
                    try:
                

                        summeravgofnongtactual = float(avgofnongt[0][0])
                        ugavglist.append(summeravgofnongtactual)
                        varu.append(summeravgofnongtactual)
                    except:
                        summeravgofnongtactual = 0
                        ugavglist.append(summeravgofnongtactual)
                        varu.append(summeravgofnongtactual)
                except:
                    summeravgofnongtactual = 0
                    ugavglist.append(summeravgofnongtactual)
                    varu.append(summeravgofnongtactual)

                try:

                    avgofgt = []

                    gtavgsql = "Select Avg(ANumEvaluation) from Rates where TAGTID = " +gtlist
                    self.cursor.execute(gtavgsql)
                    for item in self.cursor:
                        avgofgt.append(item)

                    try:
       

                        summeravgofgtactual = float(avgofgt[0][0])
                        gradavglist.append(summeravgofgtactual)
                        varg.append(summeravgofgtactual)
                        

                    except:

                        summeravgofgtactual = 0
                        gradavglist.append(summeravgofgtactual)
                        varg.append(summeravgofgtactual)
                except:
                    summeravgofgtactual = 0
                    gradavglist.append(summeravgofgtactual)
                    varg.append(summeravgofgtactual)
                
            
                


                
            
                


            if fall != 0:
                biglist.append((x[0]  + " " + x[1], "fall", fallcountgt, fallavgofgtactual, fallcountnongt, fallavgofnongtactual))
            if spring !=0 and fall != 0:
                biglist.append((" ", "spring", springcountgt, springavgofgtactual, springcountnongt, springavgofnongtactual))
            if spring !=0 and fall == 0:
                biglist.append((x[0]  + " " + x[1], "spring", springcountgt, springavgofgtactual, springcountnongt, springavgofnongtactual))
            if summer != 0 and (fall != 0 or spring != 0):
                biglist.append(("" , "summer", summercountgt, summeravgofgtactual, summercountnongt, summeravgofnongtactual))
            if summer != 0 and fall ==0 and spring == 0:
                biglist.append((x[0]  + " " + x[1], "summer", summercountgt, summeravgofgtactual, summercountnongt, summeravgofnongtactual))

            if len(varg) == 0:
                gradx = 0
            else:
                count = 0
                num = 0
                for x in varg:
                    num = num + x
                    if x != 0 :
                        count = count + 1
                if count == 0:
                    count = 1
                
                gradx = num/count
                
            if len(varu) == 0:
                ugrady = 0
            else:
                count = 0
                num = 0
                for x in varu:
                    num = num + x
                    if x != 0:
                        count = count + 1
                if count == 0:
                    count = 1
                    
                ugrady =num/count


                

            biglist.append(( "", "Avg", "", gradx,"", ugrady))


        if len(gradavglist) == 0:
            gradavgbig = 0
        else:
            count = 0
            num = 0
            for x in gradavglist:
                num = num + x
                if x != 0 :
                    count = count + 1
            if count == 0:
                count = 1
                
            gradavgbig = num/count
        if len(ugavglist) == 0:
            ugradavgbig = 0
        else:
            count = 0
            num = 0
            for x in ugavglist:
                num = num + x
                if x != 0 :
                    count = count + 1
            if count == 0:
                count = 1
            ugradavgbig =num/count
            
            
            
            
        biglist.append((" ", "Total Avg", " ",gradavgbig, "",ugradavgbig))

        for items in biglist:
            counter = 0
            for item in items:
                Label(self.tenthwin, text = item).grid(row = iteratorforgui, column = counter)
                counter = counter + 1
            iteratorforgui = iteratorforgui + 1



    def findTutorSchedule(self):
        self.thirdwin.withdraw()
        self.win5 = Toplevel()
        
        studentNum = self.usename
        
        self.win5.title("Tutor Schedule")

        sql2=("SELECT HWeekday, HTime, FName, LName, Email, HSchool, HNumber FROM Hires, Student Where THGTID = %s AND UHGTID = SGTID ORDER BY HWeekday ASC")
        self.cursor.execute(sql2,(studentNum))
        tutorTimes = self.cursor.fetchall()
        
        timeListMonday = []
        timeListTuesday = []
        timeListWednesday = []
        timeListThursday = []
        timeListFriday = []
        for x in tutorTimes:
            if x[0] == "M":
                timeListMonday.append(x)
            if x[0] == "T":
                timeListTuesday.append(x)
            if x[0] == "W":
                timeListWednesday.append(x)
            if x[0] == "R":
                timeListThursday.append(x)
            if x[0] == "F":
                timeListFriday.append(x)
                
        scheduleHeader = ["Day","Time", "First Name", "Last Name", "Email", "Course", "Number"]
        y=0
        for x in scheduleHeader:
            Label(self.win5,text = x, bd=1, relief=RAISED, padx=5, pady=5).grid(column=y, row = 0)
            y=y+1
        z=1
        for x in range(len(timeListMonday)):
            cy=0
            for y in range(len(timeListMonday[x])):
                Label(self.win5,text = timeListMonday[x][y]).grid(column = cy,row=z)
                cy=cy+1
            z=z+1
        for x in range(len(timeListTuesday)):
            cy=0
            for y in range(len(timeListTuesday[x])):
                Label(self.win5,text = timeListTuesday[x][y]).grid(column = cy,row=z)
                cy=cy+1
            z=z+1
        for x in range(len(timeListWednesday)):
            cy=0
            for y in range(len(timeListWednesday[x])):
                Label(self.win5,text = timeListWednesday[x][y]).grid(column = cy,row=z)
                cy=cy+1
            z=z+1
        for x in range(len(timeListThursday)):
            cy=0
            for y in range(len(timeListThursday[x])):
                Label(self.win5,text = timeListThursday[x][y]).grid(column = cy,row=z)
                cy=cy+1
            z=z+1
        for x in range(len(timeListFriday)):
            cy=0
            for y in range(len(timeListFriday[x])):
                Label(self.win5,text = timeListFriday[x][y]).grid(column = cy,row=z)
                cy=cy+1
            z=z+1
        z=z+1
        Button(self.win5, text = "Back",command = self.backToTutorMain, relief = RAISED, pady=10).grid(row = z, column =5, columnspan=2)

    def backToTutorMain(self):
        self.win5.destroy()
        self.thirdwin.deiconify()
             
    
    def tutorApplies(self):

        self.thirdwin.withdraw()

        self.fifthwin = Toplevel()



        



        self.uorgvar = IntVar()

        self.uorgvar.set(3)





        self.m9 = IntVar()

        self.m10 = IntVar()

        self.m11 = IntVar()

        self.m12 = IntVar()

        self.m1 = IntVar()

        self.m2 = IntVar()

        self.m3 = IntVar()

        self.m4 = IntVar()



        self.t9 = IntVar()

        self.t10 = IntVar()

        self.t11 = IntVar()

        self.t12 = IntVar()

        self.t1 = IntVar()

        self.t2 = IntVar()

        self.t3 = IntVar()

        self.t4 = IntVar()



        self.w9 = IntVar()

        self.w10 = IntVar()

        self.w11 = IntVar()

        self.w12 = IntVar()

        self.w1 = IntVar()

        self.w2 = IntVar()

        self.w3 = IntVar()

        self.w4 = IntVar()



        self.th9 = IntVar()

        self.th10 = IntVar()

        self.th11 = IntVar()

        self.th12 = IntVar()

        self.th1 = IntVar()

        self.th2 = IntVar()

        self.th3 = IntVar()

        self.th4 = IntVar()



        self.f9 = IntVar()

        self.f10 = IntVar()

        self.f11 = IntVar()

        self.f12 = IntVar()

        self.f1 = IntVar()

        self.f2 = IntVar()

        self.f3 = IntVar()

        self.f4 = IntVar()



        self.m9.set(0)

        self.m10.set(0)

        self.m11.set(0)

        self.m12.set(0)

        self.m1.set(0)

        self.m2.set(0)

        self.m3.set(0)

        self.m4.set(0)



        self.t9.set(0)

        self.t10.set(0)

        self.t11.set(0)

        self.t12.set(0)

        self.t1.set(0)

        self.t2.set(0)

        self.t3.set(0)

        self.t4.set(0)



        self.w9.set(0)

        self.w10.set(0)

        self.w11.set(0)

        self.w12.set(0)

        self.w1.set(0)

        self.w2.set(0)

        self.w3.set(0)

        self.w4.set(0)



        self.th9.set(0)

        self.th10.set(0)

        self.th11.set(0)

        self.th12.set(0)

        self.th1.set(0)

        self.th2.set(0)

        self.th3.set(0)

        self.th4.set(0)



        self.f9.set(0)

        self.f10.set(0)

        self.f11.set(0)

        self.f12.set(0)

        self.f1.set(0)

        self.f2.set(0)

        self.f3.set(0)

        self.f4.set(0)





        self.fifthwin.title("Georgia Tech Tutor Application")



        label = Label(self.fifthwin, text = "Student Information").grid(row = 0)

        label1 = Label(self.fifthwin, text = "Georgia Tech ID").grid(row = 1, column = 0)

        label2 = Label(self.fifthwin, text = "First Name").grid(row = 2, column = 0)

        label3 = Label(self.fifthwin, text = "Last Name").grid(row = 2, column = 2)

        label4 = Label(self.fifthwin, text = "Email").grid(row = 3, column = 0)

        label5 = Label(self.fifthwin, text =  "Telephone").grid(row = 3, column = 2)

        label6 = Label(self.fifthwin, text = "GPA").grid(row = 4, column = 0)

        label7 = Label(self.fifthwin, text = "Courses for Tutoring").grid(row = 5)

        



        addClassButton = Button(self.fifthwin, text = "Add Course to Tutor", command = self.addCourseTutor, pady=10).grid(row=7,column=0)

        self.counterAdd = 8

        self.gta1 = IntVar()

        self.gta1.set(0)

        self.gta2 = IntVar()

        self.gta2.set(0)

        self.gta3 = IntVar()

        self.gta3.set(0)

        self.gta4 = IntVar()

        self.gta4.set(0)



        self.variableCourseTutor1 = ""

        self.variableCourseTutor2 = ""

        self.variableCourseTutor3 = ""

        self.variableCourseTutor4 = "" 



        

        label11 = Label(self.fifthwin, text = "Available Days/Times").grid(row = 100)

        label12 = Label(self.fifthwin, text = "Monday").grid(row = 102, column = 0)

        label13 = Label(self.fifthwin, text = "Tuesday").grid(row = 104, column = 0)

        label14 = Label(self.fifthwin, text = "Wednesday").grid(row = 106, column = 0)

        label15 = Label(self.fifthwin, text = "Thursday").grid(row = 108, column = 0)

        label16 = Label(self.fifthwin, text = "Friday").grid(row = 110, column = 0)



        self.entrygtid = Entry(self.fifthwin, width = 30, state = NORMAL)

        self.entrygtid.grid(row = 1, column = 1)

        self.entrygpa =Entry(self.fifthwin, width = 30, state = NORMAL)

        self.entrygpa.grid(row = 4, column = 1)

        self.firstname1= Entry(self.fifthwin, width = 30, state = NORMAL)

        self.firstname1.grid(row = 2, column = 1)

        self.lastname1 = Entry(self.fifthwin, width = 30, state = NORMAL)

        self.lastname1.grid(row = 2, column = 3)

        self.emailentry= Entry(self.fifthwin, width = 30, state = NORMAL)

        self.emailentry.grid(row = 3, column = 1)

        self.telentry= Entry(self.fifthwin, width = 30, state = NORMAL)

        self.telentry.grid(row = 3, column = 3)





        radiobutton = Radiobutton(self.fifthwin, text = "Undergraduate", variable = self.uorgvar, value =2)

        radiobutton1 = Radiobutton(self.fifthwin, text = "Graduate", variable = self.uorgvar, value = 1)



        radiobutton.grid(row = 4, column = 3)

        radiobutton1.grid(row = 5, column = 3)





        timeSlotVar = [("m9","m10","m11","m12","m1","m2","m3","m4"),("t9","t10","t11","t12","t1","t2","t3","t4"),("w9","w10","w11","w12","w1","w2","w3","w4"),("th9","th10","th11","th12","th1","th2","th3","th4"),("f9","f10","f11","f12","f1","f2","f3","f4")]           

            



        monframe = Frame(self.fifthwin)

        monframe.grid(row = 103, columnspan = 5)



        cbuttonm9 = Checkbutton(monframe, text = "9am", variable=self.m9, onvalue=1, offvalue=0).grid(row=0, column=0)

        cbuttonm10 = Checkbutton(monframe, text = "10am", variable=self.m10, onvalue=1, offvalue=0).grid(row=0, column=1)

        cbuttonm11 = Checkbutton(monframe, text = "11am", variable=self.m11, onvalue=1, offvalue=0).grid(row=0, column=2)

        cbuttonm12 = Checkbutton(monframe, text = "12am", variable=self.m12, onvalue=1, offvalue=0).grid(row=0, column=3)

        cbuttonm1 = Checkbutton(monframe, text = "1pm", variable=self.m1, onvalue=1, offvalue=0).grid(row=0, column=4)

        cbuttonm2 = Checkbutton(monframe, text = "2pm", variable=self.m2, onvalue=1, offvalue=0).grid(row=0, column=5)

        cbuttonm3 = Checkbutton(monframe, text = "3pm", variable=self.m3, onvalue=1, offvalue=0).grid(row=0, column=6)

        cbuttonm4 = Checkbutton(monframe, text = "4pm", variable=self.m4, onvalue=1, offvalue=0).grid(row=0, column=7)



        tuesframe = Frame(self.fifthwin)

        tuesframe.grid(row = 105, columnspan = 5)



        cbuttont9 = Checkbutton(tuesframe, text = "9am", variable=self.t9, onvalue=1, offvalue=0).grid(row=0, column=0)

        cbuttont10 = Checkbutton(tuesframe, text = "10am", variable=self.t10, onvalue=1, offvalue=0).grid(row=0, column=1)

        cbuttont11 = Checkbutton(tuesframe, text = "11am", variable=self.t11, onvalue=1, offvalue=0).grid(row=0, column=2)

        cbuttont12 = Checkbutton(tuesframe, text = "12am", variable=self.t12, onvalue=1, offvalue=0).grid(row=0, column=3)

        cbuttont1 = Checkbutton(tuesframe, text = "1pm", variable=self.t1, onvalue=1, offvalue=0).grid(row=0, column=4)

        cbuttont2 = Checkbutton(tuesframe, text = "2pm", variable=self.t2, onvalue=1, offvalue=0).grid(row=0, column=5)

        cbuttont3 = Checkbutton(tuesframe, text = "3pm", variable=self.t3, onvalue=1, offvalue=0).grid(row=0, column=6)

        cbuttont4 = Checkbutton(tuesframe, text = "4pm", variable=self.t4, onvalue=1, offvalue=0).grid(row=0, column=7)

        

        wedframe = Frame(self.fifthwin)

        wedframe.grid(row = 107, columnspan = 5)



        cbuttonw9 = Checkbutton(wedframe, text = "9am", variable=self.w9, onvalue=1, offvalue=0).grid(row=0, column=0)

        cbuttonw10 = Checkbutton(wedframe, text = "10am", variable=self.w10, onvalue=1, offvalue=0).grid(row=0, column=1)

        cbuttonw11 = Checkbutton(wedframe, text = "11am", variable=self.w11, onvalue=1, offvalue=0).grid(row=0, column=2)

        cbuttonw12 = Checkbutton(wedframe, text = "12am", variable=self.w12, onvalue=1, offvalue=0).grid(row=0, column=3)

        cbuttonw1 = Checkbutton(wedframe, text = "1pm", variable=self.w1, onvalue=1, offvalue=0).grid(row=0, column=4)

        cbuttonw2 = Checkbutton(wedframe, text = "2pm", variable=self.w2, onvalue=1, offvalue=0).grid(row=0, column=5)

        cbuttonw3 = Checkbutton(wedframe, text = "3pm", variable=self.w3, onvalue=1, offvalue=0).grid(row=0, column=6)

        cbuttonw4 = Checkbutton(wedframe, text = "4pm", variable=self.w4, onvalue=1, offvalue=0).grid(row=0, column=7)







        thursframe = Frame(self.fifthwin)

        thursframe.grid(row = 109, columnspan = 5)



        cbuttonth9 = Checkbutton(thursframe, text = "9am", variable=self.th9, onvalue=1, offvalue=0).grid(row=0, column=0)

        cbuttonth10 = Checkbutton(thursframe, text = "10am", variable=self.th10, onvalue=1, offvalue=0).grid(row=0, column=1)

        cbuttonth11 = Checkbutton(thursframe, text = "11am", variable=self.th11, onvalue=1, offvalue=0).grid(row=0, column=2)

        cbuttonth12 = Checkbutton(thursframe, text = "12am", variable=self.th12, onvalue=1, offvalue=0).grid(row=0, column=3)

        cbuttonth1 = Checkbutton(thursframe, text = "1pm", variable=self.th1, onvalue=1, offvalue=0).grid(row=0, column=4)

        cbuttonth2 = Checkbutton(thursframe, text = "2pm", variable=self.th2, onvalue=1, offvalue=0).grid(row=0, column=5)

        cbuttonth3 = Checkbutton(thursframe, text = "3pm", variable=self.th3, onvalue=1, offvalue=0).grid(row=0, column=6)

        cbuttonth4 = Checkbutton(thursframe, text = "4pm", variable=self.th4, onvalue=1, offvalue=0).grid(row=0, column=7)

        



        friframe = Frame(self.fifthwin)

        friframe.grid(row = 111, columnspan = 5)

        



        cbuttonf9 = Checkbutton(friframe, text = "9am", variable=self.f9).grid(row=0, column=0)

        cbuttonf10 = Checkbutton(friframe, text = "10am", variable=self.f10, onvalue=1, offvalue=0).grid(row=0, column=1)

        cbuttonf11 = Checkbutton(friframe, text = "11am", variable=self.f11, onvalue=1, offvalue=0).grid(row=0, column=2)

        cbuttonf12 = Checkbutton(friframe, text = "12am", variable=self.f12, onvalue=1, offvalue=0).grid(row=0, column=3)

        cbuttonf1 = Checkbutton(friframe, text = "1pm", variable=self.f1, onvalue=1, offvalue=0).grid(row=0, column=4)

        cbuttonf2 = Checkbutton(friframe, text = "2pm", variable=self.f2, onvalue=1, offvalue=0).grid(row=0, column=5)

        cbuttonf3 = Checkbutton(friframe, text = "3pm", variable=self.f3, onvalue=1, offvalue=0).grid(row=0, column=6)

        cbuttonf4 = Checkbutton(friframe, text = "4pm", variable=self.f4, onvalue=1, offvalue=0).grid(row=0, column=7)





        buttonhelper = Button(self.fifthwin, text = "Okay", command = self.applyhelper)

        buttonhelper.grid(row = 120, column = 3)

        backbutton = Button(self.fifthwin, text = "Back", command = self.applyback)

        backbutton.grid(row = 120, column = 0)





    def applyhelper(self):



        



        semester = "SUMMER2014"

        timeSlotVar = [(self.m9,self.m10,self.m11,self.m12,self.m1,self.m2,self.m3,self.m4),(self.t9,self.t10,self.t11,self.t12,self.t1,self.t2,self.t3,self.t4), (self.w9,self.w10,self.w11,self.w12,self.w1,self.w2,self.w3,self.w4), (self.th9,self.th10,self.th11,self.th12,self.th1,self.th2,self.th3,self.th4), (self.f9,self.f10,self.f11,self.f12,self.f1,self.f2,self.f3,self.f4)]

        day = ["M","T","W","R","F"]

        time = [9,10,11,12,13,14,15,16]

        count=0

        for x in range(len(timeSlotVar)):

            for y in range(len(timeSlotVar[x])):

                var1 = timeSlotVar[x][y]

                yes1 = var1.get()

                if yes1 == 1:

                    count = count + 1



        gta1a = self.gta1.get()

        gta2a = self.gta2.get()

        gta3a = self.gta3.get()

        gta4a = self.gta4.get()





        if self.entrygtid.get()=="" or self.entrygpa.get()=="" or self.firstname1.get()=="" or self.lastname1.get()=="" or self.emailentry.get()=="" or self.telentry.get()=="":

            messagebox.showerror("Error","Please Fill Out All Required Fields")

        elif self.uorgvar.get() == 3:

            messagebox.showerror("Error","Please Select Level of Study")

        elif self.usename != self.entrygtid.get():

            messagebox.showerror("Error","Incorrect GTID Number")

            

            

        

## need to check if GPA is in correct format and >3.0









        elif self.variableCourseTutor1 == "" and self.variableCourseTutor2 == "" and self.variableCourseTutor3 == "" and self.variableCourseTutor4 == "":

            messagebox.showerror("Error","Must Select at least 1 course to tutor")





        elif self.uorgvar.get() ==2 and (gta1a == 1 or gta2a ==1 or gta3a==1 or gta4a==1):

            messagebox.showerror("Error", "You must be a graduate student to be a graduate TA")





        elif count < 5:

            messagebox.showerror("Error","You must sign up for at least 5 hours")

            

        elif self.usename == self.entrygtid.get():

            self.cursor.execute("SELECT DISTINCT TTGTID FROM Tutors")

            alreadyExists = self.cursor.fetchall()

            print(alreadyExists)

            for x in range(len(alreadyExists)):

                if self.entrygtid.get() == alreadyExists[x][0]:

                    messagebox.showerror("Error","Tutor already exists in system")

                    self.fifthwin.destroy()

                    self.thirdwin.deiconify()

                    return

                    

            

            print("all information entered correctly")

            



            try:

##

##                newTutorUpdate = ("INSERT INTO Tutor VALUES (%s,%s,%s)")

##                self.cursor.execute(newTutorUpdate,(self.entrygtid.get(),self.telentry.get(),self.entrygpa.get()))





                

                if self.variableCourseTutor1 != "":

                    if self.variableCourseTutor1.get() == "":

                        print("did not select course")

                    else:

                        a = self.variableCourseTutor1.get()

                        b=a.split(" ")

                        tutorsCourses = ("INSERT INTO Tutors VALUES (%s,%s,%s,%s)")

                        self.cursor.execute(tutorsCourses,(self.entrygtid.get(),self.gta1.get(),b[0],b[1]))

                if self.variableCourseTutor2 != "":

                    if self.variableCourseTutor2.get() == "":

                        print("did not select course")

                    else:

                        a = self.variableCourseTutor2.get()

                        b=a.split(" ")

                        tutorsCourses = ("INSERT INTO Tutors VALUES (%s,%s,%s,%s)")

                        self.cursor.execute(tutorsCourses,(self.entrygtid.get(),self.gta2.get(),b[0],b[1]))

                if self.variableCourseTutor3 != "":

                    if self.variableCourseTutor3.get() == "":

                        print("did not select course")

                    else:

                        a = self.variableCourseTutor3.get()

                        b=a.split(" ")

                        tutorsCourses = ("INSERT INTO Tutors VALUES (%s,%s,%s,%s)")

                        self.cursor.execute(tutorsCourses,(self.entrygtid.get(),self.gta3.get(),b[0],b[1]))

                if self.variableCourseTutor4 != "":

                    if self.variableCourseTutor4.get() == "":

                        print("did not select course")

                    else:

                        a = self.variableCourseTutor4.get()

                        b=a.split(" ")

                        tutorsCourses = ("INSERT INTO Tutors VALUES (%s,%s,%s,%s)")

                        self.cursor.execute(tutorsCourses,(self.entrygtid.get(),self.gta4.get(),b[0],b[1]))



                j=0

                for x in range(len(timeSlotVar)):

                    i=0

                    for y in range(len(timeSlotVar[x])):

                        var =timeSlotVar[x][y]

                        yes = var.get()

                        if yes == 1:

                            timeslots = ("INSERT INTO TutorTimeSlots VALUES (%s,%s,%s,%s)")

                            self.cursor.execute(timeslots,(self.entrygtid.get(),time[i],semester,day[j]))

                        else:

                            pass

                        i=i+1

                    j=j+1

                print("yay")

                messagebox.showerror("Congrats","All information is saved")

                try:
                
                    if self.uorgvar.get() == 1:
                        sql = "insert into Grad values (%s)"
                        self.cursor.execute(sql, self.usename)
                        self.database.commit()
                except:
                    pass

                try:
                                           
                    if self.uorgvar.get() == 0:
                        sql = "insert into Undergrad values (%s)"
                        self.cursor.execute(sql, self.usename)
                        self.database.commit()

                except:
                    pass

                self.fifthwin.destroy()

                self.thirdwin.deiconify()

                

                    

            except:

                messagebox.showerror("Error","Unable to add information to database, please ensure all entries are valid.")

                self.fifthwin.destroy()

                self.thirdwin.deiconify()





    def addCourseTutor(self):



        self.cursor.execute("SELECT * FROM Course")

        courses = []

        for x in self.cursor:

            courses.append(str(x[0])+" "+str(x[1]))     



        if self.counterAdd== 8:

            self.variableCourseTutor1 = StringVar(self.fifthwin)

            ow1 = OptionMenu(self.fifthwin, self.variableCourseTutor1,*courses)

            ow1.grid(row=self.counterAdd,column=0,sticky=EW)

            Checkbutton(self.fifthwin, text = "GTA", variable=self.gta1).grid(row=self.counterAdd, column=1)

        if self.counterAdd == 9:

            self.variableCourseTutor2 = StringVar(self.fifthwin)

            ow2 = OptionMenu(self.fifthwin, self.variableCourseTutor2,*courses)

            ow2.grid(row=self.counterAdd,column=0,sticky=EW)

            Checkbutton(self.fifthwin, text = "GTA", variable=self.gta2).grid(row=self.counterAdd, column=1)

        if self.counterAdd == 10:

            self.variableCourseTutor3 = StringVar(self.fifthwin)

            ow3 = OptionMenu(self.fifthwin, self.variableCourseTutor3,*courses)

            ow3.grid(row=self.counterAdd,column=0,sticky=EW)

            Checkbutton(self.fifthwin, text = "GTA", variable=self.gta3).grid(row=self.counterAdd, column=1)

        if self.counterAdd == 11:

            self.variableCourseTutor4 = StringVar(self.fifthwin)

            ow4 = OptionMenu(self.fifthwin, self.variableCourseTutor4,*courses)

            ow4.grid(row=self.counterAdd,column=0,sticky=EW)

            Checkbutton(self.fifthwin, text = "GTA", variable=self.gta4).grid(row=self.counterAdd, column=1)

        if self.counterAdd>11:

            messagebox.showerror("Error","You can only tutor up to 4 courses")

        

        self.counterAdd = self.counterAdd + 1 





    

    def applyback(self):

        self.fifthwin.destroy()

        self.thirdwin.deiconify()







    def searchtutorpage(self):
        self.searcht = Toplevel()
        self.searcht.title("Search/schedule tutor")

        
        self.thirdwin.withdraw()
        
        l1 = Label(self.searcht, text = "Course")
        l1.grid(row = 0, column = 0, sticky=W)
        self.database = self.Connect()
        self.cursor = self.database.cursor()
        self.cursor.execute("SELECT * FROM Course")
        courses = []
        for x in self.cursor:
            courses.append(str(x[0])+" "+str(x[1]))     
        self.variablesc = StringVar(self.searcht)
        w1 = OptionMenu(self.searcht, self.variablesc,*courses)
        w1.grid(row=0,column=1,columnspan=3,sticky=EW)
        
        
        
        l4 = Label(self.searcht, text = "Availability: Note - Tutor session can only be scheduled for 1 hour per week for a given course!")
        l4.grid(row=2,column = 0, columnspan = 6,sticky= EW)
        self.framewin30 = Frame(self.searcht,height=2, bd=1, relief=FLAT)
        self.framewin30.grid(row=3,column = 1, columnspan = 3)
        l41= Label(self.framewin30,text = "Day")
        l41.grid(row=0,column=0, columnspan =2, sticky = EW)
        l42= Label(self.framewin30,text = "Time")
        l42.grid(row=0,column=2, columnspan =2, sticky = EW)
        self.variablesd1 = StringVar(self.framewin30)
        OptionMenu(self.framewin30, self.variablesd1,"M","T","W","R","F").grid(row=1,column=0,columnspan = 2,sticky=EW)
        self.variablesd2 = StringVar(self.framewin30)
        OptionMenu(self.framewin30, self.variablesd2,"M","T","W","R","F").grid(row=2,column=0,columnspan = 2,sticky=EW)
        self.variablesd3 = StringVar(self.framewin30)
        OptionMenu(self.framewin30, self.variablesd3,"M","T","W","R","F").grid(row=3,column=0,columnspan = 2,sticky=EW)
        self.variablesd4 = StringVar(self.framewin30)
        OptionMenu(self.framewin30, self.variablesd4,"M","T","W","R","F").grid(row=4,column=0,columnspan = 2,sticky=EW)
        self.variablesd5 = StringVar(self.framewin30)
        OptionMenu(self.framewin30, self.variablesd5,"M","T","W","R","F").grid(row=5,column=0,columnspan = 2,sticky=EW)
        



        
        mbt1 =  Menubutton ( self.framewin30, text="Time Period", relief=RAISED )
        mbt1.grid(row=1,column=2,columnspan=2,sticky=EW)
        mbt1.menu  =  Menu ( mbt1, tearoff = 0 )
        mbt1["menu"]  =  mbt1.menu
        self.mVar9  = IntVar()
        self.mVar10  = IntVar()
        self.mVar11  = IntVar()
        self.mVar12 = IntVar()
        self.mVar13 = IntVar()
        self.mVar14 = IntVar()
        self.mVar15 = IntVar()
        self.mVar16  = IntVar()

        mbt1.menu.add_checkbutton ( label="09",variable=self.mVar9  )
        mbt1.menu.add_checkbutton ( label="10",variable=self.mVar10)
        mbt1.menu.add_checkbutton ( label="11",variable=self.mVar11 )
        mbt1.menu.add_checkbutton ( label="12",variable=self.mVar12 )
        mbt1.menu.add_checkbutton ( label="13",variable=self.mVar13 )
        mbt1.menu.add_checkbutton ( label="14",variable=self.mVar14 )
        mbt1.menu.add_checkbutton ( label="15",variable=self.mVar15 )
        mbt1.menu.add_checkbutton ( label="16",variable=self.mVar16 )

        mbt2 =  Menubutton ( self.framewin30, text="Time Period", relief=RAISED )
        mbt2.grid(row=2,column=2,columnspan=2,sticky=EW)
        mbt2.menu  =  Menu ( mbt2, tearoff = 0 )
        mbt2["menu"]  =  mbt2.menu
        self.tVar9  = IntVar()
        self.tVar10  = IntVar()
        self.tVar11  = IntVar()
        self.tVar12 = IntVar()
        self.tVar13 = IntVar()
        self.tVar14 = IntVar()
        self.tVar15 = IntVar()
        self.tVar16  = IntVar()

        mbt2.menu.add_checkbutton ( label="09",variable=self.tVar9  )
        mbt2.menu.add_checkbutton ( label="10",variable=self.tVar10 )
        mbt2.menu.add_checkbutton ( label="11",variable=self.tVar11 )
        mbt2.menu.add_checkbutton ( label="12",variable=self.tVar12 )
        mbt2.menu.add_checkbutton ( label="13",variable=self.tVar13 )
        mbt2.menu.add_checkbutton ( label="14",variable=self.tVar14 )
        mbt2.menu.add_checkbutton ( label="15",variable=self.tVar15 )
        mbt2.menu.add_checkbutton ( label="16",variable=self.tVar16 )


        mbt3 =  Menubutton ( self.framewin30, text="Time Period", relief=RAISED )
        mbt3.grid(row=3,column=2,columnspan=2,sticky=EW)
        mbt3.menu  =  Menu ( mbt3, tearoff = 0 )
        mbt3["menu"]  =  mbt3.menu
        self.wVar9  = IntVar()
        self.wVar10  = IntVar()
        self.wVar11  = IntVar()
        self.wVar12 = IntVar()
        self.wVar13 = IntVar()
        self.wVar14 = IntVar()
        self.wVar15 = IntVar()
        self.wVar16  = IntVar()

        mbt3.menu.add_checkbutton ( label="09",variable=self.wVar9  )
        mbt3.menu.add_checkbutton ( label="10",variable=self.wVar10 )
        mbt3.menu.add_checkbutton ( label="11",variable=self.wVar11 )
        mbt3.menu.add_checkbutton ( label="12",variable=self.wVar12 )
        mbt3.menu.add_checkbutton ( label="13",variable=self.wVar13 )
        mbt3.menu.add_checkbutton ( label="14",variable=self.wVar14 )
        mbt3.menu.add_checkbutton ( label="15",variable=self.wVar15 )
        mbt3.menu.add_checkbutton ( label="16",variable=self.wVar16 )


        mbt4 =  Menubutton ( self.framewin30, text="Time Period", relief=RAISED )
        mbt4.grid(row=4,column=2,columnspan=2,sticky=EW)
        mbt4.menu  =  Menu ( mbt4, tearoff = 0 )
        mbt4["menu"]  =  mbt4.menu
        self.rVar9  = IntVar()
        self.rVar10  = IntVar()
        self.rVar11  = IntVar()
        self.rVar12 = IntVar()
        self.rVar13 = IntVar()
        self.rVar14 = IntVar()
        self.rVar15 = IntVar()
        self.rVar16  = IntVar()

        mbt4.menu.add_checkbutton ( label="09",variable=self.rVar9  )
        mbt4.menu.add_checkbutton ( label="10",variable=self.rVar10 )
        mbt4.menu.add_checkbutton ( label="11",variable=self.rVar11 )
        mbt4.menu.add_checkbutton ( label="12",variable=self.rVar12 )
        mbt4.menu.add_checkbutton ( label="13",variable=self.rVar13 )
        mbt4.menu.add_checkbutton ( label="14",variable=self.rVar14 )
        mbt4.menu.add_checkbutton ( label="15",variable=self.rVar15 )
        mbt4.menu.add_checkbutton ( label="16",variable=self.rVar16 )


        mbt5 =  Menubutton ( self.framewin30, text="Time Period", relief=RAISED )
        mbt5.grid(row=5,column=2,columnspan=2,sticky=EW)
        mbt5.menu  =  Menu ( mbt5, tearoff = 0 )
        mbt5["menu"]  =  mbt5.menu
        self.fVar9  = IntVar()
        self.fVar10  = IntVar()
        self.fVar11  = IntVar()
        self.fVar12 = IntVar()
        self.fVar13 = IntVar()
        self.fVar14 = IntVar()
        self.fVar15 = IntVar()
        self.fVar16  = IntVar()

        mbt5.menu.add_checkbutton ( label="09",variable=self.fVar9  )
        mbt5.menu.add_checkbutton ( label="10",variable=self.fVar10 )
        mbt5.menu.add_checkbutton ( label="11",variable=self.fVar11 )
        mbt5.menu.add_checkbutton ( label="12",variable=self.fVar12 )
        mbt5.menu.add_checkbutton ( label="13",variable=self.fVar13 )
        mbt5.menu.add_checkbutton ( label="14",variable=self.fVar14 )
        mbt5.menu.add_checkbutton ( label="15",variable=self.fVar15 )
        mbt5.menu.add_checkbutton ( label="16",variable=self.fVar16 )

        
      
        b1 = Button(self.searcht, text = "OK", command = self.OK)
        b1.grid(row=5,column = 0,sticky=EW)
        l5 = Label(self.searcht, text = "Available Tutors",font = "B")
        l5.grid(row=6, column =2, columnspan = 1,sticky=EW)
        
        self.b2 = Button(self.searcht, text = "Schedule a Tutor", command = self.scheduletutor)
        self.b2.grid(row=7,column = 0, columnspan =1,sticky=EW)
        self.b3 = Button(self.searcht, text = "Cancel", command = self.canceltomain)
        self.b3.grid(row=7,column = 1, columnspan =1,sticky=EW)
        self.framewin3 = Frame(self.searcht,height=2, bd=1, relief=SUNKEN)
        self.framewin3.grid(row=8,column=0,columnspan=7,sticky=EW)
        bclean = Button(self.searcht, text = "Refresh", command = self.refreshsearch)
        bclean.grid(row=5,column = 3,sticky=EW)

    def refreshsearch(self):
        self.variablesd1.set("")
        self.variablesd2.set("")
        self.variablesd3.set("")
        self.variablesd4.set("")
        self.variablesd5.set("")
        self.mVar9.set(0)
        self.mVar10.set(0)
        self.mVar11.set(0)
        self.mVar12.set(0)
        self.mVar13.set(0)
        self.mVar14.set(0)
        self.mVar15.set(0)
        self.mVar16.set(0)
        self.tVar9.set(0)
        self.tVar10.set(0)
        self.tVar11.set(0)
        self.tVar12.set(0)
        self.tVar13.set(0)
        self.tVar14.set(0)
        self.tVar15.set(0)
        self.tVar16.set(0)

        self.wVar9.set(0)
        self.wVar10.set(0)
        self.wVar11.set(0)
        self.wVar12.set(0)
        self.wVar13.set(0)
        self.wVar14.set(0)
        self.wVar15.set(0)
        self.wVar16.set(0)

        self.rVar9.set(0)
        self.rVar10.set(0)
        self.rVar11.set(0)
        self.rVar12.set(0)
        self.rVar13.set(0)
        self.rVar14.set(0)
        self.rVar15.set(0)
        self.rVar16.set(0)


        self.fVar9.set(0)
        self.fVar10.set(0)
        self.fVar11.set(0)
        self.fVar12.set(0)
        self.fVar13.set(0)
        self.fVar14.set(0)
        self.fVar15.set(0)
        self.fVar16.set(0)
    
    def OK (self):
        self.mdaytime = []
        self.mdaytime.append ([self.variablesd1.get(),self.mVar9.get(),self.mVar10.get(),self.mVar11.get(),
                               self.mVar12.get(),self.mVar13.get(),self.mVar14.get(),self.mVar15.get(),self.mVar16.get()])
        self.mdaytime.append ([self.variablesd2.get(),self.tVar9.get(),self.tVar10.get(),self.tVar11.get(),
                               self.tVar12.get(),self.tVar13.get(),self.tVar14.get(),self.tVar15.get(),self.tVar16.get()])
        self.mdaytime.append ([self.variablesd3.get(),self.wVar9.get(),self.wVar10.get(),self.wVar11.get(),
                               self.wVar12.get(),self.wVar13.get(),self.wVar14.get(),self.wVar15.get(),self.wVar16.get()])
        self.mdaytime.append ([self.variablesd4.get(),self.rVar9.get(),self.rVar10.get(),self.rVar11.get(),
                               self.rVar12.get(),self.rVar13.get(),self.rVar14.get(),self.rVar15.get(),self.rVar16.get()])
        self.mdaytime.append ([self.variablesd5.get(),self.fVar9.get(),self.fVar10.get(),self.fVar11.get(),
                               self.fVar12.get(),self.fVar13.get(),self.fVar14.get(),self.fVar15.get(),self.fVar16.get()])

        daycheck = 0
        for x in range (5):
            for y in range (5):
                if x != y:
                    if self.mdaytime[x][0] == self.mdaytime[y][0] and self.mdaytime[x][0]!= "" and self.mdaytime[y][0]!= "":
                        daycheck = daycheck+1
        
        

        if daycheck != 0:
            messagebox.showerror("Error!","Please do not choose same day twice!")
            self.refreshsearch()
        elif self.variablesd1.get() == "" and self.variablesd2.get() == "" and self.variablesd3.get() == "" and self.variablesd4.get() == "" and self.variablesd5.get() == "":
            messagebox.showerror("Error!","Please choose a time!")
            self.refreshsearch()
        else:                    
            print (self.mdaytime)
            for y in range (len(self.mdaytime)):
                for x in range(len(self.mdaytime[y])):
                    if self.mdaytime[y][x] == 1:
                        self.mdaytime[y][x] = x+8
                
            for x in self.mdaytime:
                while 0 in x:
                    x.remove(0)

                while "" in x:
                    x.remove("")
                    

            while [] in self.mdaytime:
                self.mdaytime.remove([]) 

            ## update when change search course, also delete extra list in self.mdaytime
                    
                    
                    
                
            
            print (self.mdaytime)
            
            self.framewin3.destroy()
            self.framewin3 = Frame(self.searcht,height=2, bd=1, relief=SUNKEN)
            self.sc = self.variablesc.get()
            self.school = self.sc[:-5]
            self.cnumber = self.sc[-4:]
            
            if self.sc == "":
                messagebox.showerror("Error","Please choose a course!")
            
            else: 
                
              
                l71 = Label(self.framewin3,text = "First Name")
                l71.grid(row=7,column=0,sticky=EW)
                l72 = Label(self.framewin3,text = "Last Name")
                l72.grid(row=7,column=1,sticky=EW)
                l73 = Label(self.framewin3,text = "Email")
                l73.grid(row=7,column=2,sticky=EW)
                l74 = Label(self.framewin3,text = "Avg Prof Rating")
                l74.grid(row=7,column=3,sticky=EW)
                l75 = Label(self.framewin3,text = "# Professors")
                l75.grid(row=7,column=4,sticky=EW)
                l76 = Label(self.framewin3,text = "Avg Student Rating")
                l76.grid(row=7,column=5,sticky=EW)
                l77 = Label(self.framewin3,text = "# Students")
                l77.grid(row=7,column=6,sticky=EW)
                alist = self.helpfunction()
                for x in range (len(alist)):
                    for i in range (len(alist[x])):
                        Label(self.framewin3, text = alist[x][i]).grid(row= (7+x+1),column = (0+i))
                
                self.framewin3.grid(row=8,column=0,columnspan=7,sticky=EW)
                ##for x in list a
                self.b2.grid(row=7+len(alist)+2)
                self.b3.grid(row=7+len(alist)+2)
            
    def helpfunction(self):
        
        SQL2 = "SELECT  AVG(RNumEvaluation),COUNT(PRGTID) FROM Recommends WHERE TRGTID = %s"
        SQL3 = "SELECT AVG(ANumEvaluation), COUNT(UAGTID) FROM Rates WHERE TAGTID = %s"
        SQL4 = "SELECT FName, LName, Email FROM Student WHERE SGTID = %s"
        SQL11 = "SELECT TRGTID FROM Recommends WHERE TRGTID = %s"
        #get available tutors' GTID
        cursor = self.cursor
        GTID = []
        for t in range(len(self.mdaytime)):
            day = str(self.mdaytime[t][0])
            for n in range(len(self.mdaytime[t])-1):
                time = str(self.mdaytime[t][n+1])
                
                SQL1 = "SELECT TTGTID FROM Tutors NATURE JOIN TutorTimeSlots ON TSGTID = TTGTID WHERE TSchool = '"+self.school+ "'AND TNumber = "+ self.cnumber + " AND Time = " + time + " AND Semester = 'SUMMER2014' AND Weekday = '" + day + "'"
                cursor.execute(SQL1)
                for x in cursor:
                    if x not in GTID:
                        cursor.execute(SQL11, x)
                        final = cursor.fetchone()
                        if final != None:
                            GTID.append(x)

        #get tutors' professor rating aList
        aList = []
        for y in GTID:
            cursor.execute(SQL2, y)
            for i in cursor:
                aList.append(i)
        #get tutors' student rating bList
        bList = [] 
        for z in GTID:
            cursor.execute(SQL3, z)
            for j in cursor:
                bList.append(j)
        #get tutors' info
        cList = []
        for m in GTID:
            cursor.execute(SQL4, m)
            for h in cursor:
                cList.append(h)
        List = []
        i = 0
        #all info
        for q in aList:
            List.append((cList[i] + aList[i] + bList[i]))
            i = i + 1
        if List == []:
            messagebox.showerror("Error","There is no available tutor for this course at selected period!")

            
        j = 0
        for gtid in GTID:
            gtid = str(gtid)
            gtid = gtid[2:11]
            for i in range(len(self.mdaytime)):
                day = str(self.mdaytime[i][0])
                for n in range(len(self.mdaytime[i]) - 1):
                    time = str(self.mdaytime[i][n + 1])
                    
                    SQL5 = "SELECT Weekday, Time FROM TutorTimeSlots WHERE Time = " + time + " AND TSGTID = "+gtid+" AND Semester = 'SUMMER2014' AND Weekday = '" + day + "'"
                    cursor.execute(SQL5)
                    answer = cursor.fetchone()
                    if answer != None:
                        
                        cList[j] = cList[j] + answer
            j = j + 1

        self.cList = cList
        print(cList)
        print(List)

        return (List)
        
    def canceltomain(self):
        self.searcht.destroy()
        self.thirdwin.deiconify()
    def canceltosearch(self):
        self.schedulet.destroy()
        self.searcht.deiconify()


    def scheduletutor(self):
        self.searcht.withdraw()
        self.schedulet = Toplevel()
        
        l1 = Label(self.schedulet, text = "Select your Tutor for" +" "+self.sc)
        l1.grid(row=0,column=2,columnspan=3,sticky=EW)
        l9 = Label(self.schedulet, text = "NOTE: Only 1 box under the Select column ma be checked")
        l9.grid(row=9,column=0, columnspan=3,sticky=W)
        b1 = Button(self.schedulet, text = "OK", command = self.helpregistetutor)
        b1.grid(row=10,column=0,columnspan = 2,sticky = EW)
        b2 = Button(self.schedulet, text = "Cancel", command = self.canceltosearch)
        b2.grid(row=10,column=2,columnspan = 2,sticky = EW)
        self.framewin4 = Frame(self.schedulet,height=2,width = 10, bd=1, relief=FLAT)
        self.framewin4.grid(row=1,column = 0, columnspan = 10)
        l71 = Label(self.framewin4,text = "First Name")
        l71.grid(row=1,column=0,sticky=EW)
        l72 = Label(self.framewin4,text = "Last Name")
        l72.grid(row=1,column=1,sticky=EW)
        l73 = Label(self.framewin4,text = "Email")
        l73.grid(row=1,column=2,sticky=EW)
        l74 = Label(self.framewin4,text = "Day")
        l74.grid(row=1,column=3,sticky=EW)
        l75 = Label(self.framewin4,text = "Time")
        l75.grid(row=1,column=4,sticky=EW)
        n=0
        x=0
        for i in range(len(self.cList)):
            i = int(i)
            n = int(n)
            
            Label(self.framewin4,text = self.cList[i][0]).grid(row=2+i+2*n,column=0,columnspan = 1,sticky=EW)
            Label(self.framewin4,text = self.cList[i][1]).grid(row=2+i+2*n,column=1,columnspan = 1,sticky=EW)
            Label(self.framewin4,text = self.cList[i][2]).grid(row=2+i+2*n,column=2,columnspan = 1,sticky=EW)
            Label(self.framewin4,text = self.cList[i][3]).grid(row=2+i+2*n,column=3,columnspan = 1,sticky=EW)
            Label(self.framewin4,text = self.cList[i][4]).grid(row=2+i+2*n,column=4,columnspan = 1,sticky=EW)
            x1 = 2+i+2*n
            if len(self.cList[i])>=7:
                n+=1
                Label(self.framewin4,text = self.cList[i][5]).grid(row=x1+1,column=3,columnspan = 1,sticky=EW)
                Label(self.framewin4,text = self.cList[i][6]).grid(row=x1+1,column=4,columnspan = 1,sticky=EW)
            if len(self.cList[i])>=9:
                n+=1
                Label(self.framewin4,text = self.cList[i][7]).grid(row=x1+2,column=3,columnspan = 1,sticky=EW)
                Label(self.framewin4,text = self.cList[i][8]).grid(row=x1+2,column=4,columnspan = 1,sticky=EW)
            if len(self.cList[i])>=11:
                n+=1
                Label(self.framewin4,text = self.cList[i][9]).grid(row=x1+3,column=3,columnspan = 1,sticky=EW)
                Label(self.framewin4,text = self.cList[i][10]).grid(row=x1+3,column=4,columnspan = 1,sticky=EW)
            if len(self.cList[i])>=13:
                n+=1
                Label(self.framewin4,text = self.cList[i][11]).grid(row=x1+4,column=3,columnspan = 1,sticky=EW)
                Label(self.framewin4,text = self.cList[i][12]).grid(row=x1+4,column=4,columnspan = 1,sticky=EW)
            if len(self.cList[i])>=15:
                n+=1
                Label(self.framewin4,text = self.cList[i][13]).grid(row=x1+5,column=3,columnspan = 1,sticky=EW)
                Label(self.framewin4,text = self.cList[i][14]).grid(row=x1+5,column=4,columnspan = 1,sticky=EW)
            if len(self.cList[i])>=17:
                n+=1
                Label(self.framewin4,text = self.cList[i][15]).grid(row=x1+6,column=3,columnspan = 1,sticky=EW)
                Label(self.framewin4,text = self.cList[i][16]).grid(row=x1+6,column=4,columnspan = 1,sticky=EW)
            if len(self.cList[i])>=19:
                n+=1
                Label(self.framewin4,text = self.cList[i][17]).grid(row=x1+7,column=3,columnspan = 1,sticky=EW)
                Label(self.framewin4,text = self.cList[i][18]).grid(row=x1+7,column=4,columnspan = 1,sticky=EW)
            
            
        tselectlist = []
        for i in range(len(self.cList)):
            for x in range (int((len(self.cList[i])-3)/2)):
                i = int (i)
                x = int(x)
                tselectlist.append(str(self.cList[i][0])+" "+str(self.cList[i][1])+" "+str(self.cList[i][2*(x+2)-1])+" "+str(self.cList[i][2*(x+2)]))
                
        print (tselectlist)
        self.variablesct = StringVar(self.searcht)
        wfinalchoice = OptionMenu(self.schedulet, self.variablesct,*tselectlist)
        wfinalchoice.grid(row=8,column=1,columnspan=3,sticky=EW)
        
    def helpregistetutor(self):
        print(self.variablesct.get())
        finalselectedct = str(self.variablesct.get()[-2:])
        finalselectedct = finalselectedct.replace(" ","")
        finalselectedcd = str(self.variablesct.get()[-4:-2])
        finalselectedcd = finalselectedcd.replace(" ","")
        print (finalselectedct,finalselectedcd)
        namelist = (str(self.variablesct.get())).split(" ")
        fn = namelist[0]
        ln = namelist[1]
        SQL8 = "SELECT SGTID FROM Student WHERE FName = '"+fn+"' AND LName ='"+ln+"'"
        self.cursor.execute(SQL8)
        GTID = self.cursor.fetchone()
        GTID = str(GTID)[2:11]
                        
        ##to check Hires for whether it existed or not

        SQL6 = "SELECT UHGTID FROM Hires WHERE UHGTID = "+self.usename+" AND HSchool = '"+self.school+"' AND HNumber = "+self.cnumber+" AND HSemester = 'SUMMER2014'"
        self.cursor.execute(SQL6)
        an = self.cursor.fetchone()
        print(an)

        if an == None:

        ##insert part
            SQL7 = "INSERT INTO Hires VALUES ("+self.usename+", '"+self.school+"', "+self.cnumber+", "+finalselectedct+", 'SUMMER2014', '"+finalselectedcd+"', "+GTID+")"
            self.cursor.execute(SQL7)
            messagebox.showinfo("Complete","You have successfully registered!")
        else:
            messagebox.showerror("Error","You can only register one tutor for one course!")
                





win = Tk()
obj = CS4400database(win)
win.mainloop()
