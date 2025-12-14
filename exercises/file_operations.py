"""
练习: 文件处理

描述：
本练习帮助您学习如何在Python中进行文件的读取和写入操作。

请补全下面的函数，实现文件的读取和写入功能。
"""
"""
读取文本文件内容

参数:
- file_path: 文件路径

返回:
- 文件内容字符串
"""
# 请在下方编写代码
# 使用open()函数打开文件并读取内容
def read_file(file_path):
    file = open(file_path, 'r', encoding='utf-8')# 打开文件，返回文件对象
    ans = file.read()
    file.close()
    return ans
def write_file(file_path, content):
    file = open(file_path, 'w', encoding='utf-8')
    ans = file.write(content)
    file.close()
    return True
    """
    写入内容到文本文件

    参数:
    - file_path: 文件路径
    - content: 要写入的内容

    返回:
    - 是否写入成功的布尔值
    """
    # 请在下方编写代码
    # 使用with语句和open()函数写入内容到文件