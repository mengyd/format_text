import os
import re

__software__ = "strip_text"
__author__ = "MENG Yidong"
__version__ = "1.0"

__max_caracters__ = 110

def format_text_file(filename: str = None):
    """
    Delete the top, bottom spaces and blank lines
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
        elif len(s.split(' ')) < 4:
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
            else:
                # add into appeared list
                appearedlines.append(newstring)
                # write into new file
                f2.write(newstring + "\n")
                linecounter += 1

                # check length
                if len(newstring) > __max_caracters__:
                    print("*" * 30)
                    print("\tLine '", linecounter, "' is longer than", __max_caracters__, "caracters:")
                    print("\t", newstring)

                # check number
                if re.search(r'\d', newstring) is not None:
                    print("*" * 30)
                    print("\tLine '", linecounter, "' has number:")
                    print("\t", newstring)

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

# Informations
print(__software__,  "v"+__version__)
print("Author :", __author__)
print('-' * 40)

# get current working directory
workpath = os.getcwd()
print("Working in:", workpath)
print('-' * 40)
lines = 0

# parse the working directory
with os.scandir(workpath) as filelist:
    for txtfile in filelist:
        # do the operations for all the txt files
        if txtfile.name.endswith(".txt"):
            linenumber = format_text_file(filename=txtfile.name)
            repalce_file(filename=txtfile.name)
            print(txtfile.name, "treated; ", linenumber, "lines")
            print("-" * 40)

# pause
os.system('pause')