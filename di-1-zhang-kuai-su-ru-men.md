# 第1章 快速入门

本章是`Python`的快速入门，它不涉及 `Python` 的特殊规则和细节，目标是通过示例使你快速了解`Python`语言的特点。本章简要介绍 了变量表达式、控制流、函数以及输入/输出的基本概念，不会涉及`Python`语言的高级特性。尽管如此，有经验的程序员还是能够通过阅读本章的材料创建高级程序。我们鼓励新人动手运行示例，亲身体验一把 `Python`。

### 1.1. 运行Python

`Python` 程序通过解释器执行。如果你的机器已经装好了`Python`，简单的在命令行键 入`python`即可运行`python`解释器。在解释器运行的时，会有一个命令提示符 `>>>`， 在提示符后键入你的程序语句，键入的语句将会立即执行。在下边的例子中，我们在`>>>` 提示符后边键入最常见的显示`"Hello World"`的命令:

```python
Python 3.7.4 (default, Jul  9 2019, 18:13:23)
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")
Hello World
>>>
```

程序也可以像下面一样放置在一个文件中

```python
 # helloworld.py
 print("Hello World")
```

Python 源代码文件使用 `.py` 后缀。`'#'`表示本行后面的内容是注释。执行文件helloworld.py

```python
 % python helloworld.py
 Hello World
 %
```

在Windows 下，只需双击一个.py文件就能执行这个python程序。windows会自动调用 python 解释程序，然后启动一个终端窗口\(类DOS窗口\)来执行它。在这种情况下,

终端窗口会在程序执行完毕后立即关闭\(经常是在你看到它的输出之前\)。为避免这 个问题,你可以使用 python 集成开发环境，例如 IDLE 或 Pythonwin。另一个可行的方法是建立一个 bat文件，在文件写入这样一行语句，如 python -i helloworld.py。运行这个 批处理，程序在执行完成后会自动进入python解释器。

在解释器中,也可以通过函数execfile\(\)来运行一个保存在磁盘上的程序,如下例: 

`>>> execfile("helloworld.py")  
Hello World`

在UNIX下，你可以在程序的首行写入 \#! 魔法字符串来自动调用python解释器执行你的脚本。

```python
 #!/usr/local/bin/python
 print("Hello World")
```

解释器会一直运行直到文件结束。如果在交互模式下，键入 EOF字符可以退出解释器。在 UNIX下，EOF字符是Ctrl+ D；在Windows下，EOF字符是Ctrl+Z。也可以在程序中使用 sys.exit\(\) 函数或者主动触发 SystemExit 异常来退出程序：

```python
 >>> import sys
 >>> sys.exit()
```

或者

```python
 >>> raise SystemExit
```

### 1.2. 变量和表达式

通过 Listing 1.1 所示的程序示例变量和表达式的用法  
 Listing 1.1 复利计算器\(Simple Compound-Interest Calculation\)

```python
principal = 1000 # Initial amount (本金)
rate = 0.05   # Interest rate (利率)
numyears = 5  # Number of years (期数,年)
year = 1
while year <= numyears:          
    principal = principal * (1 + rate)
    print(year, principal)
    year += 1
```

程序输出:

```python
 1 1050.0
 2 1102.5
 3 1157.625
 4 1215.50625
 5 1276.2815625
```

Python 是一种动态语言，在程序运行过程中同一变量名可以在程序运行的不同阶段表示不同类型的值，比如整数、浮点数、列表或者元组\(tuple\)。事实上，程序中的变量名只是各种数据及对象的引用。这与C语言不同，C语言中变量名代表的是用来存放结果的一个固定位置及长度的内存片段。从例子 Listing 1.1 中的变量 principal 可以看出 Python语言的动态特性。最初它被赋值为一个整数，但是稍后程序将它再次赋值：

```python
principal = principal * (1 + rate)
```

这个语句计算表达式的值，然后将计算结果赋给 principal 变量做为它的新值。在这个赋值过程中，principal 由最初指向的值 1000，改为指向计算结果。它最初指向的值 1000 在计算结束后因为引用计数减少为零而被 Python 解释器自动丢弃。赋值动作结束，不但 principal 指向的值发生了变化，它指向的值的类型也随之发生了变化。在这个例子中，由于 rate 是一个浮点数，所以在赋值完成后，principal 也变成一个浮点数。

Python中每个语句以换行结束，你也可以在一行中写多个语句，这时语句之间必须使用用分号分隔，就象下面这样:

```python
principal = 1000; rate = 0.05; numyears = 5;
```

这样的写法建议仅用于临时添加的调试语句，因为可以很方便的注释或者删除。

while 语句首先检查在它后边的循环条件，若条件表达式为真，它就执行冒号后面的语句块，然后再次检查循环条件，直至为假。冒号后面的缩进语句块为**循环体**。注意，Python语言使用缩进块来表示程序逻辑，这与其它大多数语言不同（那些语言通常使用使用大括号表示语句块）。在 Listing 1.1 中while语句后的三条语句为循环体，在每次循环中均执行。Python并未规定缩进的空白数目，唯一的要求是同一层次\(Level\)的语句必须使用相同的空白数。\(注意，要么都是空格，要么都是制表符，不可以混用\)

Listing 1.1中的程序美中不足的就是输出不是很好看，为了让它美观一点,可以用格 式字符串将计算结果只保留小数点后两位:

```python
 print("%3d %0.2f" % (year, principal))
```

这样,程序的输出就变为:

```python
 1 1050.00
 2 1102.50
 3 1157.63
 4 1215.51
 5 1276.28
```

格式字符串包含普通文本及格式化字符序列，例如`"%d"`、 `"%s"`、 和 `"%f"`，这些序列决定特定类型的数据的输出格式。`'%3d'`将一个整数在宽度为3个字符的栏中右对齐，`'%0.2f'`将一个浮点数的小数点后部分转换为2位。格式字符串的作用和C语言中的`sprintf()`函数基本相同。详细内容请参阅[第4章 运算符及表达式。](di-4-zhang-yun-suan-fu-yu-biao-da-shi.md)

### 1.3. 条件语句

`if` 和 `else` 语句用来做简单的逻辑测试，比如：

```python
# Compute the maximum (z) of a and b (得到a与b中较大的一个)
if a < b:
    z = b
else:
    z = a
```

if 和 else 语句块用缩进表示，else 从句若不需要可以省略。 如果 if 或 else 语句块只有一个语句，也允许不使用缩近。也就是说:

```python
if a < b: z = a
else: z = b
```

这样的写法也是合法的，但并不推荐这样做。一直使用缩进使你的代码可读性更好，在需要往语句体中添加一个或多个语句时也更方便。 如果某个子句不需任何操作，请使用pass语句，如:

```python
if a < b:
    pass # Do nothing 
else:
    z = a
```

使用 `or`，`and` 和 `not` 关键字可组合成任意复杂的条件表达式：

```python
if b >= a and b <= c:
    print("b is between a and c")
if not (b < a or b > c):
    print("b is still between a and c")
```

用 `elif` 语句可以检验多重条件\(可代替其它语言中的`switch`语句\):


```python
if a == '+':
    op = PLUS
elif a == '-':
    op = MINUS
elif a == '*':
    op = MULTIPLY
else:
    raise RuntimeError, "Unknown operator"
```

### 1.4. 文件输入/输出

下面的程序打开一个文件，然后一行行地读出并显示文件内容:

```python
f = open("foo.txt") # Returns a file object
line = f.readline() # Invokes readline() method on file
while line:
    print(line, end='') # end='' 避免输出额外的空行
    line = f.readline()
f.close()
```

`open()` 函数返回一个新文件对象\(file object\)。通过调用此对象的不同方法可以对文 件进行不同的操作。`readline()` 方法读取文件的一行，包括换行符 `\n`。如果读到文件末尾，则返回一个空字符串。要将程序的输出内容由屏幕重定向到文件中，则需要给 `print` 函数增加一个`file` 参数，如下例:

```python
f = open("out","w")     # Open file for writing
while year <= numyears:
    principal = principal*(1+rate)
    print("%3d %0.2f" % (year,principal), file=f) #将格式文本输出到文件对象 f
    year += 1 
f.close()
```

也可以使用文件对象的 `write()` 方法向文件对象写入数据。例如上边例子中的 `print` 函数也可以改写为这样：

```python
f.write("%3d   %0.2f\n" % (year,principal))
```

### 1.5. 字符串

把一串字符用单引号，双引号或三引号引起来，你就得到一个字符串。如下例：

```python
a = 'Hello World'
b = "Python is groovy"
c = """What is footnote 5?"""
```

一个字符串以什么引号开头，就必须以什么引号结尾。两个三引号之间的一切，包括换行在内都视为字符串的内容，而单引号与双引号则更多的用来创建单行字符串（单引号与双引号也能够借助`\n` 转义符号创建多行字行串）。如下例:

```python
print('''Content-type: text/html

<h1> Hello World </h1>
Click <a href="http://www.python.org">here</a>.
''')
```

字符串是一个以 `0` 开始，整数索引的字符序列，要获得字符串 `s` 中的第 `i+1` 个字符\(别 忘记 `0` 是第一个\)，使用索引运算符 `s[i]`：

```python
a = "Hello World"
b = a[4]                # b = 'o'
```

要获得一个子串，使用切片运算符 `s[i:j]`。 它返回字符串 s 中从索引 `i` \(包括`i`\)到 `j` \(不包 括 `j`\)之间的子串。若 `i` 被省略，python就认为 `i=0`，若 `j` 被省略，python就认为 `j=len(s)-1`：

```python
c = a[0:5]   # c = "Hello"
d = a[6:]    # d = "World"
e = a[3:8]   # e = "lo Wo"
```

可以用加 `+` 运算符来连结字符串：  

```python  
g = a + " This is a test" 
```

使用 `str()` 函数, `repr()` 函数或反引号 \` 可以将其他类型的数据转换为字符串:

```python
s = "The value of x is " + str(x)
s = "The value of y is " + repr(y)
s = "The value of y is " + `y`
```
`repr()` 函数用来取得对象的规范字符串表示，向后的引号 \` 是 `repr()` 函数的快捷写法。在大多情况下 `str()` 和 `repr()` 函数会返回同样的结果，但是它们之间其实有很微妙的差别，在后边的章节我们将详细说明二者之间的区别。

### 1.6. 列表和元组\(Lists & Tuples\)

字符串是字符的序列，列表和元组则是对象的序列。象下面这样就创建出一个列表：

```python
names = [ "Dave", "Mark", "Ann", "Phil" ]
```

和字符串类似，列表和元组也是以整数 `0` 做为起始索引的序列。你可以用索引运算符来读取或者修改列表中某一元素的值：

```python
a = names[2]        # Returns the third item of the list, "Ann"
names[0] = "Jeff"   # Changes the first item to "Jeff"
```

`len()` 函数也支持得到列表的长度：

```python
print(len(names))   # prints 4
```

`append()` 方法用来把一个新元素添加到列表的末尾：

```python
names.append("Kate")
```

`aList.insert(index, aMember)` 方法把新元素 `aMember` 插入到列表 `aList[index]` 对应的元素之前:  
 
 ```python
 names.insert(2, "Sydney") 
 ```
 
 用切片运算符可以取出一个子列表，也可以对子列表重新赋值：

```python
b = names[0:2]     # Returns [ "Jeff", "Mark" ]
c = names[2:]      # Returns [ "Sydney", "Ann", "Phil", "Kate"]
names[1] = 'Jeff'  # Replace the 2nd item in names with "Jeff"  
names[0:2] = ['Dave', 'Mark', 'Jeff'] 用右边的 list 替换 names 列表中的前两个元素
```

加 `+` 运算符可以连结列表：

```python
a = [1,2,3] + [4,5]  # Result is [1,2,3,4,5] 
```

列表元素可以是任意的 Python 对象,当然也包括列表:  

```python
a = [1, "Dave", 3.14, ["Mark", 7, 9, [100, 101]], 10]
```

子列表的元素用下面的方式调用:

```python
a[1]            # Returns "Dave"     
a[3][2]         # Returns 9          
a[3][3][1]      # Returns 101        
```

Listing 1.2 中的代码从一个文件中读取一系列数字，然后输出其中的最大值和最小值。 借用这个示例我们可以了解到列表的一些高级特性:

Listing 1.2

```python
import sys                # 导入 sys 模块
f = open(sys.argv[1])     # 从命令行读取文件名
svalues = f.readlines()   # 读出所有行到一个列表
f.close()  

# 把列表中所有值转换为浮点数  
fvalues = [float(s) for s in svalues]  

# 输出最大值和最小值
print("The minimum value is ", min(fvalues))
print("The maximum value is ", max(fvalues))
```

把上面的代码保存为 `list-1.2.py`，接下来我们详细解释这个程序。

程序第一行用 `import` 语句从 `Python library` 中导入 `sys` 模块。
程序第二行打开 `sys.argv[1]` 对应的文件。这一行要求你在命令行提供一个有效的文件给上面的程序。

假设你输入下面这样一个命令：

```bash
python list-1.2.py file1 file2 file3
```

则在该程序中， `sys.argv` 的值将是 `['list-1.2.py', 'file1', 'file2', 'file3']`。显然 `sys.argv[1]` 就是我们提供给程序的第一个参数。实际上 `argv` 是 `argument values` 的缩写。

程序第三行用 `readlines()` 方法读取文件中的所有的行并将它们保存到列表 `svalues` 之中。

表达式 `[float(s) for s in svalues]` 通过循环列表 `svalues` 中的每一个字符串并对其运行函数 `float` 来得到一个全新的列表，新列表中的每一个元素都已经转换为浮点数。这种新颖的建立列表的方法称为列表推导式`(list comprehensio)`。 程序的最后两句，使用内建函数`min()`和`max ()`计算出列表中的最大值及最小值。

元组`(tuple)`类型和列表关系很密切，你可以将元组理解为它是只读的列表。将一系列逗号分割的值用小括号括起来就得到一个元组：

在某些时候，即使没有圆括号, `Python` 仍然可以根据上下文认出这是一个元组，例如：

```python
a = 1,4,5,-9,10
b = 7,
person = first_name, last_name, phone
```

不过，为了使程序更清晰可读，还是建议大家不要依赖 `Python` 的这种智能。


```python
a = (1,4,5,-9,10)
b = (7,)           # 一个元素的元组，注意一定要加一个额外的逗号!
person = (first_name, last_name, phone)
```

元组支持大多数列表运算，例如索引，切片和连结。与列表最关键的不同在于 `tuple` 是只读的，一经创建，就不可以再修改它的内容。你不能修改 `tuple` 中的元素，也不能给 `tuple` 添加或者删除元素。

### 1.7. 循环

在前面的章节，我们在使用 `while` 语句时，已经简单介绍了 while 循环。在 `Python` 语言中还有另一种循环结构，这就是 `for` 循环，它通过迭代一个序列，例如字符串，列表，或者 `tuple` 等的每一个元素来建立循环。请看下边的例子：

```python
for i in range(1,10):
    print("2 to the %d power is %d" % (i, 2**i))
```

`range(i, j)` 函数建立一个整数序列，这个序列从第 `i` 数开始\(包括 `i` \)到第 `j` 数为止\(不包括 `j`\)。若第一个数被省略，它将被认为是0。该函数还可以有第三个参数，即步进值，见下面的例子：

```python
a = range(5)                   # a = [0,1,2,3,4]      
b = range(1, 8)                # b = [1,2,3,4,5,6,7]  
c = range(0, 14, 3)            # c = [0,3,6,9,12]     
d = range(8, 1, -1)            # d = [8,7,6,5,4,3,2]  
```

`for` 语句可以迭代任何类型的序列：

```python
a = "Hello World"
# Print out the characters in a
for c in a:
    print c

b = ["Dave","Mark","Ann","Phil"]
# Print out the members of a list
for name in b:
    print name
```

在 `Python2.x` 中 `range()` 函数根据起始值，终止值及步进值三个参数在内存中建立了一个列表。当需要一个很大的列表时，初始化这个列表既占内存又费时间。 为了克服它的缺点，`Python2.x` 提供了 `xrange()` 函数。`xrange()` 函数只有在需要值时才临时通过计算提供值，这大大节省了内存。你也许已经发现在 `Python3.x` 中并没有提供 `xrange` 函数。这不是退步，简单起见，你可以认为 `Python3.x` 中的 `range` 就是 `Python2.x` 中的 `xrange`。 其实`Python3.x`中的`range`比`Python2.x`中的`xrange`还要强大的多。如果你想了解更多，请阅读<https://treyhunner.com/2018/02/python-3-s-range-better-than-python-2-s-xrange/> 这篇文章。


### 1.8. 字典

字典就是一个关联数组，也有人称之为哈希表。它是一个通过关键字做为索引的对象的集合。 `Python`使用大括号`{}`语法来创建一个字典，例如：

```python
a = {  
    "username" : "beazley",
    "home" : "/home/beazley",
    "uid" : 500 
}
```

用关键字索引运算符可以访问字典的某个值: 

```python
u = a["username"]
d = a["home"] 
```

用下面的方式插入或者修改对象:

```python
a["username"] = "pxl"
a["home"] = "/home/pxl"
a["shell"] = "/usr/bin/tcsh"
```

尽管人们通常使用字符串作为字典的关键字`(key)`，还有一些别的 `Python` 对象也可以作为字典的关键字，比如数字和 `tuple`，只要是不可修改对象，都可以用来做字典的key。也就是说有些对象，例如列表和字典，不可以用来做字典的key，因为他们的内容是允许修改的。

我们可以使用 `has_key()` 方法来检验字典中是否存在某个键/值对，也可以用 `in` 运算符来达到同样目的:

```python
if a.has_key("username"):
    username = a["username"]
else:
    username = "unknown user"
```

上边的操作还可以用更简单的方法完成:
  
```python
username = a.get("username", "unknown user")
```

字典的 `keys()` 方法返回由所有 `key` 组成的列表： 
 
```python
k = a.keys() # k = ["username", "home", "uid", "shell"] 
```
 
`del` 语句可以删除字典中的特定元素:  

```python
del a["username"]
```

### 1.9. 函数

在Python中，使用 `def` 语句来创建函数，如下例:

```python
def remainder(a, b):
    q = a // b
    r = a - q * b
    return r
```

要调用一个函数，只要使用函数名加上用括号括起来的参数就可以了。比如 `result = remainder(37, 15)`，如果需要让函数返回多个值，让它返回一个`tuple` 好了。当然，只要你愿意，让它返回一个列表我们也不介意。

```python
def divide(a,b):
    q = a // b        # If a and b are integers, q is an integer
    r = a - q * b
    return (q, r)
```

当返回一个 `tuple` 时，你会发现象下面这样调用函数会很有用: `quotient, remainder = divide(1456,33)` 你也可以象下面这样给函数的参数指定一个默认值:

```python
def connect(hostname, port, timeout=300):
    # Function body
```

如果在函数定义的时候提供了默认参数，那么在调用函数时就允许省略这个参数：

```python
connect('www.python.org', 80)
```

你也可以使用关键字参数来调用函数，这样你的参数就可以使用任意顺序:

```python
connect(port=80, hostname="www.python.org")
```

函数内部定义的变量为局部变量，要想在一个函数内部改变一个全局变量的值，在函数中使用`global`语句:

```python
a = 4.5
...
def foo():
    global a
    a = 8.8   # 改变全局变量 a 
```

### 1.10. 类

`Python` 支持面向对象编程，在面向对象编程中，`class` 语句用于定义一个类。 例如，下面这个类定义了一个简单的栈：


```python
class Stack(object):

    def __init__(self): # 初始化栈 
        self.stack = []
    
    def push(self,object):
        self.stack.append(object)
    
    def pop(self):
        return self.stack.pop()
    
    def length(self):
        return len(self.stack)
```

在类中，方法用 `def` 语句定义。类中每个方法的第一个参数总是引用类实例对象本身，使用 `self` 这个名字代表这个参数是一种习惯。不过这也仅仅是个习惯而已，如果你愿意使用别的名字，没有问题。不过为了别人容易看懂你的程序，建议还是跟随大家的习惯。类的方法中若需要调用实例对象的属性则必须显式使用`self`变量，如上所示。方法名中若前后均有两个下划线，则表示这是一个特殊方法，比如上面例子中的 `init` 方法，它用来初始化一个对象实例。

象下面这样来使用一个类:


```python
s = Stack()        # 创建栈实例
s.push("Dave")     # 进栈
s.push(42)         # 进栈
s.push([3,4,5])    # 进栈
x = s.pop()        # 出栈 x gets [3,4,5]   
y = s.pop()        # 出栈 y gets 42     
del s              # 删除栈实例
```

### 1.11. 异常

如果在你的程序在运行过程中发生了一个错误，就会触发异常 `exception`，你会看到类似下面的错误信息：

```python
Traceback (most recent call last):
  File "<interactive input>", line 42, in foo.py
NameError: a
```

错误信息指出了发生的错误类型以及出错位置，通常情况下，错误会导致程序终止。不过你可以使用 `try` 和 `except` 语句来捕获并处理异常：

```python
try:
    f = open("file.txt","r")
except IOError, e:
    print e
```

上面的语句表示：如果有 `IOError` 发生，造成错误的详细原因将会被放置在对象 `e` 中，然后运行 `except` 代码块。 若发生其他类型的异常，系统就会将控制权转到处理该异常的 `except` 代码块，如果没有找到该代码块，程序将运行终止。若程序运行过程中没有异常发生，`except` 代码块则被忽略。

`raise` 语句用来有意触发异常，你可以触发内建的异常，如下例: 

```python
raise RuntimeError, "Unrecoverable error"
```

当然，你也可以创建你自己的异常。这将在[第五章-控制流]()中的[定义新的异常]()一节中详细讲述。

### 1.12. 模块

当你的程序变得越来越大，为便于修改和维护，可能需要把它们分割成多个相关的文件。 `Python` 允许你把函数定义或多个文件所共同需要的那部分代码放入一个文件，然后在其他程序或者脚本中将该文件作为一个模块导入。要创建一个模块，把相应的语句和定义放入一个文件，这个文件的名字就是模块名。

```python
# file : div.py
def divide(a, b):
    q = a // b        # If a and b are integers, q is an integer
    r = a - q * b
    return (q, r)
```

注意:该文件必须有.py后缀。

要在其它的程序中使用这个模块，使用 `import` 语句:

```python
 import div
 a, b = div.divide(2305, 29)
```

`import` 语句创建了一个新的名字空间，该空间包含模块中所有定义对象的名称。要访问这个名字空间，把模块名作为一个前缀来使用这个模块内的对象，就像上边例子中那样: `div.divide()`

有时候为避免名字冲突，你希望使用一个不同的名字来访问这个模块，给`import`语句加上一个 `as` 模块名部分就可以了：

```python
import div as foo
a, b = foo.divide(2305, 29)
```

如果你只想导入指定的对象到当前的名字空间，使用 `from` 语句：

```python
from div import divide  
a, b = divide(2305,29) # 这种情况下不再需要div 前缀
```

导入一个模块中的所有内容到当前的名称空间: 

```python
from div import *
```

最后，内建函数`dir()`可以列出一个模块中的所有可访问内容。当你在python交互环境中测试一个模块的功能时，这会是一个很有用的工具，因为它提供了你想知道的包含所有可用函数及变量的列表：

```python
>>> import string
>>> dir(string)
['_ _builtins_ _', '_ _doc_ _', '_ _file_ _', '_ _name_ _', '_idmap',
  '_idmapL', '_lower', '_swapcase', '_upper', 'atof', 'atof_error',
  'atoi', 'atoi_error', 'atol', 'atol_error', 'capitalize',
  'capwords', 'center', 'count', 'digits', 'expandtabs', 'find',
... 
>>>
```
