import tkinter as tk

def exit_clicked():
    ret = tk.messagebox.askyesno("Product Info", "Do you want to close this application?" )
    
    if ret==True:
        root.destroy()
    
def generate_clicked():
    
    if validate_data()==True:
        total.set( quantity.get()*price.get()  )
        
        if total.get()<=10000:
            discount.set (  (total.get()*15)/100   )
        elif total.get() >10000 and total.get()<=20000:
            discount.set (  (total.get()*25)/100   )
        else:
            discount.set (  (total.get()*35)/100   )
        
        netcharges.set( total.get() -  discount.get()  )

def validate_data():
    if len( str(quantity.get()))==0 or quantity.get()<=0:
        tk.messagebox.showwarning("Product Info", "Quantity not valid!")
        return False
    
    if  len(str(price.get()))==0 or price.get()<=0:
        tk.messagebox.showwarning("Product Info", "Price not valid!")
        return False
    
    return True

root= tk.Tk()
root.geometry("400x400")
root.title("Billing System")

quantity = tk.IntVar()
price = tk.IntVar()
total = tk.IntVar()
discount = tk.IntVar()
netcharges = tk.IntVar()


lbl1 = tk.Label(root, text="Product Name")
lbl1.place(x = 50, y = 40)

ent1 = tk.Entry(root, )
ent1.place(x = 150, y = 40)

lbl2 = tk.Label(root, text="Quantity")
lbl2.place(x = 50, y = 70)

ent2 = tk.Entry(root, textvariable=quantity)
ent2.place(x = 150, y = 70)

lbl3 = tk.Label(root, text="Price")
lbl3.place(x = 50, y = 100)

ent3 = tk.Entry(root, textvariable=price)
ent3.place(x = 150, y = 100)

lbl4 = tk.Label(root, text="Total")
lbl4.place(x = 50, y = 130)

ent4 = tk.Entry(root, state="readonly", textvariable=total)
ent4.place(x = 150, y = 130)

lbl5 = tk.Label(root, text="Discount")
lbl5.place(x = 50, y = 160)

ent5 = tk.Entry(root, state="readonly", textvariable=discount)
ent5.place(x = 150, y = 160)

lbl6 = tk.Label(root, text="Net Charges")
lbl6.place(x = 50, y = 190)

ent6 = tk.Entry(root, state="readonly", textvariable=netcharges)
ent6.place(x = 150, y = 190)

btn1 = tk.Button(root, text="Generate", command=generate_clicked)
btn1.place(x = 150, y = 220)

btn2 = tk.Button(root, text="Exit", command=exit_clicked)
btn2.place(x = 240, y =220)

root.mainloop()