from tkinter import Tk,Button,Label,Entry,Radiobutton,Frame,IntVar

root=Tk()
root.title("Ejercicio 1")
root.geometry("600x450")
root.resizable(0,0)

#Buttons

#1
b1=Button(root,text="Add")
b1.config(bg="blue",font=40,fg="White")
b1.place(x="0",y="0",width="120",height="35")

#2
b2=Button(root,text="Delete")
b2.config(bg="blue",font=40,fg="White")
b2.place(x="120",y="0",width="120",height="35")

#3
b3=Button(root,text="Search")
b3.config(bg="blue",font=40,fg="White")
b3.place(x="240",y="0",width="120",height="35")

#4
b4=Button(root,text="Services")
b4.config(bg="blue",font=40,fg="White")
b4.place(x="360",y="0",width="120",height="35")

#5
b5=Button(root,text="Help")
b5.config(bg="blue",font=40,fg="White")
b5.place(x="480",y="0",width="120",height="35")

#6
b6=Button(root,text="Submit")
b6.config(bg="light grey",font=40)
b6.place(x="268",y="380")

#Frames

#1
fr1=Frame(root)
fr1.config(relief="groove",bd=1,bg="white")
fr1.place(x="0",y="55",width="600",height="100")

#2
fr2=Frame(fr1)
fr2.config(bg="white")
fr2.place(x="0",y="0",width="300",height="50")

#3
fr3=Frame(fr1)
fr3.config(bg="white")
fr3.place(x="300",y="0",width="300",height="50")

#4
fr4=Frame(fr1)
fr4.config(bg="white")
fr4.place(x="0",y="50",width="300",height="50")

#5
fr5=Frame(fr1)
fr5.config(bg="white")
fr5.place(x="300",y="50",width="300",height="50")

#6
fr6=Frame(root)
fr6.config(relief="groove",bd=1,bg="white")
fr6.place(x="0",y="250",width="600",height="100")

#5
fr7=Frame(fr6)
fr7.config(bg="white",bd=1,relief="raised")
fr7.place(x="0",y="0",width="300",height="100")

#5
fr8=Frame(fr6)
fr8.config(bg="white",bd=1,relief="raised")
fr8.place(x="300",y="0",width="300",height="100")



#Labels

#1
named1=Label(fr2,text="First Name:")
named1.config(bg="white")
named1.place(x="20",y="12")

#2
named2=Label(fr3,text="Last Name:")
named2.config(bg="white")
named2.place(x="20",y="12")

#3
named3=Label(fr4,text="Birth Date:")
named3.config(bg="white")
named3.place(x="20",y="12")

#4
named4=Label(fr5,text="Country:")
named4.config(bg="white")
named4.place(x="33",y="12")

#5
named5=Label(root,text="Credit Card (if any):")
named5.place(x="20",y="170")

#6
named6=Label(root,text="Credit Card type (if any):")
named6.place(x="20",y="220")

#7
named7=Label(fr7,text="Room Type:")
named7.config(bg="white")
named7.place(x="40",y="10")

#8
named8=Label(fr8,text="Total Staying Time (days):")
named8.config(bg="white")
named8.place(x="40",y="10")

#Entries

#1
try1=Entry(fr2)
try1.config(bg="grey",fg="white")
try1.place(x="90",y="12",width="190",height="20")

#2
try2=Entry(fr3)
try2.config(bg="grey",fg="white")
try2.place(x="90",y="12",width="190",height="20")

#3
try3=Entry(fr4)
try3.config(bg="grey",fg="white")
try3.place(x="90",y="12",width="30",height="20")

#4
try4=Entry(fr4)
try4.config(bg="grey",fg="white")
try4.place(x="130",y="12",width="30",height="20")

#5
try5=Entry(fr4)
try5.config(bg="grey",fg="white")
try5.place(x="170",y="12",width="50",height="20")

#6
try6=Entry(fr5)
try6.config(bg="grey",fg="white")
try6.place(x="90",y="12",width="190",height="20")

#7
try7=Entry(root)
try7.place(x="133",y="170",width="190",height="20")

#8
try8=Entry(fr8)
try8.config(bg="grey",fg="white")
try8.place(x="190",y="10",width="40",height="20")

#Radiobutton

#Group 1
crType=IntVar()
crType.set(0)

cr1=Radiobutton(root,text="Visa",value=1,variable=crType)
cr1.config(state="normal")
cr1.place(x="160",y="220")
cr1.deselect()

cr2=Radiobutton(root,text="Mastercard",value=2,variable=crType)
cr2.config(state="normal")
cr2.place(x="220",y="220")
cr2.deselect()

#Group 2
room=IntVar()
room.set(0)

ch1=Radiobutton(fr7,text="Normal",value=1,variable=room)
ch1.config(state="normal",bg="white")
ch1.place(x="120",y="10")
ch1.deselect()

ch2=Radiobutton(fr7,text="Familiar",value=2,variable=room)
ch2.config(state="normal",bg="white")
ch2.place(x="120",y="34")
ch2.deselect()

ch3=Radiobutton(fr7,text="Special",value=3,variable=room)
ch3.config(state="normal",bg="white")
ch3.place(x="120",y="58")
ch3.deselect()


root.mainloop()