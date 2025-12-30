import tkinter as tk
def press(v):
    entry.insert(tk.END,v)
def clear():
    entry.delete(0,tk.END)
def calc():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")
root=tk.Tk()
root.title("Calculator")
entry=tk.Entry(root,width=16,font=('Arial',24),bd=4,relief=tk.RIDGE,justify='right')
entry.grid(row=0,column=0,columnspan=4)
buttons=[
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]
row_val=1
col_val=0
for button in buttons:
    if button=='=':
        tk.Button(root,text=button,width=4,height=2,font=('Arial',18),command=calc).grid(row=row_val,column=col_val)
    else:
        tk.Button(root,text=button,width=4,height=2,font=('Arial',18),command=lambda v=button:press(v)).grid(row=row_val,column=col_val)
    col_val+=1
    if col_val>3:
        col_val=0
        row_val+=1
tk.Button(root,text='C',width=4,height=2,font=('Arial',18),command=clear).grid(row=row_val,column=0)
root.mainloop() 
