import json

import urllib3

from urllib.parse import urlencode


# 语法：request(method, url, fields, headers, **)
# 必填:
#   method：请求方式
#   url：请求地址
# 选填:
#   headers：请求头信息
#   fields：请求体数据
#   body：指定请求体类型
#   tiemout：设置超时时间


def test_HTTP():
    # 创建连接池对象，默认会校验证书
    pm = urllib3.PoolManager()
    # 发送HTTP请求
    resp = pm.request(method='get', url="http://httpbin.org/get")
    # print(type(resp))  # <class 'urllib3.response.HTTPResponse'>

    # print(resp.status)  # 查看响应状态状态码
    # print(resp.headers)  # 查看响应头信息
    print(resp.data)  # 查看响应原始二进制信息
    #  获取二进制形式的响应内容
    raw = resp.data
    # print(type(raw), raw)  # <class 'bytes'>
    # 解码字符串
    content = raw.decode("utf-8")
    # print(type(content),content)  # <class 'str'>
    # json 解析成字典对象
    obj = json.loads(content)
    # print(type(obj), obj)  # <class 'dict'>


def test_headers():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/get"

    # 定制请求头
    headers = {'school': 'hogwarts'}
    # 定制查询字符串参数
    fields = {'type': 1}
    # 发送请求
    resp = pm.request('GET', url, headers=headers, fields=fields)
    # 查看响应信息
    content = json.loads(resp.data.decode("utf-8"))
    print(content)


def test_post():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/post"

    # post请求参数
    encode_str = urlencode({'type': 1})

    # 拼接到url中，发送请求
    resp = pm.request('POST', url=f'{url}?{encode_str}')
    # 查看响应信息
    content = json.loads(resp.data.decode("utf-8"))
    print(content)
