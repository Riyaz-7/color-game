from tkinter import *
import random
from tkinter import messagebox

colors1=[]
f1=open("col.txt","r")
#cnt=0
for i in f1:
    colors1.append(i.strip('\n'))
    #colors1[cnt]=colors1[cnt].strip('\n')
    #cnt+=1

colors2 =  ['Red','Blue','Green','Pink','Black','Yellow',
                                          'Orange','White','Purple','Brown','Cyan']

score1=score2=0

timeleft1 = 30
timeleft2  =60


def start1(event):
    if timeleft1 ==30:
        count1()
    colorshuffle1()

def colorshuffle1():
    global score1
    global timeleft1

    if timeleft1 > 0:
       if e1.get().lower() == colors1[3].lower():
          score1 += 1
       e1.delete(0,END)
       random.shuffle(colors1)
       colorTab1.config(fg = str(colors1[3]), text = str(colors1[1]))
       #print(colors1[3])
       scoreTab1.config(text = "score: "+ str(score1))

def GameEnd():
   messagebox.showinfo("Game Over", "Hey your time is up!! your score is "+str(score1) )
   
def count1():
    global timeleft1
    if timeleft1 > 0 :
       timeleft1 -=1
       timeTab1.config(text = "you have: " +str(timeleft1) + " second\s ")
       timeTab1.after(1000,count1)
    else:
        GameEnd()

def start2(event):
    if timeleft2 == 60:
      count2()
    colorshuffle2()

def colorshuffle2():
    global score2
    global timeleft2
    global e2, label2 , scoreTab2

    if timeleft2 > 0:
        if e2.get().lower() == colors2[3].lower():
              score2 += 1
        e2.delete(0,END)
        random.shuffle(colors2)
        label2.config(fg = str(colors2[3]), text = str(colors2[1]))
        scoreTab2.config(text = "score: "+ str(score2))

def GameEnd1():
   messagebox.showinfo("Game Over", "Hey your time is up!! your score is "+str(score2) )   

def count2():
        global timeleft2, timeTab2
        if timeleft2 > 0 :
           timeleft2 -= 1
           timeTab2.config(text = "you have: " +str(timeleft2) + " second\s ")
           timeTab2.after(1000,count2)
        else:
            GameEnd1()

root = Tk()
root.title("The color game: Beginner level")
root.geometry("390x265")
root.configure(bg="aliceblue")

instruction1 = Label(root, text = "tell the color of the word , and not the word!", font = ('Helvitica',12, "bold"),fg="red",bg="aliceblue")
instruction1.pack()

scoreTab1 = Label(root, text = "Try scoring more than 10! Hit enter to start playing ", font = ('Helvitica',12, "bold"),fg="red",bg="aliceblue")
scoreTab1.pack()

timeTab1 = Label(root, text = "you have :"+str(timeleft1) + "second\s", font = ('Helvitica',12, "bold"),fg="dark red",bg="aliceblue")
timeTab1.pack()

colorTab1 = Label(root, font = ('Times',65,"bold"))
colorTab1.pack()

e1 = Entry(root,relief=GROOVE)
e1.pack()

root.bind('<Return>',start1)

def info():
    messagebox.showinfo("the color game",\
                                    "we read words much faster than we name colors. The higher you score, the better your attention levels are!!")

def open_new():
   global scoreTab2, timeTab2 , label2, e2
   window=Toplevel()
   window.geometry("460x220")
   window.title("The color game: Advance level")
   instruction2 = Label(window, text = "lengthier the game, the more confusion it will ", font = ('Helvitica',12, "bold"),fg="red")
   instruction2.pack()

   scoreTab2 = Label(window, text = "hit enter to start playing!", font = ('Helvitica',12, "bold"),fg="red")
   scoreTab2.pack()

   timeTab2 = Label(window, text = "you have:" +str(timeleft2) + "second\s",  font = ('Helvitica',12, "bold"),fg="red")
   timeTab2.pack()

   label2=Label(window, font = ('Times',65,"bold"))
   label2.pack()

   e2 = Entry(window,relief=GROOVE)
   e2.pack()

   exit2=Button(window, text="EXIT",padx=20,command=window.destroy).place(anchor=SW,x=30,y=200)

   window.bind('<Return>',start2)

exit1 = Button(root, text="Exit",padx=20,command=root.destroy).place(anchor=SW,x=30,y=200)
adv=Button(root, text="Advance",padx=20,command=open_new).place(anchor=SE,x=370,y=200 )
Button(root, text="know more", command=info).place(anchor=S,x=200,y=250)

root.mainloop()
