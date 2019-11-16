import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint
from ui_file import Ui_MainWindow


class Draw(QMainWindow, Ui_MainWindow):

    def __init__(self):

        super().__init__()
        self.setupUi(self)

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
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            k = randint(5, 200)
            x = randint(5, 250)
            y = randint(5, 250)
            qp.drawEllipse(x, y, k, k)

            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            k = randint(5, 200)
            x = randint(5, 250)
            y = randint(5, 250)
            qp.drawEllipse(x, y, k, k)

            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            qp.setBrush(QColor(r, g, b))
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