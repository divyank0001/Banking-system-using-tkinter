from ast import Call
from subprocess import call
import tkinter
from tkinter import BOTH, Button,messagebox
import random
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='912004',database='bank')
mycur=mydb.cursor()

root=tkinter.Tk()
root.title("Registration Form")
root.geometry('700x700')
root.config(bg='#5b5f97')

f1=tkinter.Frame(root,bg='red',height=50)
f2=tkinter.Frame(root,bg='#5b5f97')
f1.pack(fill=BOTH)
f2.pack()
lbl=tkinter.Label(f1,text="World Bank",font=('serif',30,'bold'),bg='blue')
lbl.pack()

def login():
    root.destroy()
    login=tkinter.Tk()
    login.title("LogIn Page")
    login.geometry('700x500')
    login.config(bg='#5b5f97')
    
    lf1=tkinter.Frame(login,bg='red')
    lf2=tkinter.Frame(login,bg='#5b5f97')
    lf1.pack()
    lf2.pack()

    lab=tkinter.Label(lf1,text='Login Page ',font=('Arial',30,'bold'),fg='#5b5f97')
    lab.pack()

    acc_no=tkinter.Label(lf2,text='Enter the account number ',font=('Arial',15,'bold'),fg='#5b5f97')
    acc_no.grid(row=0,column=0,pady=30)
    acc_noent=tkinter.Entry(lf2,width=40)
    acc_noent.grid(row=0,column=1,padx=30)

    pas=tkinter.Label(lf2,text='Enter the password ',font=('Arial',15,'bold'),fg='#5b5f97')
    pas.grid(row=1,column=0,pady=30)
    pasent=tkinter.Entry(lf2,width=40)
    pasent.grid(row=1,column=1,padx=10)

    def logb():
        from tkinter import messagebox
        mycur.execute("select name,acc_no,bal from account where acc_no={} and pass={}".format(acc_noent.get(),pasent.get()))
        result = mycur.fetchall()

        if (not result):
            messagebox.showerror("Failed","Incorrect Username or Password !")
            login.destroy()



        else:
            messagebox.showinfo("Success","Welcome Mr. {}".format(result[0][0]))
            login.destroy()
            inlogin=tkinter.Tk()
            inlogin.title("Account information")
            inlogin.geometry('700x700')
            inlogin.config(bg='#5b5f97')

            inlf1=tkinter.Frame(inlogin,bg='red')
            inlf2=tkinter.Frame(inlogin,bg='#5b5f97')
            inlf3=tkinter.Frame(inlogin,bg='#5b5f97')
            inlf1.pack()
            inlf2.pack()
            inlf3.pack()

            lab2=tkinter.Label(inlf1,text='Account Information ',font=('Arial',30,'bold'),fg='#5b5f97')
            lab2.pack()

            mycur.execute('select * from account where acc_no={}'.format(result[0][1]))
            result1 = mycur.fetchall()

            acc_no=tkinter.Label(inlf2,text='Account Number - {}'.format(result1[0][0]),font=('Arial',15,'bold'),fg='#5b5f97')
            acc_no.grid(row=0,column=0,pady=10)

            name=tkinter.Label(inlf2,text='Name - {}'.format(result1[0][1]),font=('Arial',15,'bold'),fg='#5b5f97')
            name.grid(row=1,column=0,pady=10)

            add=tkinter.Label(inlf2,text='Address - {}'.format(result1[0][2]),font=('Arial',15,'bold'),fg='#5b5f97')
            add.grid(row=2,column=0,pady=10)

            #bal=tkinter.Label(inlf2,text='Account Balance - {}'.format(result1[0][3]),font=('Arial',15,'bold'),fg='#5b5f97')
            #bal.grid(row=3,column=0,pady=10)

            user=tkinter.Label(inlf2,text='User ID - {}'.format(result1[0][4]),font=('Arial',15,'bold'),fg='#5b5f97')
            user.grid(row=4,column=0,pady=10)

            def transfer():
                from tkinter import messagebox
                #inlogin.destroy()
                transbal=tkinter.Tk()
                transbal.title("Transfer Balance")
                transbal.geometry('700x500')
                transbal.config(bg='#5b5f97')

                tbf1=tkinter.Frame(transbal,bg='red')
                tbf2=tkinter.Frame(transbal,bg='#5b5f97')
                tbf1.pack()
                tbf2.pack()
                
                lab3=tkinter.Label(tbf1,text='Balance Transfer ',font=('Arial',30,'bold'),fg='#5b5f97')
                lab3.pack()

                tacc=tkinter.Label(tbf2,text='Enter the account number ',font=('Arial',15,'bold'),fg='#5b5f97')
                tacc.grid(row=0,column=0,pady=30)
                taccent=tkinter.Entry(tbf2,width=40)
                taccent.grid(row=0,column=1,padx=30)

                amount=tkinter.Label(tbf2,text='Enter the Amount to transfer ',font=('Arial',15,'bold'),fg='#5b5f97')
                amount.grid(row=1,column=0,pady=30)
                amountent=tkinter.Entry(tbf2,width=40)
                amountent.grid(row=1,column=1,padx=30)


                def taccbut():
                    mycur.execute("select bal,name from account where acc_no={}".format(taccent.get()))
                    result1 = mycur.fetchall()

                    if (not result1):
                        messagebox.showerror('Fail',"The account number does not exist !!!")
                    else:
                        a = int(amountent.get())
                        if a<=result[0][2]:
                            final = result1[0][0]+a
                            mycur.execute("update account set bal={} where acc_no={}".format(final,taccent.get()))
                            messagebox.showinfo("Success","You have Debited {} and Credited to {} !!!".format(a,result1[0][1]))
                            finalme = result[0][2]-a
                            mycur.execute("update account set bal={} where acc_no={}".format(finalme,result[0][1]))
                            mydb.commit()
                            transbal.destroy()

            
                        else:
                            messagebox.showerror("Failed","You do not have Sufficient Balance in your Account !!!")
                            transbal.destroy()


                trans=tkinter.Button(tbf2,text="Transfer Money",width=20,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=taccbut)
                trans.grid(row=3,column=0)


            def withdrawl():
                from tkinter import messagebox
                inlogin.destroy()
                withbal=tkinter.Tk()
                withbal.title("Withdrawl Money")
                withbal.geometry('700x500')
                withbal.config(bg='#5b5f97')

                tbf1=tkinter.Frame(withbal,bg='red')
                tbf2=tkinter.Frame(withbal,bg='#5b5f97')
                tbf1.pack()
                tbf2.pack()

                lab5=tkinter.Label(tbf1,text='Withdrwal Balance ',font=('Arial',30,'bold'),fg='#5b5f97')
                lab5.pack()

                amount=tkinter.Label(tbf2,text='Enter the Amount to Withdrawl ',font=('Arial',15,'bold'),fg='#5b5f97')
                amount.grid(row=1,column=0,pady=30)
                amountent=tkinter.Entry(tbf2,width=40)
                amountent.grid(row=1,column=1,padx=30)

                def wit():
                    a = int(amountent.get())
                    final = result[0][2]-a
                    mycur.execute("update account set bal={} where acc_no={}".format(final,result[0][1]))
                    messagebox.showinfo("Success","You have Withdrwal {} Rupees from your Account !!!".format(a))
                    mydb.commit()
                    withbal.destroy()

                dep=tkinter.Button(tbf2,text="Withdrawl Money",width=20,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=wit)
                dep.grid(row=3,column=0)

            def deposite():
                from tkinter import messagebox
                inlogin.destroy()
                depositebal=tkinter.Tk()
                depositebal.title("Deposite Page")
                depositebal.geometry('700x500')
                depositebal.config(bg='#5b5f97')

                tbf1=tkinter.Frame(depositebal,bg='red')
                tbf2=tkinter.Frame(depositebal,bg='#5b5f97')
                tbf1.pack()
                tbf2.pack()

                lab4=tkinter.Label(tbf1,text='Deposite Balance ',font=('Arial',30,'bold'),fg='#5b5f97')
                lab4.pack()

                amount=tkinter.Label(tbf2,text='Enter the Amount to Deposite ',font=('Arial',15,'bold'),fg='#5b5f97')
                amount.grid(row=1,column=0,pady=30)
                amountent=tkinter.Entry(tbf2,width=40)
                amountent.grid(row=1,column=1,padx=30)

                def depo():
                    a = int(amountent.get())
                    final = result[0][2]+a
                    mycur.execute("update account set bal={} where acc_no={}".format(final,result[0][1]))
                    messagebox.showinfo("Success","You have Credited {} Rupees in your Account !!!".format(a))
                    mydb.commit()
                    depositebal.destroy()

                def back():
                    inlogin.call()
                    


                dep=tkinter.Button(tbf2,text="Deposit Money",width=20,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=depo)
                dep.grid(row=3,column=0)

                backb=tkinter.Button(tbf2,text="back",width=20,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=back)
                backb.grid(row=3,column=1)


            def view():
                from tkinter import messagebox
                inlogin.destroy()
                viewbal=tkinter.Tk()
                viewbal.title("View Balance")
                viewbal.geometry('700x500')
                viewbal.config(bg='#5b5f97')

                tbf1=tkinter.Frame(viewbal,bg='red')
                tbf2=tkinter.Frame(viewbal,bg='#5b5f97')
                tbf1.pack()
                tbf2.pack()

                lab4=tkinter.Label(tbf1,text='View Balance ',font=('Arial',30,'bold'),fg='#5b5f97')
                lab4.pack()

                amount=tkinter.Label(tbf2,text='Your Account Number is      ',font=('Arial',15,'bold'),fg='#5b5f97')
                amount.grid(row=1,column=0,pady=30)

                amount=tkinter.Label(tbf2,text=result[0][1],font=('Arial',15,'bold'),fg='#5b5f97')
                amount.grid(row=1,column=1,pady=30)

                amount=tkinter.Label(tbf2,text='Your Account balance is     ',font=('Arial',15,'bold'),fg='#5b5f97')
                amount.grid(row=2,column=0,pady=30)

                amount=tkinter.Label(tbf2,text=result[0][2],font=('Arial',15,'bold'),fg='#5b5f97')
                amount.grid(row=2,column=1,pady=30)

                
                def logout():
                    viewbal.destroy()

                logoff=tkinter.Button(tbf2,text="Logout",width=20,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=logout)
                logoff.grid(row=6,column=0,pady=30)
            

            def logout():
                inlogin.destroy()
                



            trans=tkinter.Button(inlf3,text="Transfer Money",width=20,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=transfer)
            trans.grid(row=2,column=0,pady=10)

            dep=tkinter.Button(inlf3,text="Deposit",width=20,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=deposite)
            dep.grid(row=3,column=0,pady=10)

            wdl=tkinter.Button(inlf3,text="Withdrawl",width=20,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=withdrawl)
            wdl.grid(row=4,column=0,pady=10)

            viewbut=tkinter.Button(inlf3,text="View Balance",width=20,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=view)
            viewbut.grid(row=5,column=0,pady=10)

            logoff=tkinter.Button(inlf3,text="Logout",width=20,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=logout)
            logoff.grid(row=6,column=0,pady=10)

    def cancel():
        login.destroy()

    logbut=tkinter.Button(lf2,text="Login",width=10,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=logb)
    logbut.grid(row=2,column=0)

    canbtn=tkinter.Button(lf2,text="Cancel",width=10,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=cancel)
    canbtn.grid(row=2,column=1)

    

            
def createacc():
    root.destroy()
    root1=tkinter.Tk()
    root1.title("Registration Form")
    root1.geometry('700x700')
    root1.config(bg='#5b5f97')

    f1=tkinter.Frame(root1,bg='red')
    f2=tkinter.Frame(root1,bg='#5b5f97')
    f1.pack()
    f2.pack()    

    def cancel():
        root1.destroy()

    def sub():
        from tkinter import messagebox
        cmd='insert into account (acc_no,name,address,bal,user,pass) values (%s,%s,%s,%s,%s,%s)'
        acc=random.randint(1111,9999)
        data=[acc,nameent.get(),addent.get(),balent.get(),userent.get(),passent.get()]
        if(data[-1]==cpassent.get()):
        
            mycur.execute(cmd,data)
            mydb.commit()
            messagebox.showinfo("Sucess","Submit Successfully")
            showlbl=tkinter.Label(f2,text="Your Account No is {}".format(acc),font=("Arial",15,'bold'))
            showlbl.grid(row=8,columnspan=2)
        else:
            messagebox.showerror("Failed","Wrong Information Provide")


    lbl=tkinter.Label(f1,text='Registration Page ',font=('Arial',30,'bold'),fg='#5b5f97')
    lbl.pack()

    namelbl=tkinter.Label(f2,text="Name  ",font=('Arial',15,'bold'),fg='#5b5f97')
    namelbl.grid(row=0,column=0,pady=30)
    nameent=tkinter.Entry(f2,width=40)
    nameent.grid(row=0,column=1,padx=30)

    addlbl=tkinter.Label(f2,text="Address  ",font=('Arial',15,'bold'),fg='#5b5f97')
    addlbl.grid(row=1,column=0,pady=10)
    addent=tkinter.Entry(f2,width=40)
    addent.grid(row=1,column=1,padx=30)

    ballbl=tkinter.Label(f2,text="Balance ",font=('Arial',15,'bold'),fg='#5b5f97')
    ballbl.grid(row=2,column=0,pady=25)
    balent=tkinter.Entry(f2,width=40)
    balent.grid(row=2,column=1,padx=30)

    userlbl=tkinter.Label(f2,text="Username ",font=('Arial',15,'bold'),fg='#5b5f97')
    userlbl.grid(row=3,column=0,pady=25)
    userent=tkinter.Entry(f2,width=40)
    userent.grid(row=3,column=1,padx=30)

    passlbl=tkinter.Label(f2,text="Password ",font=('Arial',15,'bold'),fg='#5b5f97')
    passlbl.grid(row=4,column=0,pady=25)
    passent=tkinter.Entry(f2,width=40,show="*")
    passent.grid(row=4,column=1,padx=30)

    cpasslbl=tkinter.Label(f2,text="Confirm Password",font=('Arial',15,'bold'),fg='#5b5f97')
    cpasslbl.grid(row=5,column=0,pady=25)
    cpassent=tkinter.Entry(f2,width=40,show="*")
    cpassent.grid(row=5,column=1,padx=30)

    subbtn=tkinter.Button(f2,text="Submit",width=10,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=sub)
    subbtn.grid(row=6,column=0,stick='E')

    canbtn=tkinter.Button(f2,text="Cancel",width=10,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=cancel)
    canbtn.grid(row=6,column=1)

loginbtn=tkinter.Button(f2,text="Login",width=20,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=login)
loginbtn.grid(row=1,columnspan=2,pady=30)

createaccbut=tkinter.Button(f2,text="Create Account",width=20,fg='red',bg='black',font=(15),activebackground='yellow',activeforeground='green',command=createacc)
createaccbut.grid(row=2,columnspan=1,pady=30)

root.mainloop()