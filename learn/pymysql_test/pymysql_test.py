# coding:utf-8
from conn_demo import get_coon

"""
def test1():
    # 1、打开连接
    conn = get_coon()
    # 2、获取游标
    cursor = conn.cursor()
    # 3、执行sql
    sql = "SELECT VERSION();"
    cursor.execute(sql)
    # conn.commit() 插入时需要提交
    # 4、获取结果
    version = cursor.fetchone()
    print(version)
    # 5、关闭连接
    conn.close()
"""


def test2():
    conn = get_coon()
    cursor = conn.cursor()
    sql = "SELECT * FROM u_wx_smallaccount WHERE mobile = 13761401357;"
    try:
        cursor.execute(sql)
        record = cursor.fetchone()  # 查询记录
        # fetchone()：获取单条记录
        # fetchmany(n)：获取 n 条记录
        # fetchall()：获取所有结果记录
        print(record)
    except:
        conn.rollback()
        print("Fail")
    finally:
        conn.close()
