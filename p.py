from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *
from tkinter.scrolledtext import *
from getpass import *

def f1():
	root.withdraw()
	add.deiconify()

def f2():
	add.withdraw()
	root.deiconify()

def f3():
	con=None
	try:
		con=connect('ved.db')
		cursor=con.cursor()
		cursor.execute('select * from emp')
		data=cursor.fetchall()
		if len(data)==0:
			print('No Records')
		for d in data:
			print('\n',d)
	except Exception as e:
		showerror('Issue',e)
	finally:
		if con is not None:
			con.close()

def f4():
	view.withdraw()
	root.deiconify()

def f5():
    root.withdraw()
    update.deiconify()

def f6():
	update.withdraw()
	root.deiconify()

def f7():
	root.withdraw()
	delete.deiconify()

def f8():
	delete.withdraw()
	root.deiconify()

def login():
    while True:
        un = input('Enter username: ')
        pwd = getpass('Enter password: ')

        if un == 'vedd0623' and pwd == '0623vedd':
            print('Login successful')
            return True
        else:
            print('Invalid login details. Please try again.')
            choice = input('Do you want to try again? (y/n): ')
            if choice.lower() != 'y':
                return False

if login():
	root=Tk()
	root.title('C.M.S')
	root.geometry('700x500+50+50')
	root.configure(bg='cyan')
	f=('arial',20,'bold')
	F=('algerian',20,'underline')

	lab_cms=Label(root,text='Contact Management System',font=F,bg='cyan')
	lab_cms.pack(pady=10)

	add=Tk()
	add.title('Add Contact')
	add.geometry('500x500+100+100')
	lab_phno=Label(add,text='enter Phone No.',font=f)
	lab_phno.pack(pady=20)
	ent_phno=Entry(add,font=f)
	ent_phno.pack()
	lab_name=Label(add,text='enter name',font=f)
	lab_name.pack(pady=20)
	ent_name=Entry(add,font=f)
	ent_name.pack()
	lab_email=Label(add,text='enter email address',font=f)
	lab_email.pack(pady=20)
	ent_email=Entry(add,font=f)
	ent_email.pack()

	def save_add():
		con=None
		try:
			con=connect('ved.db')
			cursor=con.cursor()
			try:
				phno=int(ent_phno.get())
			except:
				showerror('WRONG','Enter Valid phno!')
				return
			if phno<=0:
				showerror('WRONG','Phone no. should be non-negative!')
				return

			name=ent_name.get()
			if name=='' or (not name.isalnum()) or name.isnumeric():
				showerror('WRONG','Enter Valid NAME!')
				return

			try:
				email=ent_email.get()
			except:
				showerror('WRONG','Enter Valid Email!')
				return
			if len(email)==0:
				showerror('Issue','Enter email-adrs')
				return

			cursor.execute("insert into emp values(?,?,?)",(phno,name,email))
			con.commit()
			showinfo('SUccess','Record created')
			ent_phno.delete(0,END)
			ent_name.delete(0,END)
			ent_email.delete(0,END)
			ent_phno.focus()
		except Exception as e:
			showerror('Issue',e)
			con.rollback()
		finally:
			if con is not None:
				con.close()

	btn_save=Button(add,text='Save',font=f,command=save_add)
	btn_save.pack(pady=10)
	btn_back=Button(add,text='Back',font=f,command=f2)
	btn_back.pack(pady=10)
	add.withdraw()

	btn_add=Button(root,text='Add',font=F,command=f1,bg='cyan')
	btn_add.place(x=300,y=70)

	btn_view=Button(root,text='View',font=F,command=f3,bg='cyan')
	btn_view.place(x=300,y=160)

	update=Tk()
	update.title('Update Contact')
	update.geometry('600x600+100+100')
	lab_phno_upd=Label(update,text='enter phno',font=f)
	lab_phno_upd.pack(pady=20)
	ent_phno_upd=Entry(update,font=f)
	ent_phno_upd.pack()
	lab_name_upd=Label(update,text='enter name',font=f)
	lab_name_upd.pack(pady=20)
	ent_name_upd=Entry(update,font=f)
	ent_name_upd.pack()
	lab_email_upd=Label(update,text='enter email',font=f)
	lab_email_upd.pack(pady=20)
	ent_email_upd=Entry(update,font=f)
	ent_email_upd.pack()

	def save_check():
		con=None
		try:
			con=connect('ved.db')
			cursor = con.cursor()
			try:
				emp_phno = int(ent_phno_upd.get())
			except:
				showerror('WRONG','Enter Valid phno!')
				return
			if emp_phno<=0:
				showerror('WRONG','Min. phno should be non-negative!')
				return
			cursor.execute("SELECT name, email FROM emp WHERE phno = ?", (emp_phno,))
			data = cursor.fetchone()
			if data:
				ent_name_upd.delete(0, END)
				ent_name_upd.insert(0, data[0])
				ent_email_upd.delete(0, END)
				ent_email_upd.insert(0, data[1])
			else:
				showerror("Error", f"Employee with phno {emp_phno} not found")
		except Exception as e:
			showerror('Issue',e)
		finally:
			if con is not None:
				con.close()

	btn_save_check=Button(update,text='check',font=f,command=save_check)
	btn_save_check.pack(pady=10)

	def save_update():
		con=None
		try:
			con=connect('ved.db')
			cursor = con.cursor()
			try:
				emp_phno = int(ent_phno_upd.get())
			except:
				showerror('WRONG','Enter Valid phno')
				return
			if emp_phno <=0:
				showerror('WRONG','Phone no. should be non-negative!')
				return
	
			new_name = ent_name_upd.get()
			if new_name=='' or (not new_name.isalnum()) or new_name.isnumeric():
				showerror('WRONG','Enter Valid Name')
				return
			try:
				new_email = ent_email_upd.get()
			except:
				showerror('WRONG','Enter Valid Email!')
				return
			if len(new_email)==0:
				showerror('Issue','Enter email-adrs')
				return

			cursor.execute("UPDATE emp SET name = ?, email = ? WHERE phno = ?", (new_name, new_email, emp_phno))
			con.commit()
			showinfo("Success", f"emp with phno {emp_phno} updated successfully")
			ent_phno_upd.delete(0,END)
			ent_name_upd.delete(0,END)
			ent_email_upd.delete(0,END)
			ent_phno_upd.focus()
		except Exception as e:
			showerror('Update error',str(e))
		finally:
			if con is not None:
				con.close()

	btn_save_upd=Button(update,text='Save',font=f,command=save_update)
	btn_save_upd.pack(pady=10)
	btn_back_upd=Button(update,text='Back',font=f,command=f6)
	btn_back_upd.pack(pady=10)
	update.withdraw()

	btn_update=Button(root,text='Update',font=F,command=f5,bg='cyan')
	btn_update.place(x=300,y=250)

	delete=Tk()
	delete.title('Delete Contact')
	delete.geometry('500x500+100+100')
	lab_phno_del=Label(delete,text='enter phno',font=f)
	lab_phno_del.pack(pady=20)
	ent_phno_del=Entry(delete,font=f)
	ent_phno_del.pack()

	def delete_emp():
		con = None
		try:
			con = connect("ved.db")
			cursor = con.cursor()
			try:
				phno_to_delete = int(ent_phno_del.get())
			except:
				showerror('WRONG','Enter Valid phno')
				return
			if phno_to_delete <=0:
				showerror('WRONG','Phone no. should be non-negative!')
				return
			cursor.execute("DELETE FROM emp WHERE phno = ?", (phno_to_delete,))
			con.commit()
			showinfo('Success', 'Student record deleted successfully')
			ent_phno_del.delete(0, END)
			ent_phno_del.focus()
		except Exception as e:
			showerror('Deletion Error', str(e))
		finally:
			if con is not None:
				con.close()

	btn_save_del=Button(delete,text='Delete',font=f,command=delete_emp)
	btn_save_del.pack(pady=10)

	def delete_all():
		con = None
		try:
			con = connect("ved.db")
			cursor = con.cursor()
			cursor.execute("DELETE FROM emp")
			con.commit()
			showinfo('Success', 'Student records deleted successfully')
		except Exception as e:
			showerror('Deletion Error', str(e))
		finally:
			if con is not None:
				con.close()

	btn_save_del=Button(delete,text='Delete All',font=f,command=delete_all)
	btn_save_del.pack(pady=10)
	btn_back_del=Button(delete,text='Back',font=f,command=f8)
	btn_back_del.pack(pady=10)
	delete.withdraw()

	btn_delete=Button(root,text='Delete',font=F,command=f7,bg='cyan')
	btn_delete.place(x=300,y=350)

	def exit():
		if askokcancel('Quit','Do u want to exit?'):
			root.destroy()
			add.destroy()
			update.destroy()
			delete.destroy()
	root.protocol('WM_DELETE_WINDOW',exit)
	add.protocol('WM_DELETE_WINDOW',exit)
	update.protocol('WM_DELETE_WINDOW',exit)
	delete.protocol('WM_DELETE_WINDOW',exit)

	root.mainloop()
else:
	print('Login Failed!')