"""
练习: 字典操作

描述：
实现对学生成绩字典的添加、删除、修改和查询操作。

请补全下面的函数，对学生成绩字典进行各种操作。
"""

def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作

    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数

    返回:
    - 根据操作返回不同结果
    """
    # # 请在下方编写代码
    # if operation == "add":
    #     if len(args) != 2:
    #         return "添加俩参数"
    #     name,score = args
    #     if name in students_dict:
    #         return f"学生{name}已存在，无法添加"
    #     students_dict[name] = score
    # elif operation == "remove":
    #     name = args[0]
    #     if name in students_dict:
    #         del students_dict[name]
    # if operation == "update":
    #     if len(args) != 2:
    #         return "更新操作需要传入两个参数：姓名和成绩"
    #     name, score = args
    #     if name not in students_dict:
    #         return f"学生{name}不存在，无法更新"
    #     if not isinstance(score, (int, float)):
    #         return "成绩必须是整数或浮点数"
    #     students_dict[name] = score
    #     return f"成功更新学生{name}的成绩为{score}"
    #     # 处理查询操作：args需要是(姓名)
    # elif operation == "get":
    #     if len(args) != 1:
    #         return "查询操作需要传入一个参数：姓名"
    #     name = args[0]
    #     # 使用字典的get方法，不存在则返回提示
    #     return students_dict.get(name, f"学生{name}不存在")