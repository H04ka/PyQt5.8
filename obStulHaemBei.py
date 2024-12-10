from PyQt5 import QtWidgets, QtGui, QtCore
import uv


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = uv.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.conver)

        self.ui.lineEdit.setValidator(QtGui.QDoubleValidator())

        self.ui.lineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+[.][0-9]")))

        self.ui.lineEdit_2.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("")))

    def conver(self):
        c = 0
        try:
            a = float(self.ui.lineEdit.text())
            if self.ui.radioButton.isChecked() and self.ui.radioButton_4.isChecked():
                c = round(a, 2)
            if self.ui.radioButton.isChecked() and self.ui.radioButton_5.isChecked():
                c = round(a * 1000)
            if self.ui.radioButton.isChecked() and self.ui.radioButton_6.isChecked():
                c = round(a * 100000)
            if self.ui.radioButton_2.isChecked() and self.ui.radioButton_4.isChecked():
                c = round(a / 1000)
            if self.ui.radioButton_2.isChecked() and self.ui.radioButton_5.isChecked():
                c = round(a, 2)
            if self.ui.radioButton_2.isChecked() and self.ui.radioButton_6.isChecked():
                c = round(a * 100)
            if self.ui.radioButton_3.isChecked() and self.ui.radioButton_4.isChecked():
                c = round(a / 100000)
            if self.ui.radioButton_3.isChecked() and self.ui.radioButton_5.isChecked():
                c = round(a / 100)
            if self.ui.radioButton_3.isChecked() and self.ui.radioButton_6.isChecked():
                c = round(a, 2)
            self.ui.lineEdit_2.setText(str(c))
        except ValueError:
            QtWidgets.QMessageBox.critical(window, 'Empty String Error', 'Строка пуста, введите значение', buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
#this is no petrikova kod this is ivan zagorbenskiy 