import datetime
from dbconnection import DBConnection


class TimeStampListUpdateDAO:
    def update_time_stamp_list_DAO(self):
        dbconnection = DBConnection()
        connection = dbconnection.getconnection()
        cursor = connection.cursor()
        cursor.execute(
            '''update time_stamp_list set time_stamp="09:15" where time_id=3;''')
        connection.commit()
        connection.close()


timestamplistDAO = TimeStampListUpdateDAO()
timestamplistDAO.update_time_stamp_list_DAO()
