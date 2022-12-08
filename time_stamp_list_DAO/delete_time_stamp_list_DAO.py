import datetime
from dbconnection import DBConnection


class TimeStampListDeleteDAO:
    def delete_time_stamp_list_DAO(self):
        dbconnection = DBConnection()
        connection = dbconnection.getconnection()
        cursor = connection.cursor()
        cursor.execute(
            '''delete from time_stamp_list where time_id=2;''')
        connection.commit()
        connection.close()


timestamplistdeleteDAO = TimeStampListDeleteDAO()
timestamplistdeleteDAO.delete_time_stamp_list_DAO()
