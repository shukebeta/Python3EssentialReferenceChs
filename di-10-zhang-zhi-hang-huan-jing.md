# 第10章 执行环境

本章的主题是Python程序的运行环境，目标是阐述解释器的运行时行为：包括程序启动、站点配置及程序终止。

### 解释器选项及运行环境

解释器有许多选项控制它的运行时行为和及运行环境。在UNIX和Windows下,选项以命令行选项的形式传递给解释器:

```
python [option] ... [-c cmd | -m mod | file | -] [arg] ...
```

在Macintosh下,需要使用一个独立程序EditPythonPrefs来修改Python解释器的执行参数。

当前版本共支持以下命令行选项(Python2.4):

```
选项                              描述
-d 或 PYTHONDEBUG=x             生成解析器调试信息
-h                              打印帮助信息，然后退出
-i 或 PYTHONINSPECT=x           程序运行后进入交互模式(程序中的对象会继续存在)
-O 或 PYTHONOPTIMIZE=x          优化生成的字节码
-OO                             在-O的基础之上删除文档字符串
-S                              阻止包含 site 定义的模块
-t                              若发现制表符空格混合缩进给出警告信息
-tt                             若发现制表符空格混合缩进引发 TabError 异常
-u 或 PYTHONUNBUFFERED=x        非缓冲二进制标准输出及标准错误
-U                              Unicode模式,所有字符都被转换为Unicode
-v 或 PYTHONVERBOSE=x           冗余模式(跟踪 import 语句).
-V                              显示版本信息后退出
-x                              忽略程序的第一行
-c cmd                          运行字符串 cmd 
-W arg                          警告控制(arg是行为:message:category:module:lineno)
-E                              忽略环境变量(such as PYTHONPATH)
-m mod                          mod: 模块名 将模块象脚本一样运行
-Q arg                          division options: -Qold (default), -Qwarn, -Qwarnall, -Qnew
file                            脚本文件
-                               从标准输入读取程序代码 (这是默认参数)
arg ...                         脚本参数(保存在 sys.argv[1:])
```

选项 -d 用来调试解释器,普通程序员几乎不会用到这个选项(Python开发团队用的会比较多)

选项 -i 会在程序结束的时候进入交互模式,通常用于调试用户代码。

选项-O 和 -OO 使用最佳化模式,产生较优化的字节码(在第八章中有介绍).

选项 -S 忽略site 初始化模块(参见后边的 "Site 配置文件" 小节).

选项 -t ,-tt,和-v会产生额外的警告和调试信息

选项 -x 会忽略程序的第一行(例如,当第一行是启动Python解释器的脚本时).

选项 -U 强迫解释器将所有字符转化为Unicode.选项 -W 用于过滤警告信息(参阅附录A).

脚本名字在所有选项后出现。如果未提供文件名，或者提供了一个连字号(`-`)作为文件名，解释器就从标准输入读入程序。如果标准输入是一个交互的终端,一个信息条和提示符就会出现.否则解释器就打开指定文件并运行它直到文件结束.

选项 -c cmd 用于以命令行选项的形式运行一个小脚本cmd。

在程序名或hyphen()后的命令行参数会被传递给程序中的sys.argv (第九章中的 "读取参数和环境变量" 中介绍)

此外,解释器还读取以下的环境变量:

```
变量                              描述
PYTHONPATH              冒号分隔的模块搜索路径
PYTHONSTARTUP           交互模式启动时自动运行的脚本
PYTHONHOME              Python的安装位置
PYTHONINSPECT           表示 -i 选项
PYTHONUNBUFFERED        表示 -u 选项
PYTHONCASEOK            import 语句 模块名大小写不敏感 (windows)
```

PYTHONPATH指定一系列模块搜索路径,它将被插入到sys.path列表的前面。PYTHONSTARTUP指定一个脚本文件，当解释器交互方式启动时该脚本会自动运行.PYTHONHOME变量用于配置Python的安装位置,因为Python自己可以找到它的库以及包的地址,所以这个变量极少用到。如果这个变量包括一个目录,如/usr/local,则解释器就试图在这个目录查找所有文件。如果包括两个目录,例如/usr/local:/usr/local/sparc-solaris-2.6 ,解释器会在第一个目录中查找跨平台的文件,在第二个目录查找依赖平台的文件。 若指定目录没有有效的Python安装，则PYTHONHOME环境变量将被忽略。

在Windows下,有些环境变量，比如PYTHONPATH等等,是从注册表的HKEY\_LOCAL\_MACHINE/Software/Python 中读入的。在Macintosh下, 使用EditPythonPrefs程序可以改变这些环境变量。

### 交互模式

在命令行下运行Python而不提供执行脚本,就自动进入Python的交互模式。Python会首先显示版本信息,如果PYTHONSTARTUP环境变量设置了有效的脚本，Python就会运行这个脚本，最后显示交互提示符 >>>。这个脚本会被当成用户输入程序的一部分被执行。(也就是说，它并不是以import语句导入的方式被执行的)该脚本的一个典型应用就是读取用户的配置文件(比如.pythonrc)。

当接受一个交互输入时,会有两种用户提示。 >>>提示符你输入新的语句, ...提示输入你正处于一个缩进块。例如:

```
Python 2.4.2 (#67, Sep 28 2005, 12:41:11) [MSC v.1310 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(0,4):
...     print i
...
0
1
2
3
>>>
```

如果需要，修改sys.ps1和sys.ps2这两个变量你就可以自定义这两个提示。

某些系统里, Python可能被编译为使用GNU readline库。如果该特性启用的话,该库就会提供命令历史,自动完成等其它特性。特殊关键字绑定由readline库提供(参见附录A readline模块)。

默认情况下,如果你在交互模式输入一个表达式，则解释器会调用 print repr(你的表达式)来生成输出结果。从Python 2.1开始，你可以通过设置变量sys.displayhook来改变表达式的输出格式。例如:

```
>>> def my_display(x):
...     print "result = %s" % repr(x)
...
>>> sys.displayhook = my_display
>>> 3+4
result = 7
>>>
```

### 运行Python程序

在多数情况下,你希望程序能自动启动解释器,而不是每次手动启动解释器。在UNIX下,你可以在程序的第一行使用魔术字符串告诉系统由哪个解释器来运行这个脚本:

```
#!/usr/local/bin/python
# Python code from this point on...
import string
print "Hello world"
...
```

在Windows 下,双击一个.py, .pyw, .wpy, .pyc 或者.pyo文件都会自动运行解释器。除 .pyw 后缀文件外(静默运行),其他的文件都会在一个控制台窗口中运行。如果必须给解释器提供启动选项, Python程序也可以由.bat文件启动运行。

在Macintosh 下,点击一个.py文件通常会打开创建该脚本的编辑器。不过Macintosh发行版有两个特殊的程序用来创建应用程序。将一个 .py 拖到 BuildApplet 程序就会将该脚本转换为一个应用程序(打开该文件即自动调用解释器)。 BuildApplication 程序则可以转换一个 Python 脚本成为一个独立运行的应用程序(不需要Python解释器就可以运行的应用程序)。

### Site配置文件

一个典型的Python安装可能会包括很多第三方模块和包，要配置这些包, 解释器首先导入site模块. site模块的任务就是搜索包文件,必要时向sys.path添加搜索目录。另外, site模块也设置Unicode字符串转换的默认编码。更多细节参阅附录A -- site模块.

### 启用 Future 特性

从Python 2.1开始，当一个新的语言特性首次出现在发行版中时，如果该特性与旧版Python不兼容，则该特性将被默认禁用。要启用这些特性，使用语句`from __future__ import *` 。举例来说：

```
# Enable nested scopes in Python 2.1
from __future__ import nested_scopes
```

如果使用这个语句，则该语句必须是模块或程序的第一个语句。此外，`__ future__` 模块中存在的特性最终将成为Python语言标准的一部分。到那时，将不再需要使用`__future__`模块。

### 程序终止

当一个程序正常运行到最后一条语句,或者出现一个未捕获的SystemExit异常(由sys.exit()产生)，或者解释器收到一个SIGTERM或者SIGHUP(在 UNIX下)信号时,程序就会终止。解释器会将所有已知名称空间下的所有对象对象的引用记数清为0(并同时删除所有的名称空间)。当一个对象的引用记数变为零,就会自动调用它的`__del__()`来销毁该对象。_注意_ 当两个对象存在互相引用时，在程序结束时，这两个对象就无法被销毁(这会造成内存泄漏)。尽管Python的垃圾回收机制能在运行时删除这些对象,在程序结束时该机制不会被自动调用。

由于不能保证对象的`__del__()`方法在程序结束时一定会执行,一个比较好的办法就是在程序结束时显式的清除某些对象。例如打开的文件以及网络连接等。你可以给一个自定义对象写一个专门的销毁方法(例如close())，也可以写一个终止函数,并通过 atexit 模块将其注册到系统中:

```
import atexit
connection = open_connection("deaddot.com")

def cleanup():
    print "Going away..."
    close_connection(connection)

atexit.register(cleanup)
```

也可以以这种方式来调用垃圾回收器:

```
import atexit, gc
atexit.register(gc.collect)
```

当程序结束时，有些对象的 `__del__` 方法会访问全局数据或者其他模块中的方法定义。由于这些对象可能已经被删除, `__del__`方法就有可能引发NameError异常。你有可能见到类似下边这样的出错信息:

```
Exception exceptions.NameError: 'c' in <method Bar.__ del__ of Bar instance at c0310>
...
```

如果看到这个信息,说明某个对象的 `__del__`方法执行失败，这通常意味着有一项重要操作没有完成(例如关闭一个服务器连接)。最好在代码中显式的执行清理操作,而不是依赖解释器来自动做这件事。通过在 `__del__()`定义时使用默认参数能够避免这个罕见的 NameError 异常,例如:

```
import foo
class Bar:
   def __ del__ (self, foo=foo):
      foo.bar()        # 在模块foo中使用某些东西
```

有时（罕见）必须立刻终止程序,不需要做任何清理操作。这时调用 os.\_exit(status)即可。这个函数提供一个低层次exit()系统调用接口,当调用它时,程序会立即停止。
