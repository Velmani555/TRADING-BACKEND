import datetime
from dbconnection import DBConnection


class SymbolDAO:
    def insert_symbolDAO(self, symbol_id, symbol_code, symbol_name, sector_name, sector_code, created_date, updated_date, created_by, updated_by, symbol_status):
        dbconnection = DBConnection()
        connection = dbconnection.getconnection()
        cursor = connection.cursor()
        cursor.execute(
            '''insert into symbol_list (symbol_id, symbol_code, symbol_name, sector_name,sector_code,created_date,updated_date,created_by,updated_by,symbol_status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''', (symbol_id, symbol_code, symbol_name, sector_name, sector_code, created_date, updated_date, created_by, updated_by, symbol_status))
        connection.commit()
        connection.close()


symbol_id = 4


symbolDAO = SymbolDAO()
symbolDAO.insert_symbolDAO(symbol_id, symbol_name, symbol_code, sector_name,
                           sector_code, created_date, updated_date, created_by, updated_by, symbol_status)
