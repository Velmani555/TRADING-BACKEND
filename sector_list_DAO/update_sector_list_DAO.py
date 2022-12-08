import datetime
from dbconnection import DBConnection


class SectorListUpdateDAO:
    def update_sector_list_DAO(self):
        dbconnection = DBConnection()
        connection = dbconnection.getconnection()
        cursor = connection.cursor()
        cursor.execute(
            '''update sector_list set sector_id=1011 where sector_id=10;''')
        connection.commit()
        connection.close()


sectorlistupdateDAO = SectorListUpdateDAO()
sectorlistupdateDAO.update_sector_list_DAO()
