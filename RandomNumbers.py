import random
import os

def generate_random_nums():
    # random number between 0, 23
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    year = random.randint(1970, 2021)
    days = random.randint(1, 6)
    weeks = random.randint(1, 3)
    months = random.randint(1, 11)
    years = random.randint(1, 30)
    return hour, minute, year, days, weeks, months, years

# 打开txt
while True:
    filepath = input("输入目标文件：")
    if os.path.isfile(filepath):
        break
f_origin = open(filepath, 'r', encoding='utf-8')
f_destination = open('替换后.txt', 'w', encoding='utf-8')
counter = 0
# 逐行读取
for s in f_origin.readlines():
    # 生成随机数字（日期，时间，年份）
    hour, minute, year, days, weeks, months, years = generate_random_nums()
    # 随机生成替换类型
    replace_type = random.randint(1,6)
    # 准备替换文字
    if replace_type == 1:
        replace_text = str(hour) + '点' + str(minute) + '分'
    if replace_type == 2:
        replace_text = str(year) + '年'
    if replace_type == 3:
        replace_text = str(days) + '天前'
    if replace_type == 4:
        replace_text = str(weeks) + '个星期前'
    if replace_type == 5:
        replace_text = str(months) + '个月前'
    if replace_type == 6:
        replace_text = str(years) + '年前'
    # 替换xx
    s = s.replace('xx', replace_text)
    # 写入新文件
    f_destination.write(s)
    counter += 1
    print(counter)

# 关闭文件
f_origin.close()
f_destination.close()
