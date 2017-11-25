from Tkinter import *
import sqlite3
from tkMessageBox import *
from random import *

conn = sqlite3.connect('quiz.db')
cur = conn.cursor()
global un, pas, dis  # declaring username and password variable as global
a = [0] * 51
tk=Tk()
v1 = StringVar()
global score
score=0
global x
global c
c=0 #counter variable to display in
#A persons score is initially zero



def finish():
    global score
    global c
    dis.destroy()
    fin=Toplevel()
    fin.title('FINAL SCORE')
    fin.configure(bg='black')
    Label(fin,text='Your quiz finished because you sumbitted all 10 questions or pressed FINISH',font='helevetica 16 bold',relief='ridge',bg='black',fg='white').grid(row=0,column=0)
    Label(fin,text='You attemped '+str(c)+' Questions',font='helevetica 16 bold',relief='raised',bg='black',fg='white',bd=5).grid(row=1,column=0,columnspan=16)
    Label(fin,text='Your Score = '+str(score),font='helevetica 16 bold underline',relief='raised',bg='black',fg='white',bd=5).grid(row=2,column=0,columnspan=16)


def disques():
    global x, dis,timeLabel,flag
    dis = Toplevel()
    dis.title("QUESTIONS")
    dis.geometry('+0+300')
    dis.resizable(0, 0)
    dis.configure(background='#00ccff')
    v1.set("q")
    cur.execute('SELECT ques FROM questions WHERE sno==(?)', (x,))
    question = str(cur.fetchone()[0])
    Label(dis, text=question, font='times 20 bold', relief='ridge',bg='#66ff33').grid(row=0, columnspan=6)
    cur.execute('SELECT a FROM questions WHERE sno==(?)', (x,))
    opa = str(cur.fetchone()[0])
    r1 = Radiobutton(dis, text=opa, variable=v1, value='a',bg='#00ccff')
    r1.grid(row=1, column=0,sticky=W)
    cur.execute('SELECT b FROM questions WHERE sno==(?)', (x,))
    opb = str(cur.fetchone()[0])
    r2 = Radiobutton(dis, text=opb, variable=v1, value='b',bg='#00ccff')
    r2.grid(row=2, column=0,sticky=W)
    cur.execute('SELECT c FROM questions WHERE sno==(?)', (x,))
    opc = str(cur.fetchone()[0])
    r3 = Radiobutton(dis, text=opc, variable=v1, value='c',bg='#00ccff')
    r3.grid(row=3, column=0,sticky=W)
    cur.execute('SELECT d FROM questions WHERE sno==(?)', (x,))
    opd = str(cur.fetchone()[0])
    r4 = Radiobutton(dis, text=opd, variable=v1, value='d',bg='#00ccff')
    r4.grid(row=4, column=0,sticky=W)
    cur.execute('SELECT correct FROM questions WHERE sno==(?)', (x,))
    ans = str(cur.fetchone()[0])
    b1 = Button(dis, text='Sumbit',bg='powder blue',bd=5,activeforeground='blue',activebackground='black', command=lambda: dandq(ans))
    b1.grid(row=5, column=1)
    exit = Button(dis, text='FINISH',bg='powder blue',bd=5,activeforeground='blue',activebackground='red', command=lambda: finish())
    exit.grid(row=5, column=5)



def dandq(ans):
    global score
    global v1
    if v1.get() == ans:     #if answer matches from database increase score
        score = score + 1
    elif v1.get()!=ans:     #if answer doesn't match then show error
        showerror('Error','Wrong Answer')

    dis.destroy()
    ques()


def random():
    return randint(2, 50)


def ques():
    global x
    global c
    if c<10: #counter variable to check if not more than 10ques are displayed
        x = random()    #calling random function to genrate a random number
        if a[x] == 0:   #a list for checking if the question has been displayed before or not
            a[x] = 1
            c = c + 1
            disques()
        else:   #if displayed then again calling this function
            ques()
    else:
        finish()


def insertdata():
    global nun, npas, nam, signup
    cur.execute("INSERT INTO us (name,username,password)  VALUES (?,?,?)", (nam.get(), nun.get(), npas.get(),))
    conn.commit()
    signup.destroy()



def enter():
    global un, pas, login
    cur.execute('SELECT username FROM us WHERE username=? AND  password=?', (un.get(), pas.get(),))
    data = cur.fetchall()
    if not data:  # condition to check if data is found in database and if not found displaying correct error and also asking user for new input
        pas.delete(0, END)
        un.delete(0, END)
        un.focus_set()
        showerror('Error', 'Data Not Found,If New User Please Signup')
    else:  # if found then proceeding to quiz
        ques()
        login.destroy()


def newuser():
    global nun, npas, nam, signup
    signup = Tk()
    signup.title('NEW USER')
    Label(signup, text='Fill in the details below', font='times 20 bold', relief='ridge').grid(row=0, columnspan=5)
    Label(signup, text='Name').grid(row=1, column=0)
    nam = Entry(signup, width=25)
    nam.grid(row=1, column=2)
    Label(signup, text='Username').grid(row=2, column=0)
    nun = Entry(signup, width=25)  # username input
    nun.grid(row=2, column=2)
    Label(signup, text='Password').grid(row=3, column=0)
    npas = Entry(signup, width=25, show='*')  # password input
    npas.grid(row=3, column=2)
    sum = Button(signup, text='Submit', bg='cyan',bd=5,command=lambda: insertdata())
    sum.grid(row=4,column=2)


def logi():
    global un, pas, login
    login = Tk()
    login.title('Quiz Portal')
    login.resizable(0,0)
    login.geometry("600x500")
    login.configure(bg='medium orchid')
    Label(login, text='QUIZ PORTAL', font='times 40 bold', relief='raised',bg='#00ffff',bd=5).place(x=105,y=0)
    Label(login, text='Username',font='times 15 bold',bg='#66ccff').place(x=150,y=200,width=100)
    un = Entry(login, width=25,font='times 10 bold')  # username input
    un.place(x=260,y=200,height=25)
    Label(login, text='Password',font='times 15 bold',bg='#66ccff').place(x=150,y=275,width=100)
    pas = Entry(login, width=25, show='*')  # password input
    pas.place(x=260,y=275,height=25)
    b1 = Button(login, text='Login',bg='#6699ff',bd=5,activeforeground='blue',activebackground='black', command=lambda: enter())
    b1.place(x=200,y=320)
    b2 = Button(login, text='New User',bg='#6699ff',bd=5,activeforeground='blue',activebackground='black', command=lambda: newuser())
    b2.place(x=300,y=320)



logi()
mainloop()
