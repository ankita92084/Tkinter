from tkinter import*
# It helps to display the root window and manages all the other components of the tkinter application
root=Tk()
root.configure(background="sky blue")
root.title(" NAVGURUKUL CHATBOAT")

def send():
    # get() : Returns the entry's current text as a string
    send = "you->"+e.get()
    txt.insert(END,"\n"+send)
    if (e.get()=="hi"):
        txt.insert(END,"\n"+"                       Bot-> Hello!, How can we help you? ")
    elif (e.get()=="i want to know about NAVGURUKUL?"):
        txt.insert(END,"\n"+"Bot->                  Sure! Navgurukul is free SOFTWARE DEVELOPMENT COURSE  ")
    elif (e.get()=="what are the languages you are teaching "):
        txt.insert(END,"\n"+"Bot->                  We  teahes Programming Languages ")
    elif (e.get()=="Like?"):
        txt.insert(END,"\n"+"Bot->                  Python,Javascript ,Advance javascript ,Node js and react.js ")
    elif (e.get()=="oky thankyou!"):
        txt.insert(END,"\n"+"Bot->                  for any other query please visit again.")
    else:
        txt.insert(END,"\n"+"Bot-> Plese enter again ")
    e.delete(0,END)
txt = Text(root)
txt.grid(row=0,column=0)
# Entry widgets are used to display a single line text that is generally taken in the form of user Input.
e=Entry(root,width=200)
send=Button(root,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.mainloop()






