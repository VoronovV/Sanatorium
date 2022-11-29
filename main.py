from GUI import *
from database import *
import sys

class Start(QtWidgets.QMainWindow):
    def __init__(self):
        self.con = db_connection()
        create_db(self.con)
        super(Start, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_page) #устанавливает главную страницу
        self.init_UI()

    def init_UI(self):
        self.ui.entry_btn.clicked.connect(self.on_click_entry_but)
        self.ui.regisration_btn.clicked.connect(self.on_click_registration_but)

    def on_click_entry_but(self):
        self.ui.main_page.hide()
        self.ui.entry_page.show()
        self.ui.entry_btn_entry_page.clicked.connect(self.input_data_entry)
        self.ui.back_btn_entry.clicked.connect(self.back_in_main_page)

    def input_data_entry(self):
        login = self.ui.entry_login_edit.text()  # сверить с бд
        password = self.ui.entry_pass_edit.text()
        if login_in_users_table(self.con, login, password) == True:
            self.ui.entry_page.hide()
            self.ui.table_page.show()
            self.ui.back_btn_table.clicked.connect(self.back_in_main_page)
    def on_click_registration_but(self):
        self.ui.main_page.hide()
        self.ui.registration_page.show()
        self.ui.reg_btn_reg_page.clicked.connect(self.input_data_registration)
        self.ui.back_btn_reg.clicked.connect(self.back_in_main_page)

    def input_data_registration(self):
        login = self.ui.reg_login_edit.text()  # сверить с бд
        password = self.ui.reg_pass_edit.text()
        password_2 = self.ui.reg_pass_edit_2.text()
        if password == password_2:
            add_in_users_table(self.con, login, password)
            self.ui.registration_page.hide()
            self.ui.table_page.show()
            self.ui.back_btn_table.clicked.connect(self.back_in_main_page)


    def back_in_main_page(self):
        self.ui.registration_page.hide()
        self.ui.entry_page.hide()
        self.ui.table_page.hide()
        self.ui.main_page.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = Start()
    application.show()
    sys.exit(app.exec_())