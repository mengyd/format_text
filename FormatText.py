import os
import re
import random

__software__ = "FormatText"
__author__ = "MENG Yidong"
__version__ = "2.0"

# minimum words 最少词数
__min_words__ = 4
# maximum caracters 最大字符数
__max_caracters__ = 1100
# maximum lines 最大句子数
__max_lines__ = 1000
# choice for quiting
__quit_choice__ = "0"
# choice for formating
__format_choice__ = "1"
# choice for blending
__blend_choice__ = "2"
# choice for delete backup file
__delete_bak_choice__ = "3"

def format_text_by_file(filename: str = None):
    """
    Format text in a certain way
    """

    linecounter = 0 
    appearedlines = []
    # open original file
    f1 = open(filename, 'r', encoding='UTF-8')
    # create and open result file
    f2 = open(filename+".bak", 'w', encoding='UTF-8')
    # format line by line
    for s in f1.readlines():
        if s == "\n":
            # delete blank line
            # print("删除空行")
            # print(s)
            # print("-" * 20)
            pass
        # elif ":" in s:
        #     # delete line with ':'
        #     # print("删除冒号")
        #     # print(s)
        #     # print("-" * 20)
        #     pass
        else:
            # strip and capitalize the line
            s = s.strip().capitalize()

            # delete mutiple spaces
            while "  " in s:
                s = s.replace("  ", " ")

            # delete first letter if it's not alphabetic
            # if not s[0].isalpha:
            #     s = s[1:].strip().capitalize()

            if s.endswith('.') or s.endswith('!') or s.endswith('?'):
                pass
            else:
                # replace ',' by '.' at the end of the line
                s = s.rstrip(',') + '.'

            if s in appearedlines:
                # delete if the formatted line appealed already
                # print("删除重复")
                # print(s)
                # print("-" * 20)
                pass
            elif len(s) > __max_caracters__:
                # delete if too long
                # print("deleted long")
                # print("删除长句")
                pass 
            elif len(s.split(' ')) < __min_words__:
                # delete line which is too short
                # print("删除过短")
                # print(s)
                # print("-" * 20)
                pass
            # elif re.search(r'\d', s) is not None:
            #     # delete if have numbers
            #     # print("deleted num")
            #     # print("删除数字句")
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

def extract_text_in_file(filename: str = None, appeared_lines = None):
    """
    read and return contents of a file
    """
    lines_in_file = []
    # open file
    f = open(filename, 'r', encoding='UTF-8')
    # read file line by line
    for s in f.readlines():
        if s in appeared_lines:
            # delete(ignore) if the line appealed already
            pass
        else:
            lines_in_file.append(s)

    # close the files
    f.close()
    # rename file to .bak
    os.replace(filename, filename+".bak")
    # print("extracted", len(lines_in_file), "lines in", filename)
    print("从", filename, "中读取", len(lines_in_file), "行。")
    return lines_in_file

def write_text_into_file(filename: str = None, lines = None):
    """
    Write every 1000 lines of contents in the list into a file
    """
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

def write_all_in_one_file(lines = None):
    """
    write all lines into rest.txt
    """
    frest = open("rest.txt", 'w', encoding='UTF-8')
    frest.writelines(lines[:])
    print("+" * 30)
    print(len(lines), "lines left, writing into rest.txt")
    print("+" * 30, "\n")
    frest.close()
    

def text_formating_control_panel(workpath):

    # Choice for operations
    module_choice = __format_choice__

    while True:

        # ask for module to use
        # module_choice = input("Please choose a operation( " + \
        #                     __format_choice__ + " for formating, " + \
        #                     __blend_choice__ + " for blending, " + \
        #                     __delete_bak_choice__ + " for delete backup files, " + \
        #                     __quit_choice__ + " for quiting. ) : ")
        module_choice = input("请输入一个执行选项代码( " + \
                            __format_choice__ + " 为标准化文档, " + \
                            __blend_choice__ + " 为打乱文档内容, " + \
                            __delete_bak_choice__ + " 为删除备份文件, " + \
                            __quit_choice__ + " 为退出程序。 ) : ")
        
        if module_choice == __quit_choice__:
            # print("quit...")
            print("退出程序...")
            break

        # parse the working directory
        with os.scandir(workpath) as filelist:
            if module_choice == __format_choice__: # format texts
                for txtfile in filelist:
                    # do the formating for all the txt files
                    if txtfile.name.endswith(".txt"):
                        linenumber = format_text_by_file(filename=txtfile.name)
                        repalce_file(filename=txtfile.name)
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
                    if txtfile.name.endswith(".txt"):
                        # print("reading", txtfile.name)
                        print("正在读取", txtfile.name)
                        lines_in_folder.extend(extract_text_in_file(\
                            filename=txtfile.name, appeared_lines=lines_in_folder))
                        filenames_in_folder.append(txtfile.name)
                # print("extracted", len(lines_in_folder), "lines")
                print("共读取", len(lines_in_folder), "行")
                # disorganize randomly the lines
                random.shuffle(lines_in_folder)
                # parse the folder
                for file_name in filenames_in_folder:
                    lines_in_folder = write_text_into_file(filename=file_name, lines=lines_in_folder)
                # if we have more lines left
                if len(lines_in_folder) > 0:
                    # write them all into rest.txt
                    write_all_in_one_file(lines=lines_in_folder)
                # print("blending done!")
                print("打乱 完成!")
            # TODO: delete .bak files
            elif module_choice == __delete_bak_choice__: # delete backup files
                for backupfile in filelist:
                    if backupfile.name.endswith(".bak"):
                        os.remove(backupfile.name)
                # print("deleting done!")
                print("删除 完成!")
                
            print("-" * 40)


''' ----------------------------Main----------------------------- '''
if __name__ == '__main__':
    # Informations
    print(__software__,  "v"+__version__)
    print("Author :", __author__)
    print('-' * 40)

    # get current working directory
    workpath = os.getcwd()
    print('<' * 40)
    print("Working in:", workpath)
    print('>' * 40)

    text_formating_control_panel(workpath)

    # pause
    os.system('pause')