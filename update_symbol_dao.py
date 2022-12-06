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
symbol_name = "SBINN"
symbol_code = "SBBBB"
sector_name = "bank"
sector_code = 10
created_date = "2021-06-12"
updated_date = "2022-07-12"
created_by = 101
updated_by = 101
symbol_status = 1

symbolDAO = SymbolDAO()
symbolDAO.insert_symbolDAO(symbol_id, symbol_name, symbol_code, sector_name,
                           sector_code, created_date, updated_date, created_by, updated_by, symbol_status)
