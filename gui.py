from loadconfig import loadParams
import tkinter as tk
from tkinter.constants import DISABLED, END, X
from tkinter import filedialog
from typing import Text
from FormatText import text_formating_control_panel
from ProcessExcels import start_processing, controlPanel_processExcel, end_processing

__params__ = loadParams()

def onClick_btn_chooseFile():
    entry_chooseFile.delete(0, END)
    file_path = filedialog.askdirectory(title='选择待处理文件的位置！', initialdir='../')
    entry_chooseFile.insert('end', file_path)

def onClick_btn_selectMods():
    # choice for formating
    __format_choice__ = __params__["format choice"]
    # choice for blending
    __blend_choice__ = __params__["blend choice"]
    # choice for delete backup file
    __delete_bak_choice__ = __params__["delete backup choice"]
    # choice for searching keywords
    __search_keyword_choice__ = __params__["search keyword choice"]
    def onClick_btnFormat():
        text_formating_control_panel(dir_path, __format_choice__)
        ops.append(__format_choice__)
    def onClick_btnBlend():
        text_formating_control_panel(dir_path, __blend_choice__)
        ops.append(__blend_choice__)
    def onClick_btnDelete():
        text_formating_control_panel(dir_path, __delete_bak_choice__)
        ops.append(__delete_bak_choice__)
    def onClick_btnSearch():
        text_formating_control_panel(dir_path, __search_keyword_choice__, entry_search.get())
        ops.append(__search_keyword_choice__)

    def onClick_btnNewExcels():
        hasFileOps = (__format_choice__ in ops) or (__blend_choice__ in ops)
        end_processing(dir_path, hasFileOps)
        processExcelPage.destroy()


    choice = lst_Modules.get(lst_Modules.curselection())
    dir_path = entry_chooseFile.get() + '/'
    ops = []
    if choice == '文本处理':
        textFormatPage = tk.Toplevel(homepage)
        textFormatPage.geometry('1000x800')
        textFormatPage.title('Text Format')

        var_lable_workpath = tk.StringVar(textFormatPage, value='Working on: ' + dir_path)
        lable_workpath = tk.Label(textFormatPage, bg='green', fg='yellow',font=('Arial', 12), width=800, textvariable=var_lable_workpath)
        lable_workpath.pack()

        btn_format = tk.Button(textFormatPage, text="标准化文档", font=('Arial', 12), width=10, height=1, command=onClick_btnFormat)
        btn_blend = tk.Button(textFormatPage, text="打乱文档内容", font=('Arial', 12), width=10, height=1, command=onClick_btnBlend)
        btn_delete = tk.Button(textFormatPage, text="删除备份文件", font=('Arial', 12), width=10, height=1, command=onClick_btnDelete)
        btn_format.pack()
        btn_blend.pack()
        btn_delete.pack()

        entry_search = tk.Entry(textFormatPage, show=None, font=('Arial', 10), width=50)
        entry_search.pack()
        btn_search = tk.Button(textFormatPage, text="搜索", font=('Arial', 12), width=10, height=1, command=onClick_btnSearch)
        btn_search.pack()

    elif choice == 'Excel处理':
        start_processing(dir_path)
        processExcelPage = tk.Toplevel(homepage)
        processExcelPage.geometry('1000x800')
        processExcelPage.title('Process Excels')

        var_lable_workpath = tk.StringVar(processExcelPage, value='Working on: ' + dir_path)
        lable_workpath = tk.Label(processExcelPage, bg='green', fg='yellow',font=('Arial', 12), width=800, textvariable=var_lable_workpath)
        lable_workpath.pack()

        btn_format = tk.Button(processExcelPage, text="标准化文档", font=('Arial', 12), width=10, height=1, command=onClick_btnFormat)
        btn_blend = tk.Button(processExcelPage, text="打乱文档内容", font=('Arial', 12), width=10, height=1, command=onClick_btnBlend)
        btn_delete = tk.Button(processExcelPage, text="删除备份文件", font=('Arial', 12), width=10, height=1, command=onClick_btnDelete)
        btn_format.pack()
        btn_blend.pack()
        btn_delete.pack()

        entry_search = tk.Entry(processExcelPage, show=None, font=('Arial', 10), width=50)
        entry_search.pack()
        btn_search = tk.Button(processExcelPage, text="搜索", font=('Arial', 12), width=10, height=1, command=onClick_btnSearch)
        btn_search.pack()

        btn_newExcels = tk.Button(processExcelPage, text="完成", font=('Arial', 12), width=10, height=1, command=onClick_btnNewExcels)
        btn_newExcels.pack()

if __name__ == '__main__':
    homepage = tk.Tk()
    homepage.title("Home Page")
    homepage.geometry("1200x720")

    listModules = ['Excel处理','文本处理']
    lst_Modules = tk.Listbox(homepage)
    for module in listModules:
        lst_Modules.insert('end', module)
    
    btn_selectMods = tk.Button(homepage, text="选择", font=('Arial', 12), width=10, height=1, command=onClick_btn_selectMods)
    btn_chooseFile = tk.Button(homepage, text="选择文件夹", font=('Arial', 12), width=10, height=1, command=onClick_btn_chooseFile)
    entry_chooseFile = tk.Entry(homepage, show=None, font=('Arial', 10), width=50)

    entry_chooseFile.pack()
    btn_chooseFile.pack()
    lst_Modules.pack()
    btn_selectMods.pack()


    homepage.mainloop()

