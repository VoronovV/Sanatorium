from GUI import *
import sys

class setup(QtWidgets.QMainWindow):

    def __init__(self):
        super(setup, self).__init__()
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

        self.ui.entry_btn_entry_page.clicked.connect(self.input_data)

    def input_data(self):
        login = self.ui.entry_login_edit.text()  # сверить с бд
        password = self.ui.entry_pass_edit.text()
        print(login)

    def on_click_registration_but(self):
        self.ui.main_page.hide()
        self.ui.registration_page.show()
        login = self.ui.reg_login_edit.text()  # сверить с бд
        password = self.ui.reg_pass_edit.text()
        password_2 = self.ui.reg_pass_edit_2.text()
        if password == password_2:
            self.menu(login)

    def menu(self, login):
        self.ui.entry_page.hide()
        self.ui.registration_page.hide()
        print(login)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = setup()
    application.show()
    sys.exit(app.exec_())