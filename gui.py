import tkinter as tk
from tkinter.constants import DISABLED, END
from tkinter import filedialog
from typing import Text

def homePageSetup():
    homepage = tk.Tk()
    homepage.title("Home Page")
    homepage.geometry("1200x720")
    return homepage

def modulesListSetup():
    listModules = ['Excel处理','文本处理']
    lst = tk.Listbox(homepage)
    for module in listModules:
        lst.insert('end', module)
    return lst

def onClick_formatOptions(var):
    print(var.get())

def formatTextOptionsSetup(window=None):
    var = tk.StringVar()
    ops1 = tk.Radiobutton(window, text='标准化', variable=var, value='1', command=onClick_formatOptions(var))
    ops2 = tk.Radiobutton(window, text='打乱', variable=var, value='2', command=onClick_formatOptions(var))
    ops3 = tk.Radiobutton(window, text='删除备份', variable=var, value='3', command=onClick_formatOptions(var))
    ops1.pack()
    ops2.pack()
    ops3.pack()
    return var

def formatTextPageSetup(workpath):
    textFormatPage = tk.Toplevel(homepage)
    textFormatPage.geometry('1000x800')
    textFormatPage.title('Text Format')

    var_lable = tk.StringVar(textFormatPage, value='Working on: ' + workpath)
    lable_workpath = tk.Label(textFormatPage, bg='green', fg='yellow',font=('Arial', 12), width=800, textvariable=var_lable)
    lable_workpath.pack()

    var = formatTextOptionsSetup(window=textFormatPage)

    print(var.get(), "...")
    
    return textFormatPage

def processExcelPageSetup(workpath):
    processExcelPage = tk.Toplevel(homepage)
    processExcelPage.geometry('1000x800')
    processExcelPage.title('Process Excel')
    var_lable = tk.StringVar(processExcelPage, value='Working on: ' + workpath)
    lable_workpath = tk.Label(processExcelPage, bg='green', fg='yellow',font=('Arial', 12), width=800, textvariable=var_lable)
    lable_workpath.pack()
    return processExcelPage

def onClick_btn_chooseFile():
    entry_chooseFile.delete(0, END)
    file_path = filedialog.askdirectory(title='选择影像存放的位置！', initialdir='../')
    entry_chooseFile.insert('end', file_path)

def chooseFileEntrySetup():
    entry = tk.Entry(homepage, show=None, font=('Arial', 10), width=50)
    return entry

def chooseFileBtnSetup():
    btn = tk.Button(homepage, text="选择文件夹", font=('Arial', 12), width=10, height=1, command=onClick_btn_chooseFile)
    return btn

def onClick_btn_selectMods():
    value = lst_Modules.get(lst_Modules.curselection())
    dir_path = entry_chooseFile.get()
    print(dir_path)
    if value == '文本处理':
        formatTextPageSetup(dir_path)
    elif value == 'Excel处理':
        processExcelPageSetup(dir_path)

def selectBtnSetup():
    btn = tk.Button(homepage, text="选择", font=('Arial', 12), width=10, height=1, command=onClick_btn_selectMods)
    return btn

if __name__ == '__main__':
    homepage = homePageSetup()
    lst_Modules = modulesListSetup()
    btn_selectMods = selectBtnSetup()
    btn_chooseFile = chooseFileBtnSetup()
    entry_chooseFile = chooseFileEntrySetup()

    entry_chooseFile.pack()
    btn_chooseFile.pack()
    lst_Modules.pack()
    btn_selectMods.pack()


    homepage.mainloop()

