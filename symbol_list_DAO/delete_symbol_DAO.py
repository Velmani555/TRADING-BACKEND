import datetime
from dbconnection import DBConnection


class SymbolDeleteDAO:
    def delete_symbolDAO(self):
        dbconnection = DBConnection()
        connection = dbconnection.getconnection()
        cursor = connection.cursor()
        cursor.execute(
            '''delete from symbol_list where symbol_id=111;''')
        connection.commit()
        connection.close()


symboldeleteDAO = SymbolDeleteDAO()
symboldeleteDAO.delete_symbolDAO()
