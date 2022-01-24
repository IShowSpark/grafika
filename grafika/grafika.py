from tkinter import *
click=0
def clicker(event):
    global click
    click+=1
    button.config(text=click)

def clicker1(event):
    global click
    click-=1
    button.config(text=click)

def txtlabel(event):
    text=txt.get()
    label.configure(text=text)
    txt.delete(0,END)

def choose():
    chosik=var.get()
    label.configure(text=chosik)
    



window=Tk()
answ=''
while answ not in ["1","2","3"]:
    print("1 - 500x800, 2 - 800x500, 3 - 1920x1080")
    answ=input("Какое разрешение хотите выбрать?: ")

    if answ=="1":
        window.geometry("500x800")
    elif answ=="2":
        window.geometry("800x500")
    elif answ=="3":
        window.geometry("1920x1080")

window.title("Bebra")
button=Button(window,text="Нажми на меня",font="Arial 20",width=20,bg="white",fg="#00BFFF",relief=SOLID)
button.place(x=810,y=500)#side=LEFT
button.bind("<Button-1>",clicker)
button.bind("<Button-3>",clicker1)

label=Label(window,text="Pascal",height=3,width=20,font="Arial 20",bg="white",fg="#00BFFF",relief="solid")
label.place(x=810,y=100)
txt=Entry(window,font="Arial 20",bg="white",fg="#00BFFF",justify=CENTER)
txt.place(x=820,y=50)
txt.bind("<Return>", txtlabel)
gif1=PhotoImage(file="1.gif")
gif2=PhotoImage(file="2.gif")
gif3=PhotoImage(file="3.gif")
var=StringVar()
var.set("Один")
r1=Radiobutton(window,image=gif1,variable=var,value="Один",command=choose)
r2=Radiobutton(window,image=gif2,variable=var,value="Два",command=choose)
r3=Radiobutton(window,image=gif3,variable=var,value="Три",command=choose)
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)



window.mainloop()





