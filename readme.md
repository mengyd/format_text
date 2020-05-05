# Format text

### Functions
* Format all the files .txt in a **folder**
* **Capitalize** the lines
* **Add '.'** in the end of a line if not existed
* Change the **',' into '.'** in the end of a line
* Split the top and bottom **spaces** in a line
* Delete all **blank** lines
* Delete lines shorter than **4** words
* Delete lines with **':'**
* Delete all **repeated** lines
* Delete the lines **too long**
* Delete the lines that have **numbers**
* Display the number of **valid** lines of each file
* Disorganize **randomly** all the texts in the .txt files in a folder
* Delete **repeated** texts on the scale of **folder**

### Use guide
Put the ``format_text.py`` file into the folder with .txt files to format, then just **run** the script.

#### Options
##### When the program ask you to choose a operation: 
0. Tap "0" for **quiting** the program
1. Tap "1" for **formating** the .txt files
2. Tap "2" for **blending** all the lines in the .txt files in a folder 

### Constants
Change the minimum words and maximum caracters in a line as we want : 
* Minimum words : 
  * Change the value here at the top of the "format_text.py" file : ``__min_words__ = 4``
* Maximum caracters :
  * Change the value here just below the minimum words : 
  ``__max_caracters__ = 110``

___________

### 功能
* 标准化一个**文件夹**中的所有txt文档的格式
* 首字母**大写**
* 句尾加**句号**
* 句尾**逗号**改成**句号**
* 消除句子首尾**空格**
* 删除**空行**
* 删除小于**4个**单词的句子
* 删除带**冒号**的句子
* 删除**重复行**
* 删除**过长**的句子
* 删除**带数字**的句子
* 显示**合格**行数
* **随机**打乱一个文件夹中所有txt文件中的句子，并将打乱后的句子重新分配至不同文件中
* 在**文件夹**尺度上删除**重复**句子

### 用法
把 ``format_text.py`` 文件放入含有待审核的txt文档的文件夹内, 然后**运行**该脚本就行了。

#### 选项
##### 当程序要求你输入执行选项时: 
0. 输入 "0" 以**退出**程序
1. 输入 "1" 以执行**标准化**txt文档
2. 输入 "2" 以执行**打乱** 文件夹中所有txt文档内的句子

#### 常量
可根据需要改变要求的最小单词数和最大字符数 : 
* 调整**最小单词数** : 
  * 在 "format_text.py" 文件顶部改变这里的数值 : <br>
  ``__min_words__ = 4``


* 调整**最大字符数** :
  * 改变这里的数值（ 在 "format_text.py" 文件顶部，在最小单词数下面）: <br>
  ``__max_caracters__ = 110``