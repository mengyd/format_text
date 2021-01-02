import os
import re
import random

__software__ = "strip_text"
__author__ = "MENG Yidong"
__version__ = "2.0"

# minimum words 最少词数
__min_words__ = 4
# maximum caracters 最大字符数
__max_caracters__ = 110
# choice for quiting
__quit_choice__ = "0"
# choice for formating
__format_choice__ = "1"
# choice for blending
__blend_choice__ = "2"

def format_text_by_file(filename: str = None):
    """
    Format text in a certain way
    """

    linecounter = 0 
    newstring = ""
    appearedlines = []
    # open original file
    f1 = open(filename, 'r', encoding='UTF-8')
    # create and open result file
    f2 = open(filename+".bak", 'w', encoding='UTF-8')
    # format line by line
    for s in f1.readlines():
        if s == "\n":
            # delete blank line
            pass
        elif len(s.split(' ')) < __min_words__:
            # delete line which is too short
            pass
        elif ":" in s:
            # delete line with ':'
            pass
        else:
            # strip and capitalize the line
            newstring = s.strip().capitalize()
            if newstring.endswith('.') or newstring.endswith('!') or newstring.endswith('?'):
                pass
            else:
                # replace ',' by '.' at the end of the line
                newstring = newstring.rstrip(',') + '.'

            if newstring in appearedlines:
                # delete if the formatted line appealed already
                pass
            elif len(newstring) > __max_caracters__:
                # delete if too long
                print("deleted long")
                pass
            elif re.search(r'\d', newstring) is not None:
                # delete if have numbers
                print("deleted num")
                pass
            else:
                # add into appeared list
                appearedlines.append(newstring)
                # write into new file
                f2.write(newstring + "\n")
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

def extract_text_in_file(filename: str = None):
    """
    read and return contents of a file
    """
    # open file
    f = open(filename, 'r', encoding='UTF-8')
    # read file
    lines_in_file = f.readlines()
    # close the files
    f.close()
    # rename file to .bak
    os.replace(filename, filename+".bak")
    print("extracted", len(lines_in_file), "lines in", filename)
    return lines_in_file

def write_text_into_file(filename: str = None, lines: [] = None):
    """
    Write every 1000 lines of contents in the list into a file
    """
    # Create and open a file for writing
    f = open(filename, 'w', encoding='UTF-8')
    # if we have enough texts
    if len(lines) > 1000:
        # write 1000 lines into the file
        f.writelines(lines[:1000])
        print("writing in", filename, ", 1000 lines.")
        # delete these 1000 lines from the list
        del(lines[:1000])
    # if we don't have 1000 texts
    elif len(lines) > 0:
        # write all the rest into the file
        f.writelines(lines)
        print("writing in", filename, ",", len(lines), "lines")
        # empty the list
        lines.clear()
    # close file
    f.close()

    return lines

def write_all_in_one_file(lines: [] = None):
    """
    write all lines into rest.txt
    """
    frest = open("rest.txt", 'w', encoding='UTF-8')
    frest.writelines(lines[:])
    print("+" * 30)
    print(len(lines), "lines left, writing into rest.txt")
    print("+" * 30, "\n")
    frest.close()

''' ----------------------------Main----------------------------- '''
# Informations
print(__software__,  "v"+__version__)
print("Author :", __author__)
print('-' * 40)

# Choice for operations
module_choice = __format_choice__

while True:
    # get current working directory
    workpath = os.getcwd()
    print('<' * 40)
    print("Working in:", workpath)
    print('>' * 40)

    # ask for module to use
    module_choice = input("Please choose a operation( " + \
                        __format_choice__ + " for formating, " + \
                        __blend_choice__ + " for blending, " + \
                        __quit_choice__ + " for quiting. ) : ")
    
    if module_choice == __quit_choice__:
        print("quit...")
        break

    # parse the working directory
    with os.scandir(workpath) as filelist:
        if module_choice == __format_choice__: # format texts
            for txtfile in filelist:
                # do the formating for all the txt files
                if txtfile.name.endswith(".txt"):
                    linenumber = format_text_by_file(filename=txtfile.name)
                    repalce_file(filename=txtfile.name)
                    print(txtfile.name, "treated; ", linenumber, "lines")
                    print("-" * 40)
        elif module_choice == __blend_choice__: # blend texts
            lines_in_folder = []
            filenames_in_folder = []
            for txtfile in filelist:
                # do the extraction for all the txt files
                if txtfile.name.endswith(".txt"):
                    print("reading", txtfile.name)
                    lines_in_folder.extend(extract_text_in_file(filename=txtfile.name))
                    filenames_in_folder.append(txtfile.name)
            print("extracted", len(lines_in_folder), "lines")
            # disorganize randomly the lines
            random.shuffle(lines_in_folder)
            # parse the folder
            for file_name in filenames_in_folder:
                lines_in_folder = write_text_into_file(filename=file_name, lines=lines_in_folder)
            # if we have more lines left
            if len(lines_in_folder) > 0:
                # write them all into rest.txt
                write_all_in_one_file(lines=lines_in_folder)
            
        print("-" * 40)


# pause
os.system('pause')