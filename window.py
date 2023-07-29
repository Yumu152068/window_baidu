from tkinter import *
def window():
    win = Tk()
    win.title('提示')
    win.geometry('300x80')
    win.resizable(True, True)
    # 设置账号
    Label(text='搜索内容:').grid(column = 1, row = 0)
    uname = Entry(win)
    uname.grid(column = 2, row = 0)
    def login():
        global a
        global b
        a = uname.get()
        # b = pwd.get()
        win.destroy()
    # 登陆按钮
    Button(text='搜索', command=login).grid(column = 3, row = 0)
    Button.pack
    win.mainloop()
    return a
if __name__ == '__main__':
    window()
