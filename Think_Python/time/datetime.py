#_*_ encoding:utf-8 _*_

import datetime 

#获取当前日期，并输出是星期几
d = datetime.datetime.now().date()
i = d.weekday()
print(d)
print(i)
