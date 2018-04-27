#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 8:45 AM
# @Author  : Steven
# @Contact : 523348709@qq.com
# @Site    : 
# @File    : lockwipe.py
# @Software: PyCharm
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 4:23 PM
# @Author  : Steven
# @Contact : 523348709@qq.com
# @Site    :
# @File    : wifidog.py
# @Software: PyCharm
from tkinter import *
import commands

class Lockwipe(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.list=[]
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.info_var=StringVar()

        self.scan_button=Button(self,text='一键还原',command=self.recover_lock)
        self.scan_button.pack()

        self.stop_scan_button=Button(self,text='一键解锁',command=self.detect_lock)
        self.stop_scan_button.pack()

        self.info_label = Label(self,textvariable=self.info_var,bg='red')
        self.info_label.pack()

    def detect_devices(self):
        cmd='adb shell ls'
        result = commands.getoutput(cmd)
        if len(result)<50:
            return False
        else:
            return True

    def detect_lock(self):
        device_statu=self.detect_devices()
        if device_statu:
            cmd1='adb shell "su -c \'rm /data/system/gatekeeper.password.key\'"'
            cmd2='adb shell "su -c \'rm /data/system/gatekeeper.pattern.key\'"'
            cmd3='adb shell "su -c \'rm /data/system/locksettings.db-wal\'"'
            cmd4 = 'adb shell "su -c \'rm /data/system/locksettings.db\'"'
            cmd5 = 'adb shell "su -c \'rm /data/system/locksettings.db-shm\'"'
            out1=commands.getoutput(cmd1)
            out2=commands.getoutput(cmd2)
            out3=commands.getoutput(cmd3)
            out4=commands.getoutput(cmd4)
            out5=commands.getoutput(cmd5)

            #out2=commands.getoutput(cmd2)

            self.info_var.set('已经清除密码，正在重启')
            commands.getoutput('adb reboot')

        else:
            self.info_var.set('设备未开启adb或adb未连接，请检查')

    def recover_lock(self):
        device_statu = self.detect_devices()
        if device_statu:
            cmd1 = 'adb shell "su -c \'mv /data/local/tmp/gatekeeper.password.key /data/system/\'"'
            #cmd2 = 'adb shell "su -c \'mv /data/local/tmp/gatekeeper.pattern.key /data/system/\'"'
            out1 = commands.getoutput(cmd1)
            out2=''
            #out2 = commands.getoutput(cmd2)
            if len(out1) != 0 and len(out2) != 0:
                self.info_var.set('此设备密码文件未授权修改，请重置')
            elif len(out1) == 0 and len(out2) == 0:
                self.info_var, set('手机恢复加密，即将重启')
                commands.getoutput('adb reboot')
            else:
                self.info_var.set('此设备密码文件部分丢失，请重置')
        else:
            self.info_var.set('设备未开启adb或adb未连接，请检查')




if __name__ == '__main__':
    root=Tk()
    root.wm_attributes('-topmost', 1)
    root.geometry('800x300+30+30')
    dog = Lockwipe(master=root)
    dog.mainloop()