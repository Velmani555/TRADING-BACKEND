import datetime
from dbconnection import DBConnection


class SectorListDeleteDAO:
    def delete_sector_list_DAO(self):
        dbconnection = DBConnection()
        connection = dbconnection.getconnection()
        cursor = connection.cursor()
        cursor.execute(
            '''delete from sector_list where sector_id=1;''')
        connection.commit()
        connection.close()


sectorlistdeleteDAO = SectorListDeleteDAO()
sectorlistdeleteDAO.delete_sector_list_DAO()
