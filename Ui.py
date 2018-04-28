#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 9:40 AM
# @Author  : Steven
# @Contact : 523348709@qq.com
# @Site    : 
# @File    : Ui.py
# @Software: PyCharm


from tkinter import *
from lockwipe import *
from tkinter import messagebox
class Ui(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.lockwiper=Lockwipe()

    def createWidgets(self):

        self.detect_button=Button(self,text='检测设备状态',width=100,command=self.detect)
        self.detect_button.pack()


        self.unlock_button = Button(self, text='一键解锁',state='disabled',width=100)
        self.unlock_button.pack()

    def detect(self):
        state=self.lockwiper.detect_devices()
        if state:
            self.unlock_button.configure(state='normal')
            messagebox.showinfo('成功','adb设备已经连接')
            pass
        else:
            messagebox.showerror('错误','adb设备未连接')
        pass

    def unlock(self):
        state = self.lockwiper.detect_devices()
        if state:
            self.lockwiper.unlook_devices()
            messagebox.showinfo('成功','设备成功解锁，正在重启')
        else:
            messagebox.showerror('错误', 'adb设备断开连接')
            self.unlock_button.configure(state='disable')



if __name__ == '__main__':
    root=Tk()
    root.wm_attributes('-topmost', 1)
    root.title('安卓设备一键工具')
    root.geometry('250x100+30+30')
    root.resizable(width=False, height=False)
    ui = Ui(master=root)
    ui.mainloop()