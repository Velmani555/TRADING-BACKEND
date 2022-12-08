import datetime
from dbconnection import DBConnection


class SymbolSelectDAO:
    def select_Symbol_DAO(self):
        print('select operation')
        dbconnection = DBConnection()
        connection = dbconnection.getconnection()
        print('Symbol_list')
        cursor = connection.cursor()
        statement = '''select * from symbol_list;'''
        cursor.execute(statement)
        minutelist = cursor.fetchall()
        for r in minutelist:
            print(r)
        connection.commit()
        connection.close()


symbolselectDAO = SymbolSelectDAO()
symbolselectDAO.select_Symbol_DAO()
