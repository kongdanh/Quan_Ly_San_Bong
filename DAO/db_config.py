#lấy connection -> trả về lỗi nếu không truy cập được vào database
#import db_config vào tất cả các file tại thư mục dao -> lấy dữ liệu tại từng bảng

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="footballrenting"
    )