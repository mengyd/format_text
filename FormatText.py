from loadconfig import loadConfig
import os
import re
import random

__software__ = "FormatText"
__author__ = "MENG Yidong"
__version__ = "2.2"


__params__, __replacements__, __bullshits__ = loadConfig()

def control_illegal_characters(stringToControl):
    # illegal characters 非法字符
    __illegal_chars__ = __params__["illegal characters"]

    for c in __illegal_chars__:
        if c in stringToControl:
            print("find '" + c + "'")
            stringToControl = stringToControl.replace(c, " ")
            print("replaced by space")
            print("*"*10)
    return stringToControl

def control_illegal_combinations(stringToControl):
    for key in __replacements__.keys():
        if key in stringToControl:
            # print("+"*10, stringToControl, key)
            stringToControl = stringToControl.replace(key, __replacements__[key])
            # print(stringToControl, "-"*10)
    return stringToControl

def is_real_bullshit(bullshit):
    if len(bullshit) > 1:
        return True
    return False

def has_bullshits(stringToControl):
    lang = __params__["required lang"]
    try:
        for bullshit in __bullshits__[lang]:
            if bullshit in stringToControl and is_real_bullshit(bullshit):
                for word in stringToControl.split(" "):
                    if bullshit == word.strip(" ,.!?"):
                        return True
    except Exception:
        pass
    return False

def contain_zh(phrase):
    zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
    phrase_bytes = bytes(phrase, 'utf-8')
    phrase_bytes = phrase_bytes.decode()
    match = zh_pattern.search(phrase_bytes)
    return match

def format_text_by_file(filename: str = None):
    """
    Format text in a certain way
    """
    # minimum words 最少词数
    __min_words__ = __params__["minimun words"]
    # maximum words 最大词数
    __max_words__ = __params__["maximum words"]
    # maximum characters 最大字符数
    __max_characters__ = __params__["maximum characters"]

    linecounter = 0 
    appearedlines = []
    # open original file
    f1 = open(filename, 'r', encoding='UTF-8', errors='ignore')
    # create and open result file
    f2 = open(filename+".bak", 'w', encoding='UTF-8')
    # format line by line
    for s in f1.readlines():
        if s != "\n": # delete blank line

            # illegal combinations control
            s = control_illegal_combinations(s)
                
            # illegal characters control
            s = control_illegal_characters(s)

            # strip and capitalize the line
            s = s.strip().capitalize()

            # delete mutiple spaces
            while "  " in s:
                s = s.replace("  ", " ")

            # delete first letter if it's not alphabetic
            # if not s[0].isalpha:
            #     s = s[1:].strip().capitalize()

            # replace ',' by '.' at the end of the line, add . if not exist
            if s.endswith(',') or s.endswith(' ') or (len(s)>0 and s[-1].isalnum()):
                s = s.rstrip(',').rstrip(' ') + '.'

            # remove space in front of the last punctuation
            if len(s) > 1 and s[-2] == ' ' and not s[-1].isalnum():
                s = s.rstrip(s[-2]+s[-1]) + s[-1]


            if s in appearedlines:
                # delete if the formatted line appealed already
                # print("删除重复", s)
                # print("-" * 20)
                pass
            elif len(s) > __max_characters__ or len(s.split(' ')) > __max_words__:
                # delete if too long
                # print("deleted long")
                # print("删除长句", s)
                # print("-" * 20)
                pass 
            elif len(s.split(' ')) < __min_words__ and __params__["required lang"]!="zh":
                # delete line which is too short
                # print("删除过短", s)
                # print("-" * 20)
                pass
            elif has_bullshits(s):
                # delete if has sensitive words
                pass
            elif __params__['required lang']!="zh" and contain_zh(s):
                print("有汉字：", s)
            # elif re.search(r'\d', s) is not None:
            #     # delete if have numbers
            #     # print("删除数字句", s)
            #     pass
            else:
                # add into appeared list
                appearedlines.append(s)
                # write into new file
                f2.write(s + "\n")
                linecounter += 1
                
    # close the files
    f1.close()
    f2.close()
    return linecounter

def repalce_file(filename: str = None):
    """
    Delete the old file and replace it with the new one
    """
    os.remove(filename)
    os.replace(filename+".bak", filename)

def extract_text_in_file(filename: str = None, appeared_lines = [], disallow_repeat = True, save_bak = True):
    """
    read and return contents of a file
    """
    lines_in_file = []
    # open file
    f = open(filename, 'r', encoding='UTF-8')
    # read file line by line
    for s in f.readlines():
        if (s in appeared_lines) and disallow_repeat:
            # delete(ignore) if the line appealed already
            pass
        else:
            lines_in_file.append(s)

    # close the files
    f.close()
    if save_bak:
        # rename file to .bak
        os.replace(filename, filename+".bak")
    print("从", filename, "中读取", len(lines_in_file), "行。")
    return lines_in_file

def write_text_into_file(filename: str = None, lines = None):
    """
    Write every 1000 lines of contents in the list into a file
    """

    # maximum lines 最大句子数
    __max_lines__ = __params__["maximum lines"]

    # Create and open a file for writing
    f = open(filename, 'w', encoding='UTF-8')
    # if we have enough texts
    if len(lines) > __max_lines__:
        # write 1000 lines into the file
        f.writelines(lines[:__max_lines__])
        # print("writing in", filename, ",", __max_lines__, "lines.")
        print("写入", filename, ",", __max_lines__, "行。")
        # delete these 1000 lines from the list
        del(lines[:__max_lines__])
    # if we don't have 1000 texts
    elif len(lines) > 0:
        # write all the rest into the file
        f.writelines(lines)
        # print("writing in", filename, ",", len(lines), "lines")
        print("写入", filename, ",", len(lines), "行")
        # empty the list
        lines.clear()
    else:
        # print("writing in", filename, ", 0 lines")
        print("写入", filename, ", 0 行")
    # close file
    f.close()

    return lines

def write_all_in_one_file(workpath, lines = None):
    """
    write all lines into rest.txt
    """
    frest = open(workpath + __params__["redundancy_file name"], 'w', encoding='UTF-8')
    frest.writelines(lines[:])
    print("+" * 30)
    print(len(lines), "lines left, writing into "+__params__["redundancy_file name"])
    print("+" * 30, "\n")
    frest.close()

def isIgnoredFile(filename):
    for element in __params__["ignored file"]:
        if element in filename:
            return True
    return False

def askForKeyword():
    while True:
        keyword = input("请输入要查找的关键字：")
        if keyword:
            print("查找："+keyword)
            return keyword

def find_words(workpath, keyword):
    list_keywordLines = []
    # parse working directory
    with os.scandir(workpath) as filelist:
        for file in filelist:
            if file.name.endswith('.txt') and os.path.getsize(file.path) > 0 and not isIgnoredFile(file.name):
                extractedlines = extract_text_in_file(filename=file.path,disallow_repeat=False,save_bak=False)
                lineCounter = 0
                # if the sentence has keyword
                for line in extractedlines:
                    lineCounter += 1
                    # put keyword in list
                    if keyword in line:
                        list_keywordLines.append(line.strip().rstrip("\n")+"\t"+file.name.rstrip(".txt")+"\t"+str(lineCounter))

    # write list into file named by keyword
    filename = workpath+keyword + "_查询结果.txt"
    print("查询结果已输出至："+filename)
    fKeyword = open(filename, 'a', encoding='UTF-8')
    for line in list_keywordLines:
        fKeyword.write(line + "\n")
    fKeyword.close()
    
def askForOption():    
    # choice for quiting
    __quit_choice__ = __params__["quit choice"]
    # choice for formating
    __format_choice__ = __params__["format choice"]
    # choice for blending
    __blend_choice__ = __params__["blend choice"]
    # choice for delete backup file
    __delete_bak_choice__ = __params__["delete backup choice"]
    # choice for searching keywords
    __search_keyword_choice__ = __params__["search keyword choice"]
    
    # Choice for operations
    module_choice = __format_choice__
    keyword = ""
    # ask for module to use
    module_choice = input("请输入一个执行选项代码( " + \
                        __format_choice__ + " 为标准化文档, " + \
                        __blend_choice__ + " 为打乱文档内容, " + \
                        __delete_bak_choice__ + " 为删除备份文件, " + \
                        __search_keyword_choice__ + " 为搜索关键词, " + \
                        __quit_choice__ + " 为退出程序。 ) : ")

    if module_choice == __search_keyword_choice__:
        keyword = askForKeyword()

    return module_choice, keyword

def text_formating_control_panel(workpath, module_choice, keyword=""):
    # choice for quiting
    __quit_choice__ = __params__["quit choice"]
    # choice for formating
    __format_choice__ = __params__["format choice"]
    # choice for blending
    __blend_choice__ = __params__["blend choice"]
    # choice for delete backup file
    __delete_bak_choice__ = __params__["delete backup choice"]
    # choice for searching keywords
    __search_keyword_choice__ = __params__["search keyword choice"]

    # parse the working directory
    with os.scandir(workpath) as filelist:
        if module_choice == __format_choice__: # format texts
            for txtfile in filelist:
                # do the formating for all the txt files
                if txtfile.name.endswith(".txt") and not isIgnoredFile(txtfile.name):
                    linenumber = format_text_by_file(filename=txtfile.path)
                    repalce_file(filename=txtfile.path)
                    # print(txtfile.name, "treated; ", linenumber, "lines")
                    print(txtfile.name, "已处理; ", linenumber, "行")
                    print("-" * 40)
            # print("formating done!")
            print("标准化 完成!")
        elif module_choice == __blend_choice__: # blend texts
            lines_in_folder = []
            filenames_in_folder = []
            for txtfile in filelist:
                # extract from all the txt files
                if txtfile.name.endswith(".txt") and not isIgnoredFile(txtfile.name):
                    # print("reading", txtfile.name)
                    print("正在读取", txtfile.name)
                    lines_in_folder.extend(extract_text_in_file(\
                        filename=txtfile.path, appeared_lines=lines_in_folder))
                    filenames_in_folder.append(txtfile.path)
            # print("extracted", len(lines_in_folder), "lines")
            print("共读取", len(lines_in_folder), "行")
            # disorganize randomly the lines
            random.shuffle(lines_in_folder)
            newFileCounter = 0
            # parse the folder
            for file_name in filenames_in_folder:
                lines_in_folder = write_text_into_file(filename=file_name, lines=lines_in_folder)
            # if we have more lines left
            while len(lines_in_folder) > 1000:
                newFileCounter+=1
                newFileName = workpath + str(newFileCounter) + ".txt"
                if not os.path.isfile(newFileName):
                    lines_in_folder = write_text_into_file(filename=newFileName, lines=lines_in_folder)
            if len(lines_in_folder) > 0:
                # write them all into rest.txt
                write_all_in_one_file(workpath, lines=lines_in_folder)
            # print("blending done!")
            print("打乱 完成!")
        elif module_choice == __delete_bak_choice__: # delete backup files
            for backupfile in filelist:
                if backupfile.name.endswith(".bak"):
                    os.remove(backupfile.path)
            # print("deleting done!")
            print("删除 完成!")
        elif module_choice == __search_keyword_choice__: # search keyword
            find_words(workpath, keyword)
            
        print("-" * 40)


if __name__ == '__main__':
    # Informations
    print(__software__,  "v"+__version__)
    print("Author :", __author__)
    print('-' * 40)

    # choice for quiting
    __quit_choice__ = __params__["quit choice"]

    # get current working directory
    workpath = workpath = os.path.abspath(os.path.join(os.getcwd(), ".."))+"/"
    print('<' * 40)
    print("Working in:", workpath)
    print('>' * 40)

    while True:
        module_choice, keyword = askForOption()
        if module_choice == __quit_choice__:
            # print("quit...")
            print("退出程序...")
            break
        text_formating_control_panel(workpath, module_choice, keyword)

    # pause
    os.system('pause')