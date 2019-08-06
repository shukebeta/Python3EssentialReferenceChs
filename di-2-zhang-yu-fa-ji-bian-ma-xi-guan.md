# 第2章 语法及编码习惯

本章讲述`Python`程序的语法和代码约定。本章的主题有行结构，语句分组，保留字，字符串，运算符，`token`等等，另外对如何使用 `Unicode` 字符串也做了详细的描述。

## 2.1. 行结构/缩进

程序中的每个语句都以换行符结束。特别长的语句可以使用续行符`\`分成几个短行，如下例:

```python
import math  
a = math.cos(3 * (x - n)) + \
    math.sin(3 * (y - n))
```

定义三引号字符串、列表、tuple 或者字典时不需要续行符。也就是说，在程序中用圆括号`(...)`定义的`tuple`、用方括号`[...]`定义的列表、用花括号`{...}`定义的字典，以及用三引号`"""...."""`定义的字符串内不需要使用续行符。

缩进用来指示不同层次的代码块，比如函数的主体代码块，条件执行代码块，循环体代码块及类定义代码块。`Python`对缩进的大小，即空格或制表符数目个数没有限制，只有一个要求，即同一个代码块中的缩进大小必须一致：

```python
if a:  
  statement1    # 缩进一致，正确!
  statement2  
else:  
  statement3  
    statement4  #缩进不一致，错误!
```

如果块中只有很少的语句，那么你也可以把它们放置在同一行：

```python
if a: statement1
else: statement2 
```

要表示一个空的块或是空的主体，使用 `pass` 语句：

```python
if a:
    pass 
else:
    statements
```

尽管允许用制表符号指示缩进，我还是要说这是一个不好的习惯。请坚决不要混合使用制表符和空格来缩进，这会给你带来难缠的麻烦。建议你在每个缩进层次中使用`1`个制表符或`2`个或`4`个空格。运行 `Python` 程序的时候使用 `-t` 参数，如果 `Python` 发现存在制表符和空格混用，它会显示出警告信息。若改用 `-tt` 参数运行程序 `Python` 则会在发现制表符和空格混用的地方触发`TabError`异常。

`Python` 允许使用分号 `;` 把多个语句放在同一行，只有一个语句的行也可以用分号来结束。 

`#` 符号给你的程序添加注释。从 `#` 到行末的文本都是注释，只有一个例外，包在字符串引号内的 `#` 没有这个功能。 最后要说明的一点是，非交互模式下，解释器会忽略所有的空白行。同样也有一个例外，包含三引号字符串中的空行不会被忽略。

## 2.2. 标识符及保留字

标识符用于标识变量、函数、类、模块以及其他对象的名字。标识符可以包含字母、数字及下划线`_`，但必须以一个非数字字符开始。字母不仅仅包括英文字母，我们的汉字也是一种字母。不过为了国际交流，也为了自己方便，我不建议使用汉字做为标识符。标识符区分大小写，因此 `FOO` 和`foo` 是两个不同的标识符。 特殊符号，如`$`、`%`、`@`等，不能用在标识符中。另外，如 `if`，`else`，`for` 等单词是保留字，也不可以用作标识符。下表列出了所有 `Python3.7.4` 中的所有保留字：

```text
'False', 'None', 'True', 'and', 'as', 
'assert', 'async', 'await', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 
'except', 'finally', 'for', 'from', 'global', 
'if', 'import', 'in', 'is', 'lambda', 
'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield'
```

注意，随着`Python`版本升级，这个列表可能会继续增加。用下面两行代码即可方便地列出你当前使用的`Python`版本中的保留字。

```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

以下划线开始或者结束的标识符通常有特殊的意义。例如以下划线开始的标识符 `_foo` 不能用 `from module_name import *`语句导入。前后均有两个下划线的标识符， 如 `__init__`，被视为特殊方法而为`Python`保留。仅前边有两个下划线的标识符，如`__bar`，被`Python`用来实现类的私有属性，这个将在[第七章-类与面向对象编程]()中讲到。作为一个常识，我们应该避免使用容易混淆的标识符。

## 2.3. 数字/字符串

`Python` 中有四种内建的数值类型：整数、长整数、浮点数和复数。

象`1234`这样的数被解析为一个十进制的整数。要指定一个八进制或者十六进制的整数，在一个合法的八进制数前加上 `0` 或者在一个合法的`16`进制数前加上 `0x`。例如 `0644` 是一个`8`进制数，而 `0x100fea8` 则是一个`16`进制数。 在一个整数后面加上字母 `l` 或 `L`, 系统就认为这是一个长整数，如 `1234567890L`。与受机器字长限制整数类型不同，长整数可以是任何长度，只要机器的剩余内存空间放得下。象`123.34`和`1.2334e+02`这样的数被解析为浮点数。一个整数或者浮点数加上后缀`J` 或者 `j` 就构成了一个复数的虚部，你可以用一个实数加上一个虚部创建一个复数，比如 `1.2 + 12.34J`。

字符串是 `Python3` 中最常用的数据类型。在`Python3`中，所有的字符串都是`Unicode`字符串。我们已经知道可以使用单引号`'`，双引号`"`，或者三引号`'''` 或 `
"""` 来定义一个字符串。字符串前后的引号类型必须一致。反斜杠 `\` 用来转义特殊字符，比如换行符、反斜杠本身、引号以及其他不可打印的字符。`Table 2.1` 中列出了大部分特殊字符的表示方法，无法识别的转义字符串将被原样输出，包括前置的反斜线字符。此外，三引号字符串中可以包含无需转义的换行符和单引号和双引号。

邻􏱣近的紧挨着的，或者被空格或者􏰊换行符分割的字符串，例如 "hello" 'world' 会被Python自动连结为一个字符串 "helloworld"。􏰔􏰈不论是单引号字符串，双引号字符串，还是三引号字符串，都会自动连结。 例如：

```python
>>> 'h'"hllll"    """kkkkkk"""
'hhllllkkkkkk'
```

Table 2.1 标准特殊字符转义表

| 标准特殊字符 |  |
| :--- | :--- |
| 字符 | 描述 |
| \ 在行尾时 | 续行符 |
| \\\\ | 反斜杠 |
| \\' | 单引号 |
| \\" | 双引号 |
| \\a | Bell - 喇叭发出吡的一声|
| \\b | 退格符 |
| \\e | Escape |
| \\0 | Null\(空值\) |
| \\n | 换行符，等价于\x0a和\cJ |
| \\v | 垂直制表符，等价于\x0b和\cK |
| \\t | 水平制表符，等价于\x09和\cI |
| \\r | 回车符，等价于\x0d和\cM |
| \\f | 换页符，等价于\x0c和\cL |
| \\oyy | 八进制值 yy |
| \\xhh | 十六进制值 hh|
| \\other | 其他字符原样输出，包括反斜线字符 |


## 1.4. 运算符、分隔符及特殊符号

`Python3` 目前支持以下运算符:

```
+   -   *   **    //  /   %   <<  >>      &   |   ^  
+=  -=  *=  **=   //= /=  %=  <<= >>=     &=  |=  ^=
~   <   >   <=    >=  ==  !=  is  is not
```

下边这些符号可以作为表达式，列表，字典，以及语句不同部分的分隔符号:

```
( ) [ ] { } , : . ` = ;
```

比如，赋值符号 `=`，是标识符与分配给它的值之间的分隔符；逗号 `,` 是用来分隔函数参数、列表或`tuple`中元素的分隔符；小数点 `.` 是浮点数中整数部分与小数部分的分隔符，同时它还可以组成扩展切片运算中的省略符`...`。

下边这些特殊符号也在语句中使用：

```
' " # @
```

其中 `' "`是字符串的起始结束符号，`#` 是注释的开始符号，`@` 是函数修饰符号。

字符 `$`、`?` 不能作为程序语义的一部分出现，但是可以出现在字符串中。 

## 1.5. 文档字符串

如果一个模块、类、或函数体的第一个语句是一个未命名字符串，该字符串就自动成为该对象的文档字符串 `DocStrings`，例如：

```python
def fact(n):
    "This function computes a factorial"
    if (n <= 1): return 1
    else: return n*fact(n-1)
```

一些辅助浏览代码以及文档生成的工具包经常会用到文档字符串。通过访问对象的 `__doc__` 属 性，你可以得到它的文档字符串：

```python
 >>> print(fact.__doc__)
 This function computes a factorial
 >>>
```

你可能不相信，这个 __doc__ 属性也是可写的。你可以修改它的值。

文档字符串的缩进必须与定义中的其他语句一致。此外，在不同行出现的多个未命名字符串不会自动连结成一个字符串，即使他们紧挨着。

**注意**：文档字符串仅仅是第一个未命名字符串，这与前边讲到的字符串的自动连结有所不同。
