# 1.导入库
import pymysql


# 2.建立连接
def get_coon():
    """lansi_fdh数据库连接"""
    conn = pymysql.connect(host='rm-uf6o289177ht773wc5m.mysql.rds.aliyuncs.com',
                           user='mysqlsa',
                           password='Lansi123',
                           database='lansi_fdh',
                           charset="utf8mb4")
    return conn
