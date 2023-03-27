from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter.scrolledtext as st
import tkinter.ttk as ttk
import time
import tkinter.scrolledtext as sc

root = Tk()
root.geometry("1300x820")
root.resizable(False,False)
root.title("System db controller v0.1")
root.config(bg='white')
root.iconbitmap("C://Users//bahman//Desktop//db//test/R.jpg")

#defs
def connect():
    h = host_en_v.get()
    u = user_en_v.get()
    p = password_en_v.get()
    try:
        conn = mysql.connector.connect(
            host = str(h),
            user = str(u),
            passwd = str(p),
        )
        messagebox.showinfo('Server MySQL','تم الاتصال بالسيرفر بنجاح!')
    except mysql.connector.Error as e:
        messagebox.showerror('Error',str(e))

def shows_dbs():
    def s():
        h = host_en_v.get()
        u = user_en_v.get()
        p = password_en_v.get()
        try:
            conn = mysql.connector.connect(
                host = str(h),
                user = str(u),
                passwd = str(p),
                )
            cur = conn.cursor()
            cur.execute("SHOW DATABASES")
            show_databases.insert("end",'All databases found: \n \n','zero')
            for x in cur:
                show_databases.insert("end",'[+]'+str(x)+'\n \n','one')
            show_databases.insert('end','=========================>\n \n \n','two')
            messagebox.showinfo('Server MySQL','تم اظهار كل قواعد البيانات بنجاح!')
        except mysql.connector.Error as e:
            messagebox.showerror('Error',str(e))
    q = messagebox.askquestion('Server MySQL','هل تريد اظهار كل قواعد البيانات?')
    if q == 'yes':
        s()
    else:
        messagebox.showinfo('Error','تم الغاء الامر.')


def hide_dbs():
    pass

def create_db():
    h = host_en_v.get()
    u = user_en_v.get()
    p = password_en_v.get()
    db_n = c_db_en_v.get()
    try:
        conn = mysql.connector.connect(
            host = str(h),
            user = str(u),
            passwd = str(p),
        )
        cur = conn.cursor()
        cur.execute("CREATE DATABASE {}".format(db_n))
        messagebox.showinfo('Server MySQL','بنجاح '+'( '+db_n+' )'+' تم انشاء قاعدة البيانات')
    except mysql.connector.Error as e:
        messagebox.showerror('Error',str(e))

def delete_db():
    h = host_en_v.get()
    u = user_en_v.get()
    p = password_en_v.get()
    db_n = d_db_en_v.get()
    try:
        conn = mysql.connector.connect(
            host = str(h),
            user = str(u),
            passwd = str(p),
        )
        cur = conn.cursor()
        cur.execute("DROP DATABASE {}".format(db_n))
        messagebox.showinfo('Server MySQL','بنجاح '+'( '+db_n+' )'+' تم حذف قاعدة البيانات!')
    except mysql.connector.Error as e:
        messagebox.showerror('Error',str(e))

def create_table():
    h = host_en_v.get()
    u = user_en_v.get()
    p = password_en_v.get()
    db_n = db_n_en1_v.get()
    tb_name = tb_n_en1_v.get()
    c_n = c_n_en1_v.get()
    c_t = c_t_en1_v.get()
    c_l = c_l_en1_v.get()
    c_d = c_d_en1_v.get()
    c_i = c_index_en1_v.get()
    try:
        conn = mysql.connector.connect(
            host = str(h),
            user = str(u),
            passwd = str(p),
            db=str(db_n),
        )
        cur = conn.cursor()
        if c_d == "current_timestamp":
            cur.execute("CREATE TABLE {} ({} {} ({}) default {} )".format(tb_name,c_n,c_t,c_l,c_d))
            messagebox.showinfo('Server MySQL','بنجاح '+'( '+tb_name+' )'+' تم انشاء الجدول')
        if c_d == str(''):
            cur.execute("CREATE TABLE {} ({} {} ({}) {} {})".format(tb_name,c_n,c_t,c_l,c_d,c_i))
            messagebox.showinfo('Server MySQL','بنجاح '+'( '+tb_name+' )'+' تم انشاء الجدول')
    except mysql.connector.Error as e:
        messagebox.showerror('Error',str(e))

def add_columen():
    h = host_en_v.get()
    u = user_en_v.get()
    p = password_en_v.get()
    db_n = db_n_en2_v.get()
    tb_name = tb_n_en2_v.get()
    c_n = c_n_en2_v.get()
    c_t = c_t_en2_v.get()
    c_l = c_l_en2_v.get()
    c_d = c_d_en2_v.get()
    c_i = c_index_en2_v.get()
    try:
        conn = mysql.connector.connect(
            host = str(h),
            user = str(u),
            passwd = str(p),
            db=str(db_n),
        )
        cur = conn.cursor()
        if c_d == "current_timestamp":
            cur.execute("ALTER TABLE {} ADD ({} {} ({}) default {} )".format(tb_name,c_n,c_t,c_l,c_d))
            messagebox.showinfo('Server MySQL','بنجاح '+'( '+c_n+' )'+' تم اضافة الحقل')
        if c_d == str(''):
            cur.execute("ALTER TABLE {} ADD ({} {} ({}) {} {})".format(tb_name,c_n,c_t,c_l,c_d,c_i))
            messagebox.showinfo('Server MySQL','بنجاح '+'( '+c_n+' )'+' تم اضافة الحقل')
    except mysql.connector.Error as e:
        messagebox.showerror('Error',str(e))


def show_db_tables():
    h = host_en_v.get()
    u = user_en_v.get()
    p = password_en_v.get()
    db_n = tbs_db_en_v.get()
    try:
        conn = mysql.connector.connect(
            host = str(h),
            user = str(u),
            passwd = str(p),
            db=str(db_n),
            )
        sz.insert('end','( '+str(db_n)+' )'+' tables: \n \n','one')
        cur = conn.cursor()
        cur.execute("SHOW TABLES")
        for x in cur:
            sz.insert('end','[+] '+str(x)+'\n \n','zero')
        sz.insert('end','=========================>\n \n \n','three')
        messagebox.showinfo("Server Mysql"," بنجاح "+"( "+db_n+" )"+" تم اظهار جداول قاعدة البيانات!")
    except mysql.connector.Error as e:
        messagebox.showerror('Error',str(e))



#Right panel
right_panel = Frame(root,bg='whitesmoke')
right_panel.place(x=770,width=530,height=850)
right_panel_image = PhotoImage(file="C://Users//bahman//Desktop//MySQL Server Controll v1.0.0//png.png")
right_panel_image_playing = Label(root,image=right_panel_image,bg='whitesmoke')
right_panel_image_playing.place(x=770,y=160,width=530)

#title
title = Label(root, text='Server MySQL v1.0.0 [ System Db-s controller ]',bg='#333',fg='white',font=("Courier",19))
title.pack(fill=X)

#Connect Frame
connect_f = Frame(root,bg='whitesmoke',relief=SOLID,bd=1)
connect_f.place(x=20,y=50,width=350,height=250)
connect_f_title = Label(connect_f,text='Server connecting',bg='#421F40',fg='white',font=("Courier",13))
connect_f_title.pack(fill=X)
host = Label(connect_f, text='Host: ',background='whitesmoke',fg='black',font=("Tajawal",14))
host.place(x=10,y=35)
user = Label(connect_f, text='User: ',background='whitesmoke',fg='black',font=("Tajawal",14))
user.place(x=10,y=80)
password = Label(connect_f, text='Password: ',background='whitesmoke',fg='black',font=("Tajawal",14))
password.place(x=10,y=125)


host_en_v = StringVar()
host_en_v.set('localhost')
host_en = Entry(connect_f,
textvariable=host_en_v,
relief=SOLID,
justify=CENTER,
bd=1)
host_en.place(x=70,
y=40,
width=200)

user_en_v = StringVar()
user_en_v.set('root')
user_en = Entry(connect_f,
textvariable=user_en_v,
relief=SOLID,
justify=CENTER,
bd=1)

user_en.place(x=70,
y=85,
width=200)

password_en_v = StringVar()
password_en = Entry(connect_f,
textvariable=password_en_v,
relief=SOLID,
bd=1,
justify=CENTER,)
password_en.place(x=110,
y=130,
width=160)

button1 = Button(connect_f, text='Connect Now', bg='#421F40',fg='white',command=connect)
button1.place(x=10,y=170,height=70,width=330)

#Database controll Frame
db_contr_f = Frame(root,bg='whitesmoke',relief=SOLID,bd=1)
db_contr_f.place(x=400,y=50,width=350,height=250)
db_contr_f_title = Label(db_contr_f,text='Databasese Controll',bg='#196F90',fg='white',font=("Courier",13))
db_contr_f_title.pack(fill=X)
show_dbs = Label(db_contr_f, text='Show: ',background='whitesmoke',fg='black',font=("Tajawal",14))
show_dbs.place(x=10,y=35)
c_db = Label(db_contr_f, text='Create-db: ',background='whitesmoke',fg='black',font=("Tajawal",14))
c_db.place(x=10,y=80)
d_db = Label(db_contr_f, text='Drop-db: ',background='whitesmoke',fg='black',font=("Tajawal",14))
d_db.place(x=10,y=125)

c_db_en_v = StringVar()
c_db_name_en = Entry(db_contr_f,
textvariable=c_db_en_v,
relief=SOLID,
justify=CENTER,
bd=1,)

c_db_name_en.place(x=110,
y=85,
width=160)

d_db_en_v = StringVar()
d_db_name_en = Entry(db_contr_f,
textvariable=d_db_en_v,
relief=SOLID,
bd=1,
justify=CENTER,)
d_db_name_en.place(x=100,
y=130,
width=170)

show_dbs_b = Button(db_contr_f,text='All Db-s',relief=SOLID,bd=1,command=shows_dbs)
show_dbs_b.place(x=70,y=37,width=150)

hide_dbs_b = Button(db_contr_f,text='Hide',bg='#196F90',fg='white',relief=SOLID,bd=1)
hide_dbs_b.place(x=230,y=37,width=110)

c_db_b = Button(db_contr_f, text='Create', bg='#196F90',fg='white',relief=SOLID,bd=1,command=create_db)
c_db_b.place(x=280,y=80,width=60,height=30)

d_db_b = Button(db_contr_f, text='Delete', bg='#196F90',fg='white',relief=SOLID,bd=1,command=delete_db)
d_db_b.place(x=280,y=125,width=60,height=30)

#Create table Frame
create_table_f = Frame(root,bg='whitesmoke',relief=SOLID,bd=1)
create_table_f.place(x=20,y=310,width=350,height=250)
create_table_f_title = Label(create_table_f,text='Create table',bg='#0496A4',fg='white',font=("Courier",13))
create_table_f_title.pack(fill=X)
db_name1 = Label(create_table_f, text='Db-name: ',background='whitesmoke',fg='black',font=("Tajawal",13))
db_name1.place(x=10,y=35)
tb_name1 = Label(create_table_f, text='Table-n: ',background='whitesmoke',fg='black',font=("Tajawal",13))
tb_name1.place(x=10,y=70)
c_n1 = Label(create_table_f, text='Col-name: ',background='whitesmoke',fg='black',font=("Tajawal",13))
c_n1.place(x=10,y=105)
c_t1 = Label(create_table_f, text='Col-type: ',background='whitesmoke',fg='black',font=("Tajawal",13))
c_t1.place(x=10,y=140)
c_l1 = Label(create_table_f, text='Col-length: ',background='whitesmoke',fg='black',font=("Tajawal",13))
c_l1.place(x=10,y=175)
c_d1 = Label(create_table_f,text='Default:',background='whitesmoke',fg='black',font=("Tajawal",13))
c_d1.place(x=10,y=210)
c_index = Label(create_table_f,text='Index:',background='whitesmoke',fg='black',font=("Tajawal",13))
c_index.place(x=160,y=210)

db_n_en1_v = StringVar()
db_n_en1 = Entry(create_table_f,textvariable=db_n_en1_v,relief=SOLID,bd=1,justify=CENTER)
db_n_en1.place(x=90,y=38,width=130)

tb_n_en1_v = StringVar()
tb_n_en1 = Entry(create_table_f,textvariable=tb_n_en1_v,relief=SOLID,bd=1,justify=CENTER)
tb_n_en1.place(x=90,y=73,width=130)

c_n_en1_v = StringVar()
c_n_en1 = Entry(create_table_f,textvariable=c_n_en1_v,relief=SOLID,bd=1,justify=CENTER)
c_n_en1.place(x=100,y=108,width=120)

c_t_en1_v = StringVar()
c_t_en1 = ttk.Combobox(create_table_f,textvariable=c_t_en1_v,justify=CENTER)
c_t_en1['values'] = ("int","varchar","text","date","timestamp","decimal","float","bigint","boolean","serial","year","date","datetime")
c_t_en1.place(x=90,y=140,width=130)

c_l_en1_v = StringVar()
c_l_en1 = Entry(create_table_f,textvariable=c_l_en1_v,relief=SOLID,bd=1,justify=CENTER)
c_l_en1.place(x=100,y=178,width=120)

c_d_en1_v = StringVar()
c_d_en1 = ttk.Combobox(create_table_f,textvariable=c_d_en1_v,justify=CENTER)
c_d_en1['values'] = ("current_timestamp")
c_d_en1.place(x=80,y=213,width=70)

c_index_en1_v = StringVar()
c_index_en1 = ttk.Combobox(create_table_f,textvariable=c_index_en1_v,justify=CENTER)
c_index_en1['values'] = ("primary key","unique")
c_index_en1.place(x=220,y=213,width=70)

c_t_f_b1 = Button(create_table_f, text='Add one columen \n and create', bg='#0496A4',fg='white',relief=SOLID,bd=1,command=create_table)
c_t_f_b1.place(x=230,y=38,width=110,height=160)

#Add columens Frame
add_columen_f = Frame(root,bg='whitesmoke',relief=SOLID,bd=1)
add_columen_f.place(x=400,y=310,width=350,height=250)
add_columen_f_title = Label(add_columen_f,text='Add columen',bg='#8669AF',fg='white',font=("Courier",13))
add_columen_f_title.pack(fill=X)
db_name2 = Label(add_columen_f, text='Db-name: ',background='whitesmoke',fg='black',font=("Tajawal",13))
db_name2.place(x=10,y=35)
tb_name2 = Label(add_columen_f, text='Table-n: ',background='whitesmoke',fg='black',font=("Tajawal",13))
tb_name2.place(x=10,y=70)
c_n2 = Label(add_columen_f, text='Col-name: ',background='whitesmoke',fg='black',font=("Tajawal",13))
c_n2.place(x=10,y=105)
c_t2 = Label(add_columen_f, text='Col-type: ',background='whitesmoke',fg='black',font=("Tajawal",13))
c_t2.place(x=10,y=140)
c_l2 = Label(add_columen_f, text='Col-length: ',background='whitesmoke',fg='black',font=("Tajawal",13))
c_l2.place(x=10,y=175)
c_d2 = Label(add_columen_f,text='Default:',background='whitesmoke',fg='black',font=("Tajawal",13))
c_d2.place(x=10,y=210)
c_index2 = Label(add_columen_f,text='Index:',background='whitesmoke',fg='black',font=("Tajawal",13))
c_index2.place(x=160,y=210)

db_n_en2_v = StringVar()
db_n_en2 = Entry(add_columen_f,textvariable=db_n_en2_v,relief=SOLID,bd=1,justify=CENTER)
db_n_en2.place(x=90,y=38,width=130)

tb_n_en2_v = StringVar()
tb_n_en2 = Entry(add_columen_f,textvariable=tb_n_en2_v,relief=SOLID,bd=1,justify=CENTER)
tb_n_en2.place(x=90,y=73,width=130)

c_n_en2_v = StringVar()
c_n_en2 = Entry(add_columen_f,textvariable=c_n_en2_v,relief=SOLID,bd=1,justify=CENTER)
c_n_en2.place(x=100,y=108,width=120)

c_t_en2_v = StringVar()
c_t_en2 = ttk.Combobox(add_columen_f,textvariable=c_t_en2_v,justify=CENTER)
c_t_en2['values'] = ("int","varchar","text","date","timestamp","decimal","float","bigint","boolean","serial","year","date","datetime")
c_t_en2.place(x=100,y=108+27+8,width=120)

c_l_en2_v = StringVar()
c_l_en2 = Entry(add_columen_f,textvariable=c_l_en2_v,relief=SOLID,bd=1,justify=CENTER)
c_l_en2.place(x=100,y=178,width=120)

c_d_en2_v = StringVar()
c_d_en2 = ttk.Combobox(add_columen_f,textvariable=c_d_en2_v,justify=CENTER)
c_d_en2['values'] = ("current_timestamp")
c_d_en2.place(x=80,y=213,width=70)

c_index_en2_v = StringVar()
c_index_en2 = ttk.Combobox(add_columen_f,textvariable=c_index_en2_v,justify=CENTER)
c_index_en2['values'] = ("primary key","unique")
c_index_en2.place(x=220,y=213,width=70)

c_t_f_b2 = Button(add_columen_f, text='Add one columen \n into table', bg='#8669AF',fg='white',relief=SOLID,bd=1,command=add_columen)
c_t_f_b2.place(x=230,y=38,width=110,height=160)

#Show db tables Frame
show_db_tables_f = Frame(root,bg='whitesmoke',relief=SOLID,bd=1)
show_db_tables_f.place(x=20,y=570,width=350,height=250)
show_db_tables_f_title = Label(show_db_tables_f,text='Show Db tables',bg='#869AF6',fg='white',font=("Courier",13))
show_db_tables_f_title.pack(fill=X)
db_name_l = Label(root,text='Db-name: ',fg='black',bg='whitesmoke',font=("Tajawal",12))
db_name_l.place(x=30,y=610)
tables_found = Label(root,text='Tables found: ',fg='black',bg='whitesmoke',font=("Tajawal",12))
tables_found.place(x=30,y=650)
tbs_db_en_v = StringVar()
tbs_db_en = Entry(root, textvariable=tbs_db_en_v,relief=SOLID,bd=1,justify=CENTER)
tbs_db_en.place(x=110,y=614)
tbs_b = Button(root, text='Show tables',bg='#869AF6',fg='white',command=show_db_tables)
tbs_b.place(x=240,y=611,width=120)

sz = sc.ScrolledText(show_db_tables_f)
sz['relief'] = 'solid'
sz['font'] = ("Tajawal",9)
sz.tag_config('zero',foreground='green',background='white')
sz.tag_config('one',foreground='red',background='whitesmoke')
sz.tag_config('three',foreground='blue',background='whitesmoke')
sz.place(x=10,y=110,width=330,height=130)

#Show dbs
show_dbs_f = Frame(root, background='whitesmoke',relief=SOLID,bd=1)
show_dbs_f.place(x=400,y=570,width=350,height=250)
show_dbs_f_title = Label(show_dbs_f,text='Show dbs',bg='#869AF6',fg='white',font=("Courier",13))
show_dbs_f_title.pack(fill=X)
show_databases = sc.ScrolledText(show_dbs_f)
show_databases['relief'] = 'solid'
show_databases['font'] = ("Tajawal",9)
show_databases.tag_config('zero',background='whitesmoke',foreground='red')
show_databases.tag_config('one',foreground='green',background='white')
show_databases.tag_config('two',foreground='blue',background='whitesmoke')
show_databases.place(x=10,y=40,width=330,height=200)


root.mainloop()
time.sleep(5000)