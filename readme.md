# Format text

### Functions
* Format all the files .txt in a **folder**
* **Capitalize** the lines
* **Add '.'** in the end of a line if not existed
* Change the **',' into '.'** in the end of a line
* Split the top and bottom **spaces** in a line
* Delete **double spaces** in lines
* Delete first caracter if it's **not alphabetic**
* Delete all **blank** lines
* Delete lines shorter than **4** words
* Delete lines with **':'**
* Delete all **repeated** lines
* Delete the lines **too long**
* Delete the lines that have **numbers**
* Display the number of **valid** lines of each file
* Disorganize **randomly** all the texts in the .txt files in a folder
* Delete **repeated** texts on the scale of **folder**
* Delete **backup(.bak)** files

### Use guide
Put the ``format_text.py`` file into the folder with .txt files to format, then just **run** the script.

#### Options
##### When the program ask you to choose a operation: 
0. Tap "0" for **quiting** the program
1. Tap "1" for **formating** the .txt files
2. Tap "2" for **blending** all the lines in the .txt files in a folder 
3. Tap "3" for **deleting** all the .bak files in a folder 

### Constants
Change the configurations as we want : 
* Minimum words : 
  * Change the value here in the "config.json" file : ``__min_words__ = 4``
* Maximum caracters :
  * Change the value here just below the minimum words : 
  ``__max_caracters__ = 110``
* Maximum lines :
  * Change the value here just below the Maximum caracters : 
  ``__max_lines__ = 1000``

___________

### 更新
2020-05-02:
* 标准化一个**文件夹**中的所有txt文档的格式
* 首字母**大写**
* 句尾加**句号**
* 句尾**逗号**改成**句号**
* 消除句子首尾**空格**
* 删除句中的**双空格**
* 删除**非字母**的头字符
* 删除**空行**
* 删除小于**n个**单词的句子
* 删除**重复行**
* 删除**过长**的句子
* 删除**带数字**的句子
* 显示**合格**行数
* **随机**打乱一个文件夹中所有txt文件中的句子，并将打乱后的句子重新分配至不同文件中
* 在**文件夹**尺度上删除**重复**句子
* 删除**备份文件（.bak）**

2021-08-19:
* 处理写在Excel上的句子

2021-08-25:
* 将新Excel按数字命名，旧文件存入备份文件夹
* 加入config.json文件，可自定义参数

2021-09-02:
* 删除**省略号**
* 删除或替换非法字符
* 删除句末标点前的空格
* 删除或替换非法多字符组合
* 加入replacement.json文件，可自定义非法组合及对应的替换内容
* 删除大于**n个**单词的句子

2021-09-04:
* 支持 xls 和 xltx 格式的Excel文件

2021-09-05:
* 移动备份文件夹名和多余句文件名等参数至config.json中
* 可单独调用``loadParams()``和``loadReplacements()``函数

2021-09-07:
* 删除含敏感词的句子
* 在bullshits.json中按语言定义敏感词

2021-09-08:
* 搜索文件夹中含有关键词的句子，并写入关键词文档
* 支持中文标准化及打乱
* 优化文件处理，可添加忽略文件，包含忽略文件关键词的文件不会被标准化和打乱处理
* 优化敏感词处理
* 优化从txt中提取字符串，可定义是否允许重复，是否保存文件
* 更改分隔符为``\t``
* 优化Excel处理，未进行标准化或打乱的操作时不会移动原文件或重命名文件

2021-09-24:
* 忽略以~$开头的mac临时文件
* 添加可视化操作界面

2021-10-11:
* 优化mac界面的按钮显示
* 如果甚于句数多于1000，则将每1000剩余句放入新文档中

### 用法
把 ``format_text.py`` 文件放入含有待审核的txt文档的文件夹内, 然后**运行**该脚本就行了。

#### 选项
##### 当程序要求你输入执行选项时: 
0. 输入 "0" 以**退出**程序
1. 输入 "1" 以执行**标准化**txt文档
2. 输入 "2" 以执行**打乱** 文件夹中所有txt文档内的句子
3. 输入 "3" 以执行**删除** 文件夹中所有.bak文件

#### 常量
可根据需要改变设置 : 
* 调整**最小单词数** : 
  * 在 "config.json" 文件改变这里的数值 : <br>
  ``__min_words__ = 4``


* 调整**最大字符数** :
  * 改变这里的数值: <br>
  ``__max_caracters__ = 110``


* 调整**最大句子数** :
  * 改变这里的数值: <br>
  ``__max_lines__ = 1000``