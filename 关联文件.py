# 创建课程老师的字典
course_teacher_map = {}

with open("conn01", encoding='utf-8') as fin:
    for line in fin:  # 遍历文件内容
        line = line.strip()   # 去除前后空白符
        course, teacher = line.split(',')  # 用,分割每行数据，并用相应数量的变量接收
        course_teacher_map[course] = teacher  # 添加到字典的key,values中


with open("conn02", encoding='utf-8') as fio:
    for line in fio:
        line = line.strip()
        course, grade, name, score = line.split(',')
        teacher = course_teacher_map.get(course)
        print(course, teacher, grade, name, score)
