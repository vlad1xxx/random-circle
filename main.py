from PyQt5 import uic
import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton


class DrawCircle(QWidget):
    def __init__(self):
        super().__init__()
        self.should_draw = False
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.draw_btn = QPushButton('Создать кружок', self)
        self.draw_btn.setGeometry(0, 560, 800, 40)
        self.draw_btn.clicked.connect(self.redraw)

    def redraw(self):
        self.should_draw = True
        self.update()

    def paintEvent(self, event):
        if self.should_draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.should_draw = False

    def draw_circle(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        width = randint(0, 800)
        height = randint(0, 560)
        radius = randint(10, 200)
        qp.drawEllipse(width, height, radius, radius)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.paint_circle = DrawCircle()
        self.setCentralWidget(self.paint_circle)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 640)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MyWidget()
    mw.show()
    sys.exit(app.exec())
