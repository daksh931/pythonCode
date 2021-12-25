import tkinter as tk

def sign_in_clicked():
    
    if userid.get()=="spic" and password.get()=="edc":
        tk.messagebox.showinfo("Login Example", "Credentials matched, Login succeeded...")
    else:
        tk.messagebox.showwarning("Login Example","User Id or password incorrect!")

root = tk.Tk()
root.title("Login Example")
root.geometry("400x200")

userid = tk.StringVar()
password = tk.StringVar()

lbl1 = tk.Label(root, text="User Id")
lbl1.place(x = 50, y = 40)

ent1 = tk.Entry(root, textvariable=userid)
ent1.place(x = 120, y = 40)

lbl2 = tk.Label(root, text="Password")
lbl2.place(x = 50, y = 70)

ent2 = tk.Entry(root, show="*", textvariable=password)
ent2.place(x = 120, y = 70)

btn1 = tk.Button(root, text="Sign In", command=sign_in_clicked)
btn1.place(x = 120, y = 100)

btn2 = tk.Button(root, text="Cancel", command=root.destroy)
btn2.place(x = 180, y = 100)

root.mainloop()