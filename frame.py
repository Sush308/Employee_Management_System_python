from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title("Employee Management System")

        # Creating variables
        self.var_dept = StringVar()
        self.var_name = StringVar()
        self.var_designition = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_married = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_idproofcomb = StringVar()
        self.var_idproof = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()

        self.var_txt_com_search_by = StringVar()
        self.var_txt_search_by = StringVar()

        # heading
        lbl_head = Label(self.root, text='EMPLOYEE MANAGEMENT SYSTEM', font=('times new roman', 37, 'bold'),
                         fg='white', bg='black', relief=RIDGE)
        lbl_head.place(x=10, y=10, width=1340, height=80)

        # Creating Mainframe
        main_frame = Frame(self.root, bg='pink', bd=3, relief=RIDGE)
        main_frame.place(x=10, y=100, width=1340, height=600)

        # Creating Upper frame
        upper_frame = LabelFrame(main_frame, bg='white', bd=2, relief=RIDGE, text='Employee Information',
                                 font=('times new roman', 12, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1310, height=250)

        # Department
        lbl_dept = Label(upper_frame, text='Department', font=('arial', 10, 'bold'), bg='white')
        lbl_dept.grid(row=0, column=0, padx=15, sticky=W)

        combo_dept = ttk.Combobox(upper_frame, textvariable=self.var_dept, font=('arial', 10), width=28)
        combo_dept['value'] = ('Select Department', 'HR', 'Manager', 'Software Engineer')
        combo_dept.current(0)
        combo_dept.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Name
        lbl_name = Label(upper_frame, text=' Full Name', font=('arial', 10, 'bold'), bg='white')
        lbl_name.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        txt_name = ttk.Entry(upper_frame, textvariable=self.var_name, font=('arial', 10), width=30)
        txt_name.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # Designition
        lbl_desi = Label(upper_frame, text=' Designation', font=('arial', 10, 'bold'), bg='white')
        lbl_desi.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        txt_designation = ttk.Entry(upper_frame, textvariable=self.var_designition, font=('arial', 10), width=30)
        txt_designation.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Email
        lbl_email = Label(upper_frame, text=' Email', font=('arial', 10, 'bold'), bg='white')
        lbl_email.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        txt_email = ttk.Entry(upper_frame, textvariable=self.var_email, font=('arial', 10), width=30)
        txt_email.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # Address
        lbl_address = Label(upper_frame, text=' Address', font=('arial', 10, 'bold'), bg='white')
        lbl_address.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        txt_address = ttk.Entry(upper_frame, textvariable=self.var_address, font=('arial', 10), width=30)
        txt_address.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # Married
        lbl_married = Label(upper_frame, text='Married Status', font=('arial', 10, 'bold'), bg='white')
        lbl_married.grid(row=2, column=2, padx=15, sticky=W)

        combo_married = ttk.Combobox(upper_frame, textvariable=self.var_married, font=('arial', 10), width=28)
        combo_married['value'] = ('Married', 'Unmarried')
        combo_married.current(0)
        combo_married.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        # Date of birth
        lbl_dob = Label(upper_frame, text=' Date of Birth', font=('arial', 10, 'bold'), bg='white')
        lbl_dob.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        txt_dob = ttk.Entry(upper_frame, textvariable=self.var_dob, font=('arial', 10), width=30)
        txt_dob.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Date of Joining
        lbl_doj = Label(upper_frame, text=' Date of Joining', font=('arial', 10, 'bold'), bg='white')
        lbl_doj.grid(row=3, column=2, padx=10, pady=10, sticky=W)

        txt_doj = ttk.Entry(upper_frame, textvariable=self.var_doj, font=('arial', 10), width=30)
        txt_doj.grid(row=3, column=3, padx=10, pady=10, sticky=W)

        # Combo Id_proof
        combo_id_proof = ttk.Combobox(upper_frame, textvariable=self.var_idproofcomb,
                                      font=('arial', 10, 'bold'), width=15)
        combo_id_proof['value'] = ('Aadhar Card', 'PAN Card', 'Ration Card', 'Voting Card')
        combo_id_proof.current(0)
        combo_id_proof.grid(row=4, column=0, padx=15, pady=10, sticky=W)

        # Text field Id_proof
        txt_id_proof = ttk.Entry(upper_frame, textvariable=self.var_idproof, font=('arial', 10), width=30)
        txt_id_proof.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        # Gender
        lbl_gender = Label(upper_frame, text='Gender', font=('arial', 10, 'bold'), bg='white')
        lbl_gender.grid(row=4, column=2, padx=15, sticky=W)

        combo_gender = ttk.Combobox(upper_frame, textvariable=self.var_gender, font=('arial', 10), width=28)
        combo_gender['value'] = ('Male', 'Female')
        combo_gender.current(0)
        combo_gender.grid(row=4, column=3, padx=10, pady=10, sticky=W)

        # Phone
        lbl_phone = Label(upper_frame, text=' Phone No.', font=('arial', 10, 'bold'), bg='white')
        lbl_phone.grid(row=0, column=4, padx=10, pady=10, sticky=W)

        txt_phone = ttk.Entry(upper_frame, textvariable=self.var_phone, font=('arial', 10), width=30)
        txt_phone.grid(row=0, column=5, padx=10, pady=10, sticky=W)

        # Country
        lbl_country = Label(upper_frame, text=' Country', font=('arial', 10, 'bold'), bg='white')
        lbl_country.grid(row=1, column=4, padx=10, pady=10, sticky=W)

        txt_country = ttk.Entry(upper_frame, textvariable=self.var_country, font=('arial', 10), width=30)
        txt_country.grid(row=1, column=5, padx=10, pady=10, sticky=W)

        # Salary
        lbl_ctc = Label(upper_frame, text=' Salary (CTC)', font=('arial', 10, 'bold'), bg='white')
        lbl_ctc.grid(row=2, column=4, padx=10, pady=10, sticky=W)

        txt_ctc = ttk.Entry(upper_frame, textvariable=self.var_salary, font=('arial', 10), width=30)
        txt_ctc.grid(row=2, column=5, padx=10, pady=10, sticky=W)

        # Frame for button
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE)
        button_frame.place(x=1110, y=5, width=185, height=213)

        # Add Button
        btn_add = Button(button_frame, text='Save', command=self.add_data, font=('arial', 12, 'bold'),
                         bg='blue', fg='white', width=16)
        btn_add.grid(row=0,  column=0, padx=5, pady=9)

        # Update Button
        btn_update = Button(button_frame, text='Update', command=self.update_data, font=('arial', 12, 'bold'),
                            bg='blue', fg='white', width=16)
        btn_update.grid(row=1, column=0, padx=5, pady=9)

        # Delete Button
        btn_delete = Button(button_frame, text='Delete', command=self.delete_data, font=('arial', 12, 'bold'),
                            bg='blue', fg='white', width=16)
        btn_delete.grid(row=2, column=0, padx=5, pady=9)

        # Clear Button
        btn_clear = Button(button_frame, text='Clear', command=self.reset_data,  font=('arial', 12, 'bold'), bg='blue', fg='white', width=16)
        btn_clear.grid(row=3, column=0, padx=5, pady=9)

        # Down frame
        down_frame = LabelFrame(main_frame, bg='white', bd=2, relief=RIDGE, text='Employee Information Table',
                                font=('times new roman', 12, 'bold'), fg='red')
        down_frame.place(x=10, y=265, width=1310, height=310)

        # Search Frame
        search_frame = LabelFrame(down_frame, bg='white', bd=2, relief=RIDGE, text='Search Employee',
                                  font=('times new roman', 12, 'bold'), fg='red')
        search_frame.place(x=10, y=0, width=1280, height=60)

        # Search
        search_by = Label(search_frame, font=('arial', 10, 'bold'), text="Search by:", bg='red', fg='white')
        search_by.grid(row=0, column=0, padx=5, sticky=W)

        txt_com_search_by = ttk.Combobox(search_frame, state="readonly",textvariable=self.var_txt_com_search_by, font=('arial', 10, 'bold'))
        txt_com_search_by['value'] = ('Select option', 'Phone', 'id_proof')
        txt_com_search_by.current(0)
        txt_com_search_by.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        txt_search_by = ttk.Entry(search_frame, textvariable=self.var_txt_search_by, font=('arial', 10, 'bold'))
        txt_search_by.grid(row=0, column=2, padx=10)

        # #Search Button
        search_btn = Button(search_frame, text="Search", command=self.search_data, font=('arial', 10, 'bold'))
        search_btn.grid(row=0, column=3, padx=10)

        # Search All Button
        btn_search_all = Button(search_frame, text="Show All", command=self.display_all, font=('arial', 10, 'bold'))
        btn_search_all.grid(row=0, column=4, padx=10)

        # Frame for table
        table_frame = LabelFrame(down_frame, bd=2, relief=RIDGE)
        table_frame.place(x=10, y=65, width=1280, height=210)

        x_scroll = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        y_scroll = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame, columns=("dept", "name", "desi", "email", "address", "married",
                                                                 "dob", "doj", "idproofcomb", "idproof", "gender",
                                                                 "phone", "country", "salary",),
                                           xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

        x_scroll.pack(side=BOTTOM, fill=X)
        y_scroll.pack(side=RIGHT, fill=Y)

        x_scroll.config(command=self.employee_table.xview)
        y_scroll.config(command=self.employee_table.yview)

        self.employee_table.heading('dept', text='Department')
        self.employee_table.heading('name', text='Full Name')
        self.employee_table.heading('desi', text='Designation')
        self.employee_table.heading('email', text='Email')
        self.employee_table.heading('address', text='Address')
        self.employee_table.heading('married', text='Married Status')
        self.employee_table.heading('dob', text='Date Of Birth')
        self.employee_table.heading('doj', text='Date Of Joining')
        self.employee_table.heading('idproofcomb', text='ID Type')
        self.employee_table.heading('idproof', text='ID Proof')
        self.employee_table.heading('gender', text='Gender')
        self.employee_table.heading('phone', text='Phone')
        self.employee_table.heading('country', text='Country')
        self.employee_table.heading('salary', text='Salary')

        self.employee_table['show'] = 'headings'

        self.employee_table.column("dept", width=60)
        self.employee_table.column('name', width=110)
        self.employee_table.column('desi', width=80)
        self.employee_table.column('email', width=100)
        self.employee_table.column('address', width=100)
        self.employee_table.column('married', width=65)
        self.employee_table.column('dob', width=60)
        self.employee_table.column('doj', width=80)
        self.employee_table.column('idproofcomb', width=70)
        self.employee_table.column('idproof', width=70)
        self.employee_table.column('gender', width=40)
        self.employee_table.column('phone', width=50)
        self.employee_table.column('country', width=40)
        self.employee_table.column('salary', width=40)

        self.employee_table.pack(fill=BOTH, expand=1)

        self.employee_table.bind('<ButtonRelease>', self.auto_fill)

        self.display_all()

    def add_data(self):
        if self.var_dept.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root',
                                               password='Sushil@1432', database='employee')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into emp values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_dept.get(),
                    self.var_name.get(),
                    self.var_designition.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_married.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_idproofcomb.get(),
                    self.var_idproof.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_country.get(),
                    self.var_salary.get()))

                conn.commit()
                self.display_all()
                conn.close()
                messagebox.showinfo('Success', 'Employee hes been added!', parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)

    def display_all(self):
        conn = mysql.connector.connect(host='localhost', username='root',
                                       password='Sushil@1432', database='employee')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from emp')
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def auto_fill(self, event=""):
        pointing_row = self.employee_table.focus()
        content = self.employee_table.item(pointing_row)
        data = content['values']

        self.var_dept.set(data[0]),
        self.var_name.set(data[1]),
        self.var_designition.set(data[2]),
        self.var_email.set(data[3]),
        self.var_address.set(data[4]),
        self.var_married.set(data[5]),
        self.var_dob.set(data[6]),
        self.var_doj.set(data[7]),
        self.var_idproofcomb.set(data[8]),
        self.var_idproof.set(data[9]),
        self.var_gender.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_country.set(data[12]),
        self.var_salary.set(data[13])

    def update_data(self):
        if self.var_dept.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure update this employee data...')
                if update > 0:
                    conn = mysql.connector.connect(host='localhost', username='root',
                                                   password='Sushil@1432', database='employee')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update emp set Department=%s, Name=%s, Designition=%s, Email=%s, Address=%s,'
                                      ' Married_status=%s, DOB=%s, DOJ=%s, id_proof_type=%s, Gender=%s, Phone=%s, '
                                      'Country=%s, Salary=%s where id_proof=%s', (
                                                                                    self.var_dept.get(),
                                                                                    self.var_name.get(),
                                                                                    self.var_designition.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_married.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_doj.get(),
                                                                                    self.var_idproofcomb.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_country.get(),
                                                                                    self.var_salary.get(),
                                                                                    self.var_idproof.get()))
                else:
                    if not update:
                        return
                conn.commit()
                self.display_all()
                conn.close()
                messagebox.showinfo('success', 'Employee Data Successfully Updated...', parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)

    def delete_data(self):
        if self.var_idproof.get() == "":
            messagebox.showerror('Error', 'All Fields Are Required...', parent=self.root)
        else:
            try:
                delete = messagebox.askyesno('Delete', 'Are you Sure Delete this Record...', parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host='localhost', username='root',
                                                   password='Sushil@1432', database='employee')
                    my_cursor = conn.cursor()
                    my_cursor.execute('delete from emp where id_proof=%s', (self.var_idproof.get(),))
                else:
                    if not delete:
                        return
                conn.commit()
                self.display_all()
                conn.close()
                messagebox.showinfo('Delete', 'Employee Data Successfully Deleted...', parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)

    def reset_data(self):
        self.var_dept.set("Select Department"),
        self.var_name.set(""),
        self.var_designition.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        self.var_married.set("Married"),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_idproofcomb.set("Select ID Proof"),
        self.var_idproof.set("")
        self.var_gender.set(""),
        self.var_phone.set(""),
        self.var_country.set(""),
        self.var_salary.set("")

    def search_data(self):
        if self.var_txt_com_search_by.get() == "" or self.var_txt_search_by.get() == "":
            messagebox.showerror('Error', 'please Select Option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root',
                                               password='Sushil@1432', database='employee')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from emp where ' +str(self.var_txt_com_search_by.get())+" LIKE '%"
                                  +str(self.var_txt_search_by.get()+"%'"))
                all_rows = my_cursor.fetchall()
                if len(all_rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in all_rows:
                        self.employee_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except EXCEPTION as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
