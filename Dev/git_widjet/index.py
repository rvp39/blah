from tkinter import *
import os
initial_path="C:\\Users\\rvp39\\Dev\\web_mk1"
#def chCWD(s):
#    new_path=initial_path+"\\"+s
#    os.chdir(new_path)
def run(cmd):
    os.system(cmd)
def comit():
    A=entry.get()
    comt="git commit -m \""+A+"\""
    os.system(comt)
    entry.delete(0, END)


master=Tk()
master.title("Git Widjet")
master.minsize(300,250)
Label(master, text="CWD : ").grid(row=0, column=0, padx=10,pady=10)
Label(master, text=os.getcwd()).grid(row=0, column=1, padx=10,pady=10)

#Button(master, text="web_mk1", command=chCWD("web_mk1")).grid(row=1, column=0, padx=10 ,pady=10)

Button(master, text="git add", command=run("git add .")).grid(row=2, column=0, padx=10,pady=10)

Button(master ,text="git push", command=run("git push origin master")).grid(row=2, column=1, padx=10,pady=10)

Label(master, text="comit message").grid(row=3, column=0,padx=10, pady=20)
entry=Entry(master).grid(row=3, column=1,padx=20 ,pady=20)
Button(master, text="git commit",command=comit).grid(row=3,column=2,padx=10,pady=20)

mainloop()