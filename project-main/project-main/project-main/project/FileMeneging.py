import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = ['file1', 'file2', 'file3']
        self.data1 = {'file1': 0, 'file2': 1, 'file3': 2}
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Главная форма')

        self.btn = QPushButton('Другая форма', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 150)
        self.btn.clicked.connect(self.open_second_form)

        for i in range(3):
            print(i)
            self.data[i] = QLabel(self)
            self.data[i].setText(self.data[i])
            self.data[i].move(100, 30 + i * 30)

            self.btni = QPushButton(self)
            self.btni.resize(30, 30)
            self.btni.move(130, 30 + i * 30)
            self.btni.clicked.connect(self.run)

    def run(self):
        self.sender()

    def open_second_form(self):
        self.second_form = SecondForm(self, "Данные для второй формы")
        self.second_form.show()


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Вторая форма')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())