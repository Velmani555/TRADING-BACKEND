import datetime
from dbconnection import DBConnection


class TimeStampListDAO:
    def insert_time_stamp_list_DAO(self, time_id, time_stamp, currentref_date, created_date, updated_date, created_by, updated_by, time_id_status):
        dbconnection = DBConnection()
        connection = dbconnection.getconnection()
        cursor = connection.cursor()
        cursor.execute(
            '''insert into time_stamp_list (time_id,time_stamp,currentref_date,created_date,updated_date,created_by,updated_by,time_id_status) values(%s,%s,%s,%s,%s,%s,%s,%s);''', (time_id, time_stamp, currentref_date, created_date, updated_date, created_by, updated_by, time_id_status))
        connection.commit()
        connection.close()


time_id = 3
time_stamp = "09:16:00"
currentref_date = "2022-06-12"
created_date = "2022-06-12"
updated_date = "2022-06-12"
created_by = 1
updated_by = 2
time_id_status = 1

timestamplisttDAO = TimeStampListDAO()
timestamplisttDAO.insert_time_stamp_list_DAO(
    time_id, time_stamp, currentref_date, created_date, updated_date, created_by, updated_by, time_id_status)
