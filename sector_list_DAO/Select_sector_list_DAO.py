import datetime
from dbconnection import DBConnection


class SectorListSelectDAO:
    def select_sector_list_DAO(self):
        print('select Sector_list operation')
        dbconnection = DBConnection()
        connection = dbconnection.getconnection()
        print('Sector_list_DAO')
        cursor = connection.cursor()
        statement = '''select * from sector_list;'''
        cursor.execute(statement)
        minutelist = cursor.fetchall()
        for r in minutelist:
            print(r)
        connection.commit()
        connection.close()


sectorlistselectDAO = SectorListSelectDAO()
sectorlistselectDAO.select_sector_list_DAO()
