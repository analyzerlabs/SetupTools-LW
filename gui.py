import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from setuptools import *

Ui_Dialog window() 
window.setupUi()
'''
def dialog():
    mbox = QMessageBox()

    mbox.setText("Your allegiance has been noted")
    mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
    mbox.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(1080,720)
    w.setWindowTitle('SetupTools')
    
    label = QLabel(w)
    label.setText("Behold the Guru, Guru99")
    label.move(100,130)
    label.show()

    btn = QPushButton(w)
    btn.setText('Beheld')
    btn.move(110,150)
    btn.show()
    btn.clicked.connect(dialog)

    
    w.show()
    sys.exit(app.exec_())'''


    listaComs = self.ReadCOMS()
        j=0
        for i in listaComs:
            print(listaComs[j])
            self.COM_LIST.addItem("")  
            self.COM_LIST.setItemText(j, _translate("SetupTools",str(listaComs[j]) ))
            j = j +1

    def ReadCOMS(self):
        result = []
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result   

    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        SetupTools = QtWidgets.QDialog()
        ui = Ui_SetupTools()
        ui.setupUi(SetupTools)
        SetupTools.show()
        sys.exit(app.exec_())
