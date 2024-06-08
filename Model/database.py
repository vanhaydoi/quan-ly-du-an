import mysql.connector

class MySQLConnector:
    def __init__(self, host, port,username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port = self.port,
                user=self.username,
                password=self.password,
                database=self.database
            )
            print("Kết nối thành công")
        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def execute_query(self, query):
        if not self.connection:
            print("Lỗi: Không kết nối được với cơ sở dữ liệu MySQL.")
            return None
        
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            if cursor.with_rows:  # Kiểm tra nếu có kết quả trả về
                result = cursor.fetchall()
                return result
        except mysql.connector.Error as err:
            print(f"Lỗi thực hiện truy vấn: {err}")
            return None
        finally:
            cursor.close()

        self.connection.commit() # Đảm bảo dữ liệu được lưu
        print("Query được thực hiện thành công.")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Đã đóng kết nối với cơ sở dữ liệu MySQL.")


#Kết nối tới mysql của bản thân
# connector = MySQLConnector(host='localhost', port=3306,username='root', password='123456', database='qlnv')
# connector.connect()



    