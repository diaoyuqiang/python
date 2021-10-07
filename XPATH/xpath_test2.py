import urllib.request as request
from lxml import etree

# xpath抓取静态页面
res = request.urlopen("https://www.ctrip.com/")  # 打开url地址

html_content = str(res.read(), encoding="utf-8")  # 获取html页面内容（将字节码转换成字符串)
# print(html_content)

# 根据字符串获取html树
tree = etree.HTML(html_content)

result = tree.xpath('//*[@class="inner-tab-scroll-list"]/div')  # //:匹配所有 获取页面上calss=site-tree-noicon属性的节点信息
for i in result:
    text = i.xpath('./a/div[@class="item-msg"]/p/text()')[0]
    print(text)

# with open("xc.html", "w", encoding="utf-8") as f:
#     f.write(html_content)