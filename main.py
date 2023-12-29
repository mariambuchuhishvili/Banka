import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel

from ui_main_window import Ui_MainWindow
from ui_new_write_window import Ui_Dialog
from ui_change_target import Ui_Dialog_Target
from connection import Data

#открывает главную страницу
class InvestmentTracker(QMainWindow):
    def __init__(self):
        super(InvestmentTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()
        self.reload_data()

        self.ui.addButton.clicked.connect(self.open_new_write_window)
        self.ui.editButton.clicked.connect(self.open_new_write_window)
        self.ui.deleteButton.clicked.connect(self.delete_current_write)
        self.ui.targetButton.clicked.connect(self.open_change_target_window)


# открывает окошечко добаления новой записи
    def open_new_write_window(self):
        self.new_write_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_write_window)
        self.new_write_window.show()
        sender = self.sender()
        if sender.objectName() == "addButton":
            self.ui_window.saveButton.clicked.connect(self.add_new_write)
        else:
            self.ui_window.saveButton.clicked.connect(self.edit_current_write)
# открывает окошечко изменения цели
    def open_change_target_window(self):
        self.change_target_window = QtWidgets.QDialog()
        self.ui_target_window = Ui_Dialog_Target()
        self.ui_target_window.setupUi(self.change_target_window)
        self.change_target_window.show()

        self.ui_target_window.saveTargetButton.clicked.connect(self.change_target)

    def add_new_write(self):
        date = self.ui_window.dateEdit.text()
        balance = self.ui_window.inputLineEdit.text()

        self.conn.add_new_investment_query(date, balance)
        self.view_data()
        self.reload_data()
        self.new_write_window.close()

    def edit_current_write(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        date = self.ui_window.dateEdit.text()
        balance = self.ui_window.inputLineEdit.text()

        self.conn.update_investment_query(date, balance, id)
        self.view_data()
        self.reload_data()
        self.new_write_window.close()

    def check_delete_write(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Хотите удалить эту запись?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.No)
        return msgBox.exec()

    def delete_current_write(self, sender):
        btn_clicked = self.check_delete_write()

        if btn_clicked == QtWidgets.QMessageBox.Yes:
            index = self.ui.tableView.selectedIndexes()[0]
            id = str(self.ui.tableView.model().data(index))
            self.conn.delete_investment_query(id)
            self.view_data()
            self.reload_data()

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('investments')
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def reload_data(self):

        current = self.conn.total_balance()
        if current!='':
            self.ui.current.setText(current)
            self.ui.progressBar.setValue(int(current)*100/int(self.ui.target.text()))
        else:
            current = 0
            self.ui.current.setText(str(current))
            self.ui.progressBar.setValue(int(current) * 100 / int(self.ui.target.text()))

    def change_target(self):
        newTarget = self.ui_target_window.inputTargetEdit.text()
        self.conn.update_target_query(newTarget)
        self.ui.target.setText(str(self.check_target()))
        self.view_data()
        self.reload_data()
        self.change_target_window.close()

    def check_target(self):
        target = self.conn.get_last_target_query()
        if target != None:
            return target
        else:
            return 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InvestmentTracker()
    window.show()
    sys.exit(app.exec())
