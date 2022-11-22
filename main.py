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


        # self.__MainWindow = QtWidgets.QMainWindow()
        # self.__ui = Ui_MainWindow
        # self.__ui.setupUi(self.__MainWindow)
        # self.__MainWindow.show()
        # self.__ui.entry.clicked.connect(self.on_click_entry_but)
        # self.__ui.regisration.clicked.connect(self.on_click_registration_but)
        # sys.exit(app.exec_())  # завершение программы

    def on_click_entry_but(self):
        self.ui.main_page.hide()
        self.ui.entry_page.show()



    def on_click_registration_but(self):
        self.ui.main_page.hide()
        self.ui.registration_page.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = setup()
    application.show()
    sys.exit(app.exec_())