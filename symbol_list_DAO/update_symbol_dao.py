import datetime
from dbconnection import DBConnection


class SymbolUpdateDAO:
    def update_symbolDAO(self):
        dbconnection = DBConnection()
        connection = dbconnection.getconnection()
        cursor = connection.cursor()
        cursor.execute(
            '''update symbol_list set symbol_id=5 where symbol_id=8;''')
        connection.commit()
        connection.close()


symbolDAO = SymbolUpdateDAO()
symbolDAO.update_symbolDAO()
