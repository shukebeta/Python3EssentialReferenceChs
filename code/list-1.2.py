import sys                # 导入 sys 模块
print(sys.argv);sys.exit();
f = open(sys.argv[1])     # 从命令行读取文件名
svalues = f.readlines()   # 读出所有行到一个列表
f.close()  

# 把列表中所有值转换为浮点数  
fvalues = [float(s) for s in svalues]  

# 输出最大值和最小值
print("The minimum value is ", min(fvalues))
print("The maximum value is ", max(fvalues))
