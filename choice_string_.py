import random
import string

ALL_CHARS = string.digits + string.ascii_letters  # digits: 0-9  ascii_letters: a-z, A-Z
# print(ALL_CHARS)

def generate_code(code_len=4):
    """生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    # random.choices(seq): 从序列中随机抽样
    return ''.join(random.choices(ALL_CHARS, k=code_len))
"""
join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
random.choices(population,weights=None,*,
cum_weights=None,k=1)
Python3.6版本新增。
population：集群。
weights：相对权重。
cum_weights：累加权重。
k：选取次数。
"""

for _ in range(10):
    print(generate_code())
