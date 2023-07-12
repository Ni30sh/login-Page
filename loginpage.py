from tkinter import *

log = Tk()
log.geometry("500x500+300+120")

login_frame = Label(log, text="Sign",font=("Microsoft YaHei UI Light", 12, "italic bold"))
login_frame.place(x=250,y=40,height=40,width=60)
log.mainloop()