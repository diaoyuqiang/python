import requests
import re
import json
import pprint  # 格式化输出


def get_response(url_vdo):
    headers = {
        'refer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4506.400'
    }
    result = requests.get(url=url_vdo, headers=headers)
    return result


def get_info(url_vdo):
    result = requests.get(url=url_vdo)
    da = re.findall('<script>window.__playinfo__=(.*?)</script>', result.text)[0]
    json_da = json.loads(da)
    pprint.pprint(json_da)


url = 'https://www.bilibili.com/bangumi/play/ep424179'

get_info(url)