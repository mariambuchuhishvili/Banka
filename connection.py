from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('investments_db.db')
        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Не получилось открыть базу данных.",
                                           "Нажмите Cancel чтобы закрыть окно.", QtWidgets.QMessageBox.Cancel)
            return False
        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS investments (ID integer primary key AUTOINCREMENT, Date VARCHAR(20), "
                   "Balance integer)")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)
        query.exec()
        return query

    def add_new_investment_query(self, date, balance):
        sql_query = "INSERT INTO investments (Date,Balance) VALUES (?, ?)"
        self.execute_query_with_params(sql_query, [date, balance])

    def update_investment_query(self, date, balance, id):
        sql_query = "UPDATE investments SET Date=?, Balance=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [date, balance, id])

    def delete_investment_query(self, id):
        sql_query = "DELETE FROM investments WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, filter=None, value=None):
        sql_query = f"SELECT SUM({column}) FROM investments"
        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"
        query_values = []
        if value is not None:
            query_values.append(value)
        query = self.execute_query_with_params(sql_query, query_values)
        if query.next():
            return str(query.value(0))
        return '0'

    def total_balance(self):
        return self.get_total(column="Balance")
