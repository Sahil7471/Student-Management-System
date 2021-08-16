from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class student:
        def __init__(self,root):
                self.root =root
                self.root.title("Student Management System")
                self.root.geometry("1530x790+0+0")

                #variable
                self.var_dep=StringVar()
                self.var_course=StringVar()
                self.var_year=StringVar()
                self.var_semester=StringVar()
                self.var_std_id=StringVar()
                self.var_std_name=StringVar()
                self.var_div=StringVar()
                self.var_rollno=StringVar()
                self.var_gender=StringVar()
                self.var_dob=StringVar()
                self.var_email=StringVar()
                self.var_phone=StringVar()
                self.var_address=StringVar()
                self.var_teacher=StringVar()
      




                title = Label(self.root,text="Student management system",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),fg="blue")
                title.pack(side=TOP,fill=X)

#manage fame
                Manage_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="black")
                Manage_Frame.place(x=15,y=100,width=1500,height=600)

#left frame
                DataleftFrame=LabelFrame(Manage_Frame,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
                DataleftFrame.place(x=10,y=10,width=660,height=580)

                std_lb1_info_frame=LabelFrame(DataleftFrame,relief=RIDGE,padx=2,text="Current Course Information",font=("times new roman",12,"bold"),fg="red",bg="white")
                std_lb1_info_frame.place(x=0,y=15,width=650,height=115)

                #labels
                lb1_dep=Label(std_lb1_info_frame,text="Department",font=("arial",12,"bold"),bg="white")
                lb1_dep.grid(row=0,column=0,padx=2,sticky=W)

                combo_dep=ttk.Combobox(std_lb1_info_frame,textvariable=self.var_dep,font=("arial",12,"bold"),width=17,state="readonly")
                combo_dep["value"]=("Select Departmaent","Computer","IT","Civil")
                combo_dep.current(0)
                combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
                #course
                course_std=Label(std_lb1_info_frame,font=("arial",12,"bold"),text="Courses:",bg="white")
                course_std.grid(row=0,column=2,sticky=W,padx=2,pady=10)
                com_txtcourse_std=ttk.Combobox(std_lb1_info_frame,textvariable=self.var_course,state="readonly",font=("arial",12,"bold"),width=17)
                com_txtcourse_std["value"]=("Select Course","FE","SE","TE","BE")
                com_txtcourse_std.current(0)
                com_txtcourse_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)
                #year
                current_year=Label(std_lb1_info_frame,font=("arial",12,"bold"),text="Year:",bg="white")
                current_year.grid(row=1,column=0,sticky=W,padx=2,pady=10)
                com_txt_current_year=ttk.Combobox(std_lb1_info_frame,textvariable=self.var_year,state="readonly",font=("arial",12,"bold"),width=17)
                com_txt_current_year["value"]=("Select Course","2020-2021","2021-2022","2022-2023","2023-2024")
                com_txt_current_year.current(0)
                com_txt_current_year.grid(row=1,column=1,sticky=W,padx=2)

                #semster
                label_semester=Label(std_lb1_info_frame,font=("arial",12,"bold"),text="Semester:",bg="white")
                label_semester.grid(row=1,column=2,sticky=W,padx=2,pady=10)
                com_semester=ttk.Combobox(std_lb1_info_frame,textvariable=self.var_semester,state="readonly",font=("arial",12,"bold"),width=17)
                com_semester["value"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4")
                com_semester.current(0)
                com_semester.grid(row=1,column=3,sticky=W,padx=2,pady=10)

                # Student class LabelFrame
                std_lb1_class_frame=LabelFrame(DataleftFrame,relief=RIDGE,padx=2,text="Class Course Information",font=("times new roman",12,"bold"),fg="red",bg="white")
                std_lb1_class_frame.place(x=0,y=150,width=650,height=350)
                #id
                lb1_id=Label(std_lb1_class_frame,text="StudentID:",font=("arial",12,"bold"),bg="white")
                lb1_id.grid(row=0,column=0,sticky=W,padx=2,pady=7)
                id_entr=ttk.Entry(std_lb1_class_frame,textvariable=self.var_std_id,font=("arial",12,"bold"),width=22)
                id_entr.grid(row=0,column=1,sticky=W,padx=2,pady=7)
                #Name
                lb1_Name=Label(std_lb1_class_frame,text="Student Name:",font=("arial",12,"bold"),bg="white")
                lb1_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)
                txt_name=ttk.Entry(std_lb1_class_frame,textvariable=self.var_std_name,font=("arial",11,"bold"),width=22)
                txt_name.grid(row=0,column=3,sticky=W,padx=2,pady=7)
                #divison
                lb1_div=Label(std_lb1_class_frame,text="Divison:",font=("arial",12,"bold"),bg="white")
                lb1_div.grid(row=1,column=0,sticky=W,padx=2,pady=7)
                com_txt_div=ttk.Combobox(std_lb1_class_frame,textvariable=self.var_div,state="readonly",font=("arial",12,"bold"),width=20)
                com_txt_div["value"]=("Select Divison","A","B","C","D")
                com_txt_div.current(0)
                com_txt_div.grid(row=1,column=1,sticky=W,padx=2,pady=7)
                #Roll
                lb1_roll=Label(std_lb1_class_frame,text="  Roll No.:",font=("arial",12,"bold"),bg="white")
                lb1_roll.grid(row=1,column=2,sticky=W,padx=2,pady=7)
                txt_roll=ttk.Entry(std_lb1_class_frame,textvariable=self.var_rollno,font=("arial",11,"bold"),width=22)
                txt_roll.grid(row=1,column=3,sticky=W,padx=2,pady=7)

                #gender
                lb1_gen=Label(std_lb1_class_frame,text="Gender:",font=("arial",12,"bold"),bg="white")
                lb1_gen.grid(row=2,column=0,sticky=W,padx=2,pady=7)
                com_txt_gender=ttk.Combobox(std_lb1_class_frame,textvariable=self.var_gender,state="readonly",font=("arial",12,"bold"),width=20)
                com_txt_gender["value"]=("Male","Female","Other")
                com_txt_gender.current(0)
                com_txt_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)

                #DoB
                lb1_dob=Label(std_lb1_class_frame,text="  DOB:",font=("arial",12,"bold"),bg="white")
                lb1_dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)
                txt_dob=ttk.Entry(std_lb1_class_frame,textvariable=self.var_dob,font=("arial",11,"bold"),width=22)
                txt_dob.grid(row=2,column=3,sticky=W,padx=2,pady=7)

                #Email
                lb1_Email=Label(std_lb1_class_frame,text="  Email.:",font=("arial",12,"bold"),bg="white")
                lb1_Email.grid(row=3,column=0,sticky=W,padx=2,pady=7)
                txt_Email=ttk.Entry(std_lb1_class_frame,textvariable=self.var_email,font=("arial",11,"bold"),width=22)
                txt_Email.grid(row=3,column=1,sticky=W,padx=2,pady=7)

                #phone
                lb1_phone=Label(std_lb1_class_frame,text="  Phone NO.:",font=("arial",12,"bold"),bg="white")
                lb1_phone.grid(row=3,column=2,sticky=W,padx=2,pady=7)
                txt_phone=ttk.Entry(std_lb1_class_frame,textvariable=self.var_phone,font=("arial",11,"bold"),width=22)
                txt_phone.grid(row=3,column=3,sticky=W,padx=2,pady=7)

                #Address
                lb1_addre=Label(std_lb1_class_frame,text="Address.:",font=("arial",12,"bold"),bg="white")
                lb1_addre.grid(row=4,column=0,sticky=W,padx=2,pady=7)
                txt_addre=ttk.Entry(std_lb1_class_frame,textvariable=self.var_address,font=("arial",11,"bold"),width=22)
                txt_addre.grid(row=4,column=1,sticky=W,padx=2,pady=7)

                #Teacher
                lb1_teacher=Label(std_lb1_class_frame,text="  Teacher Name.:",font=("arial",12,"bold"),bg="white")
                lb1_teacher.grid(row=4,column=2,sticky=W,padx=2,pady=7)
                txt_teacher=ttk.Entry(std_lb1_class_frame,textvariable=self.var_teacher,font=("arial",11,"bold"),width=22)
                txt_teacher.grid(row=4,column=3,sticky=W,padx=2,pady=7)

                #Button fame
                btn_Frame=Frame(DataleftFrame,bd=2,relief=RIDGE,bg="white")
                btn_Frame.place(x=0,y=400,width=650,height=38)

                btn_Add=Button(btn_Frame,text="Save",command=self.add_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
                btn_Add.grid(row=0,column=0,padx=1)

                btn_update=Button(btn_Frame,text="Update",command=self.update_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
                btn_update.grid(row=0,column=1,padx=1)

                btn_delete=Button(btn_Frame,text="Delete",command=self.delete_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
                btn_delete.grid(row=0,column=2,padx=1)

                btn_reset=Button(btn_Frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
                btn_reset.grid(row=0,column=3,padx=1)



        #right frame
                DatarightFrame=LabelFrame(Manage_Frame,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
                DatarightFrame.place(x=681,y=10,width=800,height=580)    

                search_frame=LabelFrame(DatarightFrame,bd=4,relief=RIDGE,padx=2,text="Search Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
                search_frame.place(x=0,y=0,width=790,height=80)

                search_by=Label(search_frame,text="Search by:",font=("arial",12,"bold"),fg="red",bg="white")
                search_by.grid(row=0,column=0,sticky=W,padx=2,pady=7)
                
                #search
                self.var_com_search=StringVar()

                com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=("arial",12,"bold"),width=18)
                com_txt_search["value"]=("Select Option","Roll No.","Phone","Student_id")
                com_txt_search.current(0)
                com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

                self.var_search=StringVar()
                txt_search=ttk.Entry(search_frame,textvariable=self.var_search,font=("arial",11,"bold"),width=20)
                txt_search.grid(row=0,column=2,sticky=W,padx=5)
        
                btn_search=Button(search_frame,command=self.search_data,text="Search",font=("arial",11,"bold"),width=14,bg="blue",fg="white")
                btn_search.grid(row=0,column=3,padx=5)

                btn_showall=Button(search_frame,command=self.fetch_data,text="Show All",font=("arial",11,"bold"),width=14,bg="blue",fg="white")
                btn_showall.grid(row=0,column=4,padx=5)
                
                #table and scroll

                table_frame=Frame(DatarightFrame,bd=4,relief=RIDGE)
                table_frame.place(x=0,y=100,width=790,height=400)

                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
                self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","rollno","gender","dob","email","phone","address","teacher"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.student_table.xview)
                scroll_y.config(command=self.student_table.yview)

                self.student_table.heading("dep",text="Department")
                self.student_table.heading("course",text="Course")
                self.student_table.heading("year",text="Year")
                self.student_table.heading("sem",text="Semester")
                self.student_table.heading("id",text="StudentId")
                self.student_table.heading("name",text="Student Name") 
                self.student_table.heading("div",text="Class Div")
                self.student_table.heading("rollno",text="Roll No.")
                self.student_table.heading("gender",text="Gender")
                self.student_table.heading("dob",text="DOB")
                self.student_table.heading("email",text="Email")
                self.student_table.heading("phone",text="Phone No")
                self.student_table.heading("address",text="Address")
                self.student_table.heading("teacher",text="Teacher") 

                self.student_table["show"]="headings"

                self.student_table.column("dep",width=100)
                self.student_table.column("course",width=100)
                self.student_table.column("year",width=100)
                self.student_table.column("sem",width=100)
                self.student_table.column("id",width=100)
                self.student_table.column("name",width=100)
                self.student_table.column("div",width=100)
                self.student_table.column("rollno",width=100)
                self.student_table.column("gender",width=100)
                self.student_table.column("dob",width=100)
                self.student_table.column("email",width=100)
                self.student_table.column("phone",width=100)
                self.student_table.column("address",width=100)
                self.student_table.column("teacher",width=100)
                
                
                self.student_table.pack(fill=BOTH,expand=1)
                self.student_table.bind("<ButtonRelease>",self.get_cursor)
                self.fetch_data()

        def add_data(self):
                if(self.var_dep.get()=="" or self.var_email.get()=="" or self.var_std_id.get()==""):  
                        messagebox.showerror("Error","All fied are requied")
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost",user="root",password="Sahil@123",database="logininfo")                       
                                my_cursur=conn.cursor()
                                my_cursur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_std_id.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_rollno.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Sucess","Student has been added!",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)  

        #fetch function
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",user="root",password="Sahil@123",database="logininfo")                       
                my_cursur=conn.cursor()
                my_cursur.execute("select * from student")
                data=my_cursur.fetchall()
                if len(data)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                                self.student_table.insert("",END,values=i)
                        conn.commit()
                conn.close()
        #get cursour
        def get_cursor(self,event=""):
                cursour_row=self.student_table.focus()
                content=self.student_table.item(cursour_row)
                data=content["values"]

                self.var_dep.set(data[0])
                self.var_course.set(data[1])
                self.var_year.set(data[2])
                self.var_semester.set(data[3])
                self.var_std_id.set(data[4])
                self.var_std_name.set(data[5])
                self.var_div.set(data[6])
                self.var_rollno.set(data[7])
                self.var_gender.set(data[8])
                self.var_dob.set(data[9])
                self.var_email.set(data[10])
                self.var_phone.set(data[11])
                self.var_address.set(data[12])
                self.var_teacher.set(data[13])

        def update_data(self):
                if(self.var_dep.get()=="" or self.var_email.get()=="" or self.var_std_id.get()==""):  
                        messagebox.showerror("Error","All fied are requied")
                else:
                        try:
                                update=messagebox.askyesno("Update","Are you sure to update this student data",parent=self.root)
                                if update>0:
                                        conn=mysql.connector.connect(host="localhost",user="root",password="Sahil@123",database="logininfo")                       
                                        my_cursur=conn.cursor()
                                        my_cursur.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Rollno=%s,Gender=%s,DOB=%s,email=%s,Phone=%s,Address=%s,Teacher=%s where student_id=%s",(
                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                                        self.var_rollno.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                        self.var_std_id.get(),
                                                                                                                                                                                                                        ))
                                else:
                                        if not update:
                                                return
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Success","Student successfully updaded",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
        def delete_data(self):
                if self.var_std_id.get()=="":
                         messagebox.showerror("Error","All fied are requied")
                else:
                        try:
                                Delete=messagebox.askyesno("Delete","Are you sure delete this student")
                                if Delete>0:
                                        conn=mysql.connector.connect(host="localhost",user="root",password="Sahil@123",database="logininfo")                       
                                        my_cursur=conn.cursor()
                                        sql="delete from student where student_id=%s"
                                        value=(self.var_std_id.get(),)
                                        my_cursur.execute(sql,value)
                                else:
                                        if not Delete:
                                                return
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Delete","Your Student data has been Deleted",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)        
        #reset
        def reset_data(self):
                self.var_dep.set("Select Department")
                self.var_course.set("Select Course")
                self.var_year.set("Select Year")
                self.var_semester.set("Select Semester")
                self.var_std_id.set("")
                self.var_std_name.set("")
                self.var_div.set("Select Division")
                self.var_rollno.set("")
                self.var_gender.set("")
                self.var_dob.set("")
                self.var_email.set("")
                self.var_phone.set("")
                self.var_address.set("")
                self.var_teacher.set("")

        #search data
        def search_data(self):
                if self.var_com_search.get()=="" or self.var_search.get()=="":
                        messagebox.showerror("Error","Please select option")
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost",user="root",password="Sahil@123",database="logininfo")                       
                                my_cursur=conn.cursor()
                                my_cursur.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                                rows=my_cursur.fetchall()
                                if len(rows)!=0:
                                        self.student_table.delete(*self.student_table.get_children())
                                        for i in rows:
                                                self.student_table.insert("",END,values=i)
                                        conn.commit()
                                conn.close()
                        except Exception as es:
                                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)



                                


#details form
      #  Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
       # Detail_Frame.place(x=500,y=100,width=800,height=560)

if __name__=="__main__":
        root=Tk()
        ob=student(root)
        root.mainloop()