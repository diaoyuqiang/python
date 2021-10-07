import urllib.request as request
from lxml import etree

# xpath抓取静态页面
res = request.urlopen("https://www.sojson.com/json/json_index.html")  # 打开url地址

html_content = str(res.read(), encoding="utf-8")  # 获取页面内容（将字节码转换成字符串)

# 根据字符串获取html树
tree = etree.HTML(html_content)
# print(tree)

result = tree.xpath('//*[starts-with(@class, "site-tree-noicon")]/a')  # //:匹配所有 获取页面上calss=site-tree-noicon属性的节点信息

for item in result:  # 遍历a节点
    try:
        text = item.xpath("./cite/text()")[0]  # 抓取a节点下cite节点的文本内容
        print(text)
        text2 = item.xpath("./em/text()")   # 抓取a节点下em节点的文本内容
        if text2:
            print(text2[0])

    except Exception as e:  # 异常处理
        print("html页面抓取异常，异常信息为：", e)