from loadconfig import loadParams
import tkinter as tk
from tkinter.constants import DISABLED, END, X
from tkinter import Frame, filedialog, messagebox
from FormatText import text_formating_control_panel
from ProcessExcels import start_processing, end_processing

__params__ = loadParams()

def onClick_btn_chooseFile():
    entry_chooseFile.delete(0, END)
    file_path = filedialog.askdirectory(title='选择待处理文件夹的位置！', initialdir='../')
    entry_chooseFile.insert('end', file_path)

def center_window(window, w, h):
    # 获取屏幕 宽、高
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

def decor_button(window, text, command, model="default"):
    bg_color = __params__["button_model"][model][0]
    fg_color = __params__["button_model"][model][1]
    btn = tk.Button(window, text=text, relief='flat', bg=bg_color, fg=fg_color, font=('Arial', 12), width=10, height=1, command=command)
    return btn

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
        messagebox.showinfo('提示','标准化已完成', parent=textFormatPage)
    def onClick_btnBlend():
        text_formating_control_panel(dir_path, __blend_choice__)
        ops.append(__blend_choice__)
        messagebox.showinfo('提示','打乱已完成', parent=textFormatPage)
    def onClick_btnDelete():
        text_formating_control_panel(dir_path, __delete_bak_choice__)
        ops.append(__delete_bak_choice__)
        messagebox.showinfo('提示','删除备份已完成', parent=textFormatPage)
    def onClick_btnSearch():
        text_formating_control_panel(dir_path, __search_keyword_choice__, entry_search.get())
        ops.append(__search_keyword_choice__)
        messagebox.showinfo('提示','搜索结果已添加至：'+entry_search.get()+'_查询结果', parent=textFormatPage)
    def onClick_btnFinish():
        if choice == 'Excel处理':
            hasFileOps = (__format_choice__ in ops) or (__blend_choice__ in ops)
            end_processing(dir_path, hasFileOps)
        textFormatPage.destroy()
    def onClose_textFormatPage():
        onClick_btnFinish()

    if not entry_chooseFile.get():
        messagebox.showwarning('警告','未指定工作文件夹！')
    elif not lst_Modules.curselection():
        messagebox.showwarning('警告','未指定执行模组！')
    else:
        choice = lst_Modules.get(lst_Modules.curselection())
        dir_path = entry_chooseFile.get() + '/'
        ops = []
        textFormatPage = tk.Toplevel(homepage)
        center_window(textFormatPage, 500, 350)
        textFormatPage.attributes("-topmost", 1)
        textFormatPage.protocol('WM_DELETE_WINDOW', onClose_textFormatPage)

        var_lable_workpath = tk.StringVar(textFormatPage, value='Working on: ' + dir_path)
        lable_workpath = tk.Label(textFormatPage, bg='black', fg='white',font=('Arial', 12), width=800, textvariable=var_lable_workpath)
        lable_workpath.pack(side='top')

        topFrame_textFormatPage = Frame(textFormatPage)
        topFrame_textFormatPage.pack(side='top', expand=True, fill=['x'])

        centerFrame_textFormatPage = Frame(textFormatPage)
        centerFrame_textFormatPage.pack(fill=['x'])

        bottomFrame_textFormatPage = Frame(textFormatPage)
        bottomFrame_textFormatPage.pack(side='bottom', expand=True)

        # btn_format = tk.Button(centerFrame_textFormatPage, text="标准化文档", font=('Arial', 12), width=10, height=1, command=onClick_btnFormat)
        btn_format = decor_button(centerFrame_textFormatPage, "标准化文档", onClick_btnFormat, "primary")
        # btn_blend = tk.Button(centerFrame_textFormatPage, text="打乱文档内容", font=('Arial', 12), width=10, height=1, command=onClick_btnBlend)
        btn_blend = decor_button(centerFrame_textFormatPage, "打乱文档内容", onClick_btnBlend, "primary")
        # btn_delete = tk.Button(centerFrame_textFormatPage, text="删除备份文件", font=('Arial', 12), width=10, height=1, command=onClick_btnDelete)
        btn_delete = decor_button(centerFrame_textFormatPage, "删除备份文件", onClick_btnDelete, "warning")
        btn_format.pack(side='left', expand=True)
        btn_blend.pack(side='left', expand=True)
        btn_delete.pack(side='left', expand=True)

        entry_search = tk.Entry(topFrame_textFormatPage, show=None, font=('Arial', 10), width=50)
        entry_search.pack(side='left', expand=True)
        # btn_search = tk.Button(topFrame_textFormatPage, text="搜索", font=('Arial', 12), width=10, height=1, command=onClick_btnSearch)
        btn_search = decor_button(topFrame_textFormatPage, "搜索", onClick_btnSearch, "info")
        btn_search.pack(side='right', expand=True)

        # btn_Finish = tk.Button(bottomFrame_textFormatPage, text="完成", font=('Arial', 12), width=10, height=1, command=onClick_btnFinish)
        btn_Finish = decor_button(bottomFrame_textFormatPage, "完成", onClick_btnFinish, "success")
        btn_Finish.pack()
        
        if choice == 'txt处理':
            textFormatPage.title('txt处理')
        elif choice == 'Excel处理':
            start_processing(dir_path)
            textFormatPage.title('Excel处理')

if __name__ == '__main__':
    homepage = tk.Tk()
    homepage.title("Home Page")
    center_window(homepage, 500, 300)

    topFrame = Frame(homepage)
    topFrame.pack(side='top', fill=['x'], expand=True)

    listModules = ['Excel处理','txt处理']
    lst_Modules = tk.Listbox(homepage)
    for module in listModules:
        lst_Modules.insert('end', module)

    btn_selectMods = decor_button(homepage, "选择", onClick_btn_selectMods, "primary")
    btn_chooseFile = decor_button(topFrame, "选择文件夹", onClick_btn_chooseFile, "info")
    entry_chooseFile = tk.Entry(topFrame, show=None, font=('Arial', 10), width=50)

    entry_chooseFile.pack(side='left', expand=True)
    btn_chooseFile.pack(side='right', expand=True)
    lst_Modules.pack(expand=True)
    btn_selectMods.pack(expand=True)

    homepage.mainloop()

