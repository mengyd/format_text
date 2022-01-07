from FormatText import text_formating_control_panel, askForOption, isIgnoredFile
from datetime import datetime
import pandas as pd
import os
import shutil
import loadconfig

__params__ = loadconfig.loadParams()

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
    df_from_txt = pd.read_csv(filename, sep="\t", header=None)
    return df_from_txt

def dfTextToExcel(filename, df_from_txt):
    output_name = filename.replace('.txt', '.xlsx')
    df_from_txt.to_excel(output_name, index=False, header=False)

def deleteEmptyExcel(textname):
    excel_name = textname.replace('.txt', '.xlsx')
    os.remove(excel_name)

def isExcel(filename):
    if filename.endswith('.xlsx') or filename.endswith('.xls') or filename.endswith('xltx'):
        if not filename.startswith('~$'):
            return True
    return False

def start_processing(workpath):
    # 遍历Excel
    with os.scandir(workpath) as filelist:
        for file in filelist:
            if isExcel(file.name) and not isIgnoredFile(file.name):
                # 读取Excel
                source_df = readExcel(file.path)
                # 写入TXT
                dfExcelToText(file.path, source_df)

def controlPanel_processExcel(workpath):
    # choice for formating
    __format_choice__ = __params__["format choice"]
    # choice for blending
    __blend_choice__ = __params__["blend choice"]
    
    # TXT操作
    ops = []
    while True:
        module_choice, keyword = askForOption()
        if module_choice == __quit_choice__:
            # print("quit...")
            print("退出程序...")
            break
        text_formating_control_panel(workpath, module_choice, keyword)
        ops.append(module_choice)
    hasFileOps = (__format_choice__ in ops) or (__blend_choice__ in ops)
    return hasFileOps

def end_processing(workpath, hasFileOps):
    if hasFileOps:
        # 将原Excel文件移入备份文件夹
        # 创建备份文件夹
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        backup_dir = workpath+__params__["backup_excel folder"]+current_time
        os.makedirs(backup_dir, exist_ok=True)
        # 遍历Excel
        with os.scandir(workpath) as filelist:
            for file in filelist:
                if isExcel(file.name) and not isIgnoredFile(file.name):
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
                    if file.name == __params__["redundancy_file name"] or isIgnoredFile(file.name):
                        output_name = file.path
                    else:
                        output_name = workpath + str(output_counter) + ".xlsx"
                    print("+"*15)
                    if hasFileOps or isIgnoredFile(file.name):
                        print("正在写入"+output_name)
                        print(df_from_txt)
                        dfTextToExcel(output_name, df_from_txt)

    # 遍历txt
    with os.scandir(workpath) as filelist:
        for file in filelist:
            if file.name.endswith('.txt'):
                # 删除txt
                os.remove(file.path)


if __name__ == '__main__':
    # choice for quiting
    __quit_choice__ = __params__["quit choice"]

    # 选择工作目录
    while True:
        workpath = input("输入目标文件夹（直接点击Enter为所在父文件夹）：")
        if not workpath:
            workpath = os.path.abspath(os.path.join(os.getcwd(), ".."))+"/"
            print("Working in", workpath)
        if os.path.isdir(workpath):
            break
    
    start_processing(workpath)
    hasFileOps = controlPanel_processExcel(workpath)
    end_processing(workpath, hasFileOps)

    # pause
    os.system('pause')