import datetime
from dbconnection import DBConnection


class SymbolSelectDAO:
    def select_Symbol_DAO(self):
        print('select operation')
        dbconnection = DBConnection()
        connection = dbconnection.getconnection()
        print('time_stamp_list_DAO')
        cursor = connection.cursor()
        statement = '''select * from time_stamp_list;'''
        cursor.execute(statement)
        minutelist = cursor.fetchall()
        for r in minutelist:
            print(r)
        connection.commit()
        connection.close()


symbolselectDAO = SymbolSelectDAO()
symbolselectDAO.select_Symbol_DAO()
