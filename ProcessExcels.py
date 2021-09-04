from FormatText import text_formating_control_panel
from datetime import datetime
import pandas as pd
import os
import shutil

def readExcel(filename):
    source_df = pd.read_excel(filename, na_filter=False)
    return source_df

def dfExcelToText(filename, source_df):
    if filename.endswith('xls'):
        output_name = filename.replace('.xls', '.txt')
    else:
        output_name = filename.replace('.xlsx', '.txt').replace('.xltx', '.txt')
        
    with open(output_name, 'w', encoding='utf-8') as f:
        df_string = source_df.to_string(index=False)
        f.write(df_string)

def readText(filename):
    df_from_txt = pd.read_csv(filename, sep="*", header=None)
    return df_from_txt

def dfTextToExcel(filename, df_from_txt):
    output_name = filename.replace('.txt', '.xlsx')
    df_from_txt.to_excel(output_name, index=False, header=False)

def deleteEmptyExcel(textname):
    excel_name = textname.replace('.txt', '.xlsx')
    os.remove(excel_name)


if __name__ == '__main__':
    # 选择工作目录
    while True:
        workpath = input("输入目标文件夹（直接点击Enter为所在父文件夹）：")
        if not workpath:
            workpath = os.path.abspath(os.path.join(os.getcwd(), ".."))
            print("Working in", workpath)
        if os.path.isdir(workpath):
            break
    
    # 遍历Excel
    with os.scandir(workpath) as filelist:
        for file in filelist:
            if file.name.endswith('.xlsx') or file.name.endswith('.xls') or file.name.endswith('xltx'):
                # 读取Excel
                source_df = readExcel(file.path)
                # 写入TXT
                dfExcelToText(file.path, source_df)
    
    # TXT操作
    text_formating_control_panel(workpath)

    # 将原Excel文件移入备份文件夹
    # 创建备份文件夹
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir = workpath+"/"+"backup excels "+current_time
    os.makedirs(backup_dir, exist_ok=True)
    # 遍历Excel
    with os.scandir(workpath) as filelist:
        for file in filelist:
            if file.name.endswith('.xlsx') or file.name.endswith('.xls') or file.name.endswith('xltx'):
                # 移入备份文件夹
                shutil.move(file.path, backup_dir)
            

    # 遍历TXT
    with os.scandir(workpath) as filelist:
        output_counter = 0
        for file in filelist:
            if file.name.endswith('.txt'):
                # 只读非空文件
                if os.path.getsize(file.path) > 0 :
                    output_counter += 1
                    # 读取TXT
                    df_from_txt = readText(file.path)
                    # 写入Excel;不改变rest名字
                    if file.name == "rest.txt":
                        output_name = file.path
                    else:
                        output_name = workpath + "/" + str(output_counter) + ".xlsx"
                    print("+"*15)
                    print("正在写入"+output_name)
                    print(df_from_txt)
                    dfTextToExcel(output_name, df_from_txt)

    # 遍历txt
    with os.scandir(workpath) as filelist:
        for file in filelist:
            if file.name.endswith('.txt'):
                # 删除txt
                os.remove(file.path)

    # pause
    os.system('pause')