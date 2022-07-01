import re
some_text = 'a,b,,,,c d'
pattern = re.compile('[, ]+')  # 根据正则表达式创建模式对象，每次使用不需要转换
# obj = re.split('[, ]+', some_text)
re_str = pattern.split(some_text)  # =re.split(): 根据指定字符切割原串
print(re_str)

