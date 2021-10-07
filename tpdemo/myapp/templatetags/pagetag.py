from django import template
# from django.utils.html import format_html

register = template.Library()


# 自定义过滤器（实现大写转换）
@register.filter
def myupper(val):
    # print ('val from template:',val)
    return val.upper()


# 自定义标签（实现减法计算）
@register.simple_tag
def jian(a, b):
    res = int(a) - int(b)
    return res