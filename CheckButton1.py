import tkinter as tk

def center_screen(frame):
    FormWidth = 400
    FormHeight= 400
    
    ScreenWidth = root.winfo_screenwidth()
    ScreenHeight = root.winfo_screenheight()
    
    x = (ScreenWidth/2) - (FormWidth/2)
    y = (ScreenHeight/2) - (FormHeight/2)
    
    root.geometry("%dx%d+%d+%d" % (FormWidth, FormHeight, x,y))

def show_clicked():
    if v1.get()==True:
        tk.messagebox.showinfo("CheckButton example","Checked")
    else:
        tk.messagebox.showinfo("CheckButton example","Not Checked")

root = tk.Tk()
root.title("Check Box Example")

v1 = tk.BooleanVar()

root.resizable(0,0)
root.attributes("-toolwindow",1)
#root.overrideredirect(1)
center_screen(root)

chk1 = tk.Checkbutton(root, text="NRI", variable=v1)
chk1.place(x = 50, y = 40)

btn1 = tk.Button(root, text="Show", command=show_clicked)
btn1.place(x = 50, y = 70)


root.mainloop()