# 第1章 快速入门

本章是Python的快速入门，它不涉及 python的特殊规则和细节，目标是通过示例使你快速了解Python语言的特点。本章简要介绍 了变量表达式、控制流、函数以及输入/输出的基本概念，不会涉及Python语言的高级特性。尽管如此，有经验的程序员还是能够通过阅读本章的材料创建高级程序。我们鼓励新人动手运行示例，亲身体验一把 Python。

### 1.1. 运行Python

Python 程序通过解释器执行。如果你的机器已经装好了python，简单的在命令行键 入python即可运行python解释器。在解释器运行的时，会有一个命令提示符 &gt;&gt;&gt;， 在提示符后键入你的程序语句，键入的语句将会立即执行。在下边的例子中，我们 在&gt;&gt;&gt;提示符后边键入最常见的显示"Hello World"的命令:

```text
Python 3.7.4 (default, Jul  9 2019, 18:13:23)
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")
```

```text
Hello World
>>>
```

```text
程序也可以像下面一样放置在一个文件中
```

```text
 # helloworld.py
 print("Hello World")
```

Python 源代码文件使用 `.py` 后缀。`'#'`表示本行后面的内容是注释。执行文件helloworld.py

```text
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

```text
 #!/usr/local/bin/python
 print("Hello World")
```

解释器会一直运行直到文件结束。如果在交互模式下，键入 EOF字符可以退出解释器。在 UNIX下，EOF字符是Ctrl+ D；在Windows下，EOF字符是Ctrl+Z。也可以在程序中使用 sys.exit\(\) 函数或者主动触发 SystemExit 异常来退出程序：

```text
 >>> import sys
 >>> sys.exit()
```

或者

```text
 >>> raise SystemExit
```

### 1.2. 变量和表达式

通过 Listing 1.1 所示的程序示例变量和表达式的用法  
 Listing 1.1 复利计算器\(Simple Compound-Interest Calculation\)

```text
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

```text
 1 1050.0
 2 1102.5
 3 1157.625
 4 1215.50625
 5 1276.2815625
```

Python 是一种动态语言，在程序运行过程中同一变量名可以在程序运行的不同阶段表示不同类型的值，比如整数、浮点数、列表或者元组\(tuple\)。事实上，程序中的变量名只是各种数据及对象的引用。这与C语言不同，C语言中变量名代表的是用来存放结果的一个固定位置及长度的内存片段。从例子 Listing 1.1 中的变量 principal 可以看出 Python语言的动态特性。最初它被赋值为一个整数，但是稍后程序将它再次赋值：

```text
principal = principal * (1 + rate)
```

这个语句计算表达式的值，然后将计算结果赋给 principal 变量做为它的新值。在这个赋值过程中，principal 由最初指向的值 1000，改为指向计算结果。它最初指向的值 1000 在计算结束后因为引用计数减少为零而被 Python 解释器自动丢弃。赋值动作结束，不但 principal 指向的值发生了变化，它指向的值的类型也随之发生了变化。在这个例子中，由于 rate 是一个浮点数，所以在赋值完成后，principal 也变成一个浮点数。

Python中每个语句以换行结束，你也可以在一行中写多个语句，这时语句之间必须使用用分号分隔，就象下面这样:

```text
principal = 1000; rate = 0.05; numyears = 5;
```

\(建议这样的写法仅仅用于调试语句，因为可以很方便的只删一行就删掉全部调试 语句\)

while 语句首先检查在它后边的循环条件，若条件表达式为真，它就执行冒号后面的语句块，然后再次检查循环条件，直至为假。冒号后面的缩进语句块为循环体。注意，Python语言使用缩进块来表示程序逻辑，这与其它大多数语言不同（那些语言通常使用使用大括号表示语句块\)。在 Listing 1.1中while语句后的三条语句为循环体，在每次循环中均执行。Python并未指定缩进的空白\(空格和制表符\)数目，唯一的要求是同一层次\(Level\)的语句必须使用相同的缩进空白。\(注意，要么都是空格，要么都是制表符，不可以混用\)

Listing 1.1中的程序美中不足的就是输出不是很好看，为了让它美观一点,可以用格 式字符串将计算结果只保留小数点后两位:

```text
 print("%3d %0.2f" % (year, principal))
```

这样,程序的输出就变为:

```text
 1 1050.00
 2 1102.50
 3 1157.63
 4 1215.51
 5 1276.28
```

格式字符串包含普通文本及格式化字符序列，例如`"%d"`、 `"%s"`、 和 `"%f"`，这些序列决定特定类型的数据的输出格式。`'%3d'`将一个整数在宽度为3个字符的栏中右对齐，`'%0.2f'`将一个浮点数的小数点后部分转换为2位。格式字符串的作用和C语言中的`sprintf()`函数基本相同。详细内容请参阅[第4章 运算符及表达式。](di-4-zhang-yun-suan-fu-yu-biao-da-shi.md)

### 1.3. 条件语句

`if` 和 `else` 语句用来做简单的逻辑测试，比如：

```text
# Compute the maximum (z) of a and b (得到a与b中较大的一个)
if a < b:
    z = b
else:
    z = a
```

if和else的语句块用缩进来表示，else从句在某些情况下可以省略。 如果if或else语句 块只有一个语句，也可以不使用缩近。也就是说:

这样的写法也是合法的，但这不是推荐的作法。一直使用缩近可以让你方便的在语 句体中添加一个语句，而且读起来更清晰。 若某个子句不需任何操作,就使用pass语 句，如:

通过使用 or,and 和 not 关键字你可以建立任意的条件表达式:

用 elif 语句可以检验多重条件\(用于代替其它语言中的switch语句\):

Toggle line numbers

```text
   1 if a<b: z=a
   2 else: z=b
```

Toggle line numbers

1 if a &lt; b:  
 2 pass \# Do nothing 3 else:  
 4 z=a

Toggle line numbers

```text
   1 if b >= a and b <= c:
   2         print "b is between a and c"
   3 if not (b < a or b > c):
   4         print "b is still between a and c"
```

Toggle line numbers

```text
   1 if a == '+':
   2         op = PLUS
   3 elif a == '-':
   4         op = MINUS
   5 elif a == '*':
   6         op = MULTIPLY
   7 else:
   8         raise RuntimeError, "Unknown operator"
```

1.4. 文件输入/输出

下面的程序打开一个文件,然后一行行地读出并显示文件内容:

open\(\)函数返回一个新文件对象\(file object\)。通过调用此对象的不同方法可以对文 件进行不同的操作。readline\(\)方法读取文件的一行\(包括换行符'\n'\)。如果读到 文件末尾，就返回一个空字符串。要将程序的输出内容由屏幕重定向到文件中，可 以使用'&gt;&gt;'运算符，如下例:

Toggle line numbers

```text
1 f = open("foo.txt")
2 line = f.readline()
3 while line:
```

1. 4  print line,
2. ```text
   5          line = f.readline()
   ```

6 f.close\(\)

```text
# Returns a file object
# Invokes readline() method on file
```

```text
# trailing ',' omits newline character
```

当然,文件对象也拥有write\(\)方法，通过它可以向文件对象写入新的数据。例如上 边例子中的print的语句也可以写成这样:

```text
f.write("%3d   %0.2f\n" % (year,principal))
```

1.5. 字符串

要创建一个字符串，你使用单引号,双引号或三引号将其引起来，如下例:

一个字符串用什么引号开头，就必须用什么引号结尾。两上三引号之间的一切都作 为字符串的内容,对应的单引号与双引号却只能创建单行字符串。如下例:

字符串是一个以0开始，整数索引的字符序列,要获得字符串 s 中的第 i+1 个字符\(别 忘了0是第一个\),使用索引操作符 s\[i\]:

要获得一个子串,使用切片运算符 s\[i:j\]。 它返回字符串 s 中从索引 i \(包括i\)到 j \(不包 括 j\)之间的子串。若 i 被省略，python就认为 i=0，若 j 被省略，python就认为 j=len\(s\)-1:

可以用加\(+\)运算符来连结字符串:  
 g = a + " This is a test" 通过使用str\(\)函数,repr\(\)函数或向后的引号\(\`\)可以将其他类型的数据转换为字符串:

Toggle line numbers

```text
   1 a = 'Hello World'
   2 b = "Python is groovy"
   3 c = """What is footnote 5?"""
```

Toggle line numbers

```text
   1 print '''Content-type: text/html
   2
   3 <h1> Hello World </h1>
   4 Click <a href="http://www.python.org">here</a>.
   5 '''
```

Toggle line numbers

```text
   1 a = "Hello World"
   2 b = a[4]                # b = 'o'
```

Toggle line numbers

```text
   1 c = a[0:5]
   2 d = a[6:]
   3 e = a[3:8]
```

```text
# c = "Hello"
# d = "World"
# e = "lo Wo"
```

Toggle line numbers

Toggle line numbers

```text
   1 f = open("out","w")     # Open file for writing
   2 while year <= numyears:
```

1. ```text
      3          principal = principal*(1+rate)
   ```
2. 4  print &gt;&gt;f,"%3d %0.2f" %% \(year,principal\) \#将格式文本输出到

文件对象 f  
 5 year += 1 6 f.close\(\)

repr\(\)函数用来取得对象的规范字符串表示，向后的引号\(\`\)是repr\(\)函数的快捷版。 在大多情况下str\(\)和repr\(\)函数会返回同一个结果,但是它们之间有很微妙的差别,后边

```text
的章节对此将有详细描述。
```

### 1.6. 列表和元组\(Lists & Tuples\)

就如同字符串是字符的序列,列表和元组则是任意对象的序列。象下面这样就可以创 建一个列表:

```text
names = [ "Dave", "Mark", "Ann", "Phil" ]
```

列表和元组都是以整数0来开始索引的序列,你可以用索引操作符来读取或者修改列 表中特定元素的值:

```text
a = names[2]
names[0] = "Jeff"
```

用len\(\)函数得到列表的长度:

```text
print len(names)
```

```text
 # Returns the third item of the list, "Ann"
 # Changes the first item to "Jeff"
```

\# prints 4

append\(\)方法可以把一个新元素插入列表的末尾:

```text
names.append("Kate")
```

aList.insert\(index,aMember\)方法可以把新元素 aMember 插入到列表 aList\[index\]

元素之前:  
 names.insert\(2, "Sydney"\) 用切片操作符可以取出一个子列表或者对子列表重新赋值:

b = names\[0:2\]  
 c = names\[2:\]  
 "Phil", "Kate" \]  
 names\[1\] = 'Jeff'  
 with "Jeff"  
 names\[0:2\] = \['Dave','Mark','Jeff'\] 个元素

```text
# Returns [ "Jeff", "Mark" ]
# Returns [ "Sydney", "Ann",
```

\# Replace the 2nd item in names  
 \# 用右边的 list 替换 names 列表中的前两

加\(+\)运算符可以连结列表:  
 a = \[1,2,3\] + \[4,5\] \# Result is \[1,2,3,4,5\] 列表元素可以是任意的 Python 对象,当然也包括列表:  
 a = \[1,"Dave",3.14, \["Mark", 7, 9, \[100,101\]\], 10\]

```text
1 s = "The value of x is " + str(x)
2 s = "The value of y is " + repr(y)
3 s = "The value of y is " + `y`
```

子列表的元素用下面的方式调用:

```text
a[1]
a[3][2]
a[3][3][1]
```

```text
# Returns "Dave"
# Returns 9
# Returns 101
```

Listing 1.2中代码从一个文件中读取一系列数字，然后输出其中的最大值和最小值。 通过这个示例我们可以了解到列表的一些高级特性:

Listing 1.2 列表的高级特性

Toggle line numbers

1 import sys

\# Load the sys module \(导入sys模  
 \# Filename on the command line  
 \# Read all lines into a list \(读出

块\)

2 f = open\(sys.argv\[1\]\) \(从命令行读取文件名\)

3 svalues = f.readlines\(\) 所有行到一个列表\)

4 f.close\(\)  
 5  
 6 \# Convert all of the input values from strings to floats \(把输入的值

转换为浮点数\)  
 7 fvalues = \[float\(s\) for s in svalues\]  
 8  
 9 \# Print min and max values \(输出最大值和最小值\)

```text
  10 print "The minimum value is ", min(fvalues)
  11 print "The maximum value is ", max(fvalues)
```

程序第一行用import语句从Python library中导入sys模块。 你需要在命令行提供一个文件名给上面的程序，该文件名参数保存在sys.argv 列表

中，open方法通过读取sys.argv\[1\]得到这个文件名参数。 readlines\(\)方法读取文件中的所有的行到一个列表中。

表达式 \[float\(s\) for s in svalues\] 通过循环列表svalues中的所有字符串并对每个元素运 行函数float\(\)来建立一个新的列表,这种特殊的建立列表的方法叫做列表包含\( list comprehension\)。 在列表中所有的字符串都转换为浮点数之后,内建函数min\(\)和max \(\)计算出列表中的最大值及最小值。

元组\(tuple\)类型和列表关系很密切,通过用圆括号中将一系列逗号分割的值括起来可 以得到一个元组:

在某些时候，即使没有圆括号, Python仍然可以根据上下文认出这是一个元组，如: \(为了写出更清晰可读的程序，建议你不要依赖 Python 的智能\)

```text
 a = 1,4,5,-9,10
 b = 7,
 person = first_name, last_name, phone
```

Toggle line numbers

```text
   1 a = (1,4,5,-9,10)
```

2 b = \(7,\) \# 一个元素的元组 \(注意一定要 加一个额外的逗号!\)

```text
   3 person = (first_name, last_name, phone)
```

元组支持大多数列表的操作,比如索引,切片和连结。一个关键的不同是你不能在一个 tuple创建之后修改它的内容。也就是说,你不能修改其中的元素,也不能给tuple添加 新的元素。

1.7. 循环

通过使用while语句，我们在前面已经简单介绍了 while 循环。在Python中另一种循 环结构是 for 循环，它通过 迭代 一个序列\(例如字符串,列表,或者tuple等\)中的每个元 素来建立循环。下边是一个例子:

```text
 for i in range(1,10):
         print "2 to the %d power is %d" % (i, 2**i)
```

range\(i,j\)函数建立一个整数序列,这个序列从第 i 数开始\(包括 i \)到第 j 数为止\(不包括 j\)。若第一个数被省略，它将被认为是0。该函数还可以有第三个参数，步进值，见 下面的例子:

```text
a = range(5)
b = range(1,8)
c = range(0,14,3)
d = range(8,1,-1)
```

```text
# a = [0,1,2,3,4]
# b = [1,2,3,4,5,6,7]
# c = [0,3,6,9,12]
# d = [8,7,6,5,4,3,2]
```

for语句可以迭代任何类型的序列:

```text
 a = "Hello World"
 # Print out the characters in a
 for c in a:
```

```text
         print c
 b = ["Dave","Mark","Ann","Phil"]
```

```text
 # Print out the members of a list
 for name in b:
```

print name

range\(\)函数根据起始值，终止值及步进值三个参数在内存中建立一个列表，当需要 一个很大的列表时,这个既占内存又费时间。为了克服它的缺点,Python提供了xrange \(\)函数:

```text
 for i in xrange(1,10):
         print "2 to the %d power is %d" % (i, 2**i)
```

```text
 a = xrange(100000000)       # a = [0,1,2, ..., 99999999]
 b = xrange(0,100000000,5)   # b = [0,5,10, ...,99999995]
```

xrange\(\)函数只有在需要值时才临时通过计算提供值，这大大节省了内存。 1.8. 字典

字典就是一个关联数组\(或称为哈希表\)。它是一个通过关键字索引的对象的集合。 使用大括号{}来创建一个字典，如下 例:

a= {  
 "username" : "beazley",

```text
        "home" : "/home/beazley",
```

"uid" : 500 }

用关键字索引操作符可以访问字典的某个特定值: u = a\["username"\]

d = a\["home"\] 用下面的方式插入或者修改对象:

```text
 a["username"] = "pxl"
 a["home"] = "/home/pxl"
 a["shell"] = "/usr/bin/tcsh"
```

尽管字符串是最常见的 关键字\(key\) 类型，你还是可以使用很多其它的 python 对象 做为字典的关键字，比如 数字 和 tuple，只要是不可修改对象，都可以用来做字典 的key。有些对象,例如列表和字典,不可以用来做字典的key,因为他们的内容是允许 更改的。

我们可以使用 has\_key\(\) 方法来检验一个键/值对是否存在\(或者in操作符\):

```text
 if a.has_key("username"):
      username = a["username"]
```

```text
 else:
      username = "unknown user"
```

上边的操作还可以用更简单的方法完成:  
 username = a.get\("username", "unknown user"\)  
 字典的keys\(\) 方法返回由所有关键字组成的列表:  
 k = a.keys\(\) \# k = \["username","home","uid","shell"\] del语句可以删除字典中的特定元素:  
 del a\["username"\]

1.9. 函数

在Python中，使用def语句来创建函数，如下例:

```text
 def remainder(a,b):
         q = a/b
```

```text
         r = a - q*b
         return r
```

要调用一个函数，只要使用函数名加上用括号括起来的参数就可以了。比如result = remainder\(37,15\),如果你打算让函数返回多个值，就让它返回一个元组好了。\(当 然，只要你愿意，让它返回一个列表我们也不会介意\)

```text
 def divide(a,b):
         q = a/b        # If a and b are integers, q is an integer
         r = a - q*b
         return (q,r)
```

当返回一个 tuple 时，你会发现象下面这样调用函数会很有用: quotient, remainder = divide\(1456,33\) 你也可以象下面这样给函数的参数指定一个默认值:

```text
 def connect(hostname,port,timeout=300):
       # Function body
```

```text
若在函数定义的时候提供了默认参数，那么在调用函数时就允许省略这个参数:
```

```text
connect('www.python.org', 80)
```

你也可以使用关键字参数来调用函数,这样你的参数就可以使用任意顺序:

```text
connect(port=80,hostname="www.python.org")
```

函数内部定义的变量为局部变量，要想在一个函数内部改变一个全局变量的值，在 函数中使用global语句:

Toggle line numbers

```text
   1 a = 4.5
   2 ...
   3 def foo():
```

1. 4  global a
2. 5  a = 8.8

\# 改变全局变量 a

1.10. 类

Python支持面向对象编程，在面向对象编程中，class语句用于定义新类型的对象。 例如，下面这个类定义了一个简单的堆栈:

Toggle line numbers

```text
   1 class Stack(object):
```

2 3 4 5 6 7 8 9

def \_\_init\_\_\(self\): \# 初始化栈 self.stack = \[ \]

```text
def push(self,object):
        self.stack.append(object)
```

```text
def pop(self):
        return self.stack.pop()
```

```text
def length(self):
        return len(self.stack)
```

在类定义中,方法用 def 语句定义。类中每个方法的第一个参数总是引用类实例对象 本身，大家习惯上使用 self 这个名字代表这个参数。不过这仅仅是个习惯而已，如 果你愿意也可以用任意的别的名字。不过为了别人容易看懂你的程序，最好还是跟

随大家的习惯。类的方法中若需要调用实例对象的属性则必须显式使用self变量\(如 上所示\)。方法名中若前后均有两个下划线，则表示这是一个特殊方法，比如init方 法被用来初始化一个对象\(实例\)。

象下面这样来使用一个类:

Toggle line numbers

```text
   1 s = Stack()
   2 s.push("Dave")
   3 s.push(42)
   4 s.push([3,4,5])
   5 x = s.pop()
   6 y = s.pop()
   7 del s
```

\# Create a stack \(创建\)  
 \# Push some things onto it \(写入\)

\# x gets \[3,4,5\] \(读取\) \# y gets 42  
 \# Destroy s \(删除\)

1.11. 异常

如果在你的程序发生了一个错误，就会引发异常\(exception\),你会看到类似下面的错 误信息:

```text
 Traceback (most recent call last):
  File "<interactive input>", line 42, in foo.py
```

NameError: a

错误信息指出了发生的错误类型及出错位置，通常情况下，错误会导致程序终止。 不过你可以使用 try 和 except 语句来捕获并处理异常:

```text
 try:
     f = open("file.txt","r")
```

```text
 except IOError, e:
     print e
```

上面的语句表示:如果有 IOError 发生，造成错误的详细原因将会被放置在对象 e 中，然后运行 except 代码块。 若发生其他类型的异常，系统就会将控制权转到处理 该异常的 except 代码块，如果没有找到该代码块，程序将运行终止。若没有异常发 生，except代码块就被忽略掉。

raise语句用来有意引发异常，,你可以使用内建异常来引发异常，如下例: raise RuntimeError, "Unrecoverable error"

当然，你也可以建立你自己的异常，这将在 第五章--控制流中的定义新的异常中详 细讲述。

1.12. 模块

当你的程序变得越来越大，为了便于修改和维护，你可能需要把它们分割成多个相 关文件。 Python允许你把函数定义或公共部分放入一个文件，然后在其他程序或者 脚本中将该文件作为一个模块导入。要创建一个模块，把相应的语句和定义放入一 个文件，这个文件名就是模块名。\(注意:该文件必须有.py后缀\):

Toggle line numbers

要在其它的程序中使用这个模块，使用import语句:

```text
 import div
 a, b = div.divide(2305, 29)
```

import语句创建一个新的名字空间，该空间包含模块中所有定义对象的名称。要访 问这个名字空间，把模块名作为一个前缀来使用这个模块内的对象，就像上边例子 中那样:div.divide\(\)

如果你希望使用一个不同的模块名字访问这个模块，给import语句加上一个 as 模块 名 部分就可以了:

```text
 import div as foo
 a,b = foo.divide(2305,29)
```

如果你只想导入指定的对象到当前的名称空间,使用 from 语句:

from div import divide  
 a,b = divide\(2305,29\) \# No longer need the div prefix \(不再需要div 前缀\)

导入一个模块中的所有内容到当前的名称空间: from div import \*

最后，内建函数dir\(\)可以列出一个模块中的所有可访问内容。当你在python交互环境中测试一 个模块的功能时，这会是一个很有用的工具，因为它可以提供一个包含可用函数及变量的列表:

```text
 >>> import string
 >>> dir(string)
 ['_ _builtins_ _', '_ _doc_ _', '_ _file_ _', '_ _name_ _', '_idmap',
```

```text
  '_idmapL', '_lower', '_swapcase', '_upper', 'atof', 'atof_error',
  'atoi', 'atoi_error', 'atol', 'atol_error', 'capitalize',
  'capwords', 'center', 'count', 'digits', 'expandtabs', 'find',
```

... &gt;&gt;&gt;

