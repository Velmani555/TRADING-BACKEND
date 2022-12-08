import datetime
from dbconnection import DBConnection


class SectorListInsertDAO:
    def insert_sector_list_DAO(self, sector_id, sector_name, symbol_id, symbol_code, created_date, updated_date, created_by, updated_by, sector_status):
        dbconnection = DBConnection()
        connection = dbconnection.getconnection()
        cursor = connection.cursor()
        cursor.execute(
            '''insert into sector_list (sector_id,sector_name,symbol_id,symbol_code,created_date,updated_date,created_by,updated_by,sector_status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);''', (sector_id, sector_name, symbol_id, symbol_code, created_date, updated_date, created_by, updated_by, sector_status))
        connection.commit()
        connection.close()


sector_id = 10
sector_name = "bank"
symbol_id = 2
symbol_code = "SBIN"
created_date = "2022-06-12"
updated_date = "2022-06-12"
created_by = 1
updated_by = 2
sector_status = 1

sectorlistinsertDAO = SectorListInsertDAO()
sectorlistinsertDAO.insert_sector_list_DAO(
    sector_id, sector_name, symbol_id, symbol_code, created_date, updated_date, created_by, updated_by, sector_status)
