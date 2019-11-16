import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class Draw(QMainWindow):

    def __init__(self):

        super().__init__()
        uic.loadUi('ui_file.ui', self)

        self.clicked = False
        self.draw.clicked.connect(self.run)

    def run(self):
        self.clicked = True
        self.update()

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    def drawBrushes(self, qp):

        if self.clicked:
            qp.setBrush(QColor('yellow'))
            k = randint(5, 200)
            x = randint(5, 250)
            y = randint(5, 250)
            qp.drawEllipse(x, y, k, k)

            qp.setBrush(QColor('yellow'))
            k = randint(5, 200)
            x = randint(5, 250)
            y = randint(5, 250)
            qp.drawEllipse(x, y, k, k)

            qp.setBrush(QColor('yellow'))
            k = randint(5, 200)
            x = randint(5, 250)
            y = randint(5, 250)
            qp.drawEllipse(x, y, k, k)

            self.clicked = False


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Draw()
    ex.show()
    sys.exit(app.exec_())