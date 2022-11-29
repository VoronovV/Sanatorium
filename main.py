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
            self.open_menu()

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
            self.open_menu()


    def back_in_main_page(self):
        self.ui.registration_page.hide()
        self.ui.entry_page.hide()
        self.ui.table_page_empl.hide()
        self.ui.table_page_proc.hide()
        self.ui.table_page_rooms.hide()
        self.ui.table_page_clients.hide()
        self.ui.menu_page.hide()
        self.ui.main_page.show()


    def back_in_menu(self):
        self.ui.table_page_empl.hide()
        self.ui.table_page_proc.hide()
        self.ui.table_page_rooms.hide()
        self.ui.table_page_clients.hide()
        self.ui.menu_page.show()

    def open_menu(self):
        self.ui.entry_page.hide()
        self.ui.menu_page.show()
        self.ui.exit_btn.clicked.connect(self.back_in_main_page)
        self.ui.clients_btn.clicked.connect(self.open_clients_table)
        self.ui.employees_btn.clicked.connect(self.open_empl_table)
        self.ui.rooms_btn.clicked.connect(self.open_rooms_table)
        self.ui.proc_btn.clicked.connect(self.open_proc_table)


    def open_clients_table(self):
        self.ui.menu_page.hide()
        self.ui.table_page_clients.show()

        self.ui.back_btn_clients.clicked.connect(self.back_in_menu)
    def open_empl_table(self):
        self.ui.menu_page.hide()
        self.ui.table_page_empl.show()

        self.ui.back_btn_empl.clicked.connect(self.back_in_menu)
    def open_rooms_table(self):
        self.ui.menu_page.hide()
        self.ui.table_page_rooms.show()

        self.ui.back_btn_rooms.clicked.connect(self.back_in_menu)
    def open_proc_table(self):
        self.ui.menu_page.hide()
        self.ui.table_page_proc.show()

        self.ui.back_btn_proc.clicked.connect(self.back_in_menu)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = Start()
    application.show()
    sys.exit(app.exec_())