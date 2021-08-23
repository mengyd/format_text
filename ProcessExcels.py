from FormatText import text_formating_control_panel
import pandas as pd
import os

def readExcel(filename):
    source_df = pd.read_excel(filename, na_filter=False)
    return source_df

def dfExcelToText(filename, source_df):
    output_name = filename.replace('.xlsx', '.txt')
    with open(output_name, 'w', encoding='utf-8') as f:
        df_string = source_df.to_string(header=False, index=False)
        f.write(df_string)

def readText(filename):
    df_from_txt = pd.read_csv(filename, sep="*", header=None)
    return df_from_txt

def dfTextToExcel(filename, df_from_txt):
    output_name = filename.replace('.txt', '.xlsx')
    df_from_txt.to_excel(output_name, index=False, header=False)

def deleteEmptyExcelFromTxt(textname):
    excel_name = textname.replace('.txt', '.xlsx')
    os.remove(excel_name)


if __name__ == '__main__':
    # 选择工作目录
    while True:
        workpath = input("输入目标文件夹（直接点击Enter为所在文件夹）：")
        if not workpath:
            workpath = os.path.abspath(os.path.join(os.getcwd(), ".."))
            print("Working in", workpath)
        if os.path.isdir(workpath):
            break
    
    # 遍历Excel
    with os.scandir(workpath) as filelist:
        for file in filelist:
            if file.name.endswith('.xlsx'):
                # 读取Excel
                source_df = readExcel(file.name)
                # 写入TXT
                dfExcelToText(file.name, source_df)
    
    # TXT操作
    text_formating_control_panel(workpath)

    # 遍历TXT
    with os.scandir(workpath) as filelist:
        for file in filelist:
            if file.name.endswith('.txt'):
                # 只读非空文件
                if os.path.getsize(file.name) > 0 :
                    # 读取TXT
                    df_from_txt = readText(file.name)
                    # 写入Excel
                    print("正在写入"+file.name)
                    print(df_from_txt)
                    dfTextToExcel(file.name, df_from_txt)
                else:
                    deleteEmptyExcelFromTxt(file.name)

    # 遍历txt
    with os.scandir(workpath) as filelist:
        for file in filelist:
            if file.name.endswith('.txt'):
                # 删除txt
                os.remove(file.name)

    # pause
    os.system('pause')