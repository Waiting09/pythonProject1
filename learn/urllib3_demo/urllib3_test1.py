import json

import urllib3

from urllib.parse import urlencode


# �﷨��request(method, url, fields, headers, **)
# ����:
#   method������ʽ
#   url�������ַ
# ѡ��:
#   headers������ͷ��Ϣ
#   fields������������
#   body��ָ������������
#   tiemout�����ó�ʱʱ��


def test_HTTP():
    # �������ӳض���Ĭ�ϻ�У��֤��
    pm = urllib3.PoolManager()
    # ����HTTP����
    resp = pm.request(method='get', url="http://httpbin.org/get")
    # print(type(resp))  # <class 'urllib3.response.HTTPResponse'>

    # print(resp.status)  # �鿴��Ӧ״̬״̬��
    # print(resp.headers)  # �鿴��Ӧͷ��Ϣ
    print(resp.data)  # �鿴��Ӧԭʼ��������Ϣ
    #  ��ȡ��������ʽ����Ӧ����
    raw = resp.data
    # print(type(raw), raw)  # <class 'bytes'>
    # �����ַ���
    content = raw.decode("utf-8")
    # print(type(content),content)  # <class 'str'>
    # json �������ֵ����
    obj = json.loads(content)
    # print(type(obj), obj)  # <class 'dict'>


def test_headers():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/get"

    # ��������ͷ
    headers = {'school': 'hogwarts'}
    # ���Ʋ�ѯ�ַ�������
    fields = {'type': 1}
    # ��������
    resp = pm.request('GET', url, headers=headers, fields=fields)
    # �鿴��Ӧ��Ϣ
    content = json.loads(resp.data.decode("utf-8"))
    print(content)


def test_post():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/post"

    # post�������
    encode_str = urlencode({'type': 1})

    # ƴ�ӵ�url�У���������
    resp = pm.request('POST', url=f'{url}?{encode_str}')
    # �鿴��Ӧ��Ϣ
    content = json.loads(resp.data.decode("utf-8"))
    print(content)
