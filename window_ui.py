# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 475)
        MainWindow.setMinimumSize(QtCore.QSize(430, 475))
        MainWindow.setMaximumSize(QtCore.QSize(430, 475))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 430, 450))
        self.tabWidget.setObjectName("tabWidget")
        self.sorted_tab = QtWidgets.QWidget()
        self.sorted_tab.setObjectName("sorted_tab")
        self.sorted_table = QtWidgets.QTableWidget(self.sorted_tab)
        self.sorted_table.setGeometry(QtCore.QRect(0, 0, 425, 425))
        self.sorted_table.setMinimumSize(QtCore.QSize(422, 425))
        self.sorted_table.setMaximumSize(QtCore.QSize(425, 422))
        self.sorted_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.sorted_table.setColumnCount(3)
        self.sorted_table.setObjectName("sorted_table")
        self.sorted_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sorted_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sorted_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sorted_table.setHorizontalHeaderItem(2, item)
        self.sorted_table.horizontalHeader().setDefaultSectionSize(140)
        self.sorted_table.horizontalHeader().setStretchLastSection(True)
        self.sorted_table.verticalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.sorted_tab, "")
        self.unsorted_tab = QtWidgets.QWidget()
        self.unsorted_tab.setObjectName("unsorted_tab")
        self.unsorted_table = QtWidgets.QTableWidget(self.unsorted_tab)
        self.unsorted_table.setGeometry(QtCore.QRect(0, 0, 425, 425))
        self.unsorted_table.setMinimumSize(QtCore.QSize(422, 425))
        self.unsorted_table.setMaximumSize(QtCore.QSize(425, 422))
        self.unsorted_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.unsorted_table.setColumnCount(4)
        self.unsorted_table.setObjectName("unsorted_table")
        self.unsorted_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.unsorted_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.unsorted_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.unsorted_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.unsorted_table.setHorizontalHeaderItem(3, item)
        self.unsorted_table.horizontalHeader().setDefaultSectionSize(106)
        self.unsorted_table.horizontalHeader().setStretchLastSection(True)
        self.unsorted_table.verticalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.unsorted_tab, "")
        self.settings_tab = QtWidgets.QWidget()
        self.settings_tab.setObjectName("settings_tab")
        self.barcode_col_box = QtWidgets.QSpinBox(self.settings_tab)
        self.barcode_col_box.setGeometry(QtCore.QRect(190, 18, 42, 22))
        self.barcode_col_box.setMinimum(1)
        self.barcode_col_box.setMaximum(999)
        self.barcode_col_box.setProperty("value", 3)
        self.barcode_col_box.setObjectName("barcode_col_box")
        self.label = QtWidgets.QLabel(self.settings_tab)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.settings_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.open_btn = QtGui.QAction(MainWindow)
        self.open_btn.setObjectName("open_btn")
        self.menu.addAction(self.open_btn)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Report Counter"))
        item = self.sorted_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Пилот"))
        item = self.sorted_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Количество"))
        item = self.sorted_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Процент анридов"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sorted_tab), _translate("MainWindow", "Отсортировано"))
        self.unsorted_table.setSortingEnabled(False)
        item = self.unsorted_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Аллея"))
        item = self.unsorted_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Количество"))
        item = self.unsorted_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Пилот"))
        item = self.unsorted_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Процент анридов"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.unsorted_tab), _translate("MainWindow", "Не отсортировано"))
        self.label.setText(_translate("MainWindow", "Столбец с штрихкодами"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), _translate("MainWindow", "Настройки"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.open_btn.setText(_translate("MainWindow", "Открыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
