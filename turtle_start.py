#use this below in LXTerminal to install pyside module
#sudo apt-get install python3-pyside

import sys
import turtle
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication


class TurtleControl(QtWidgets.QWidget):
    def __init__(self, turtle):
        super(TurtleControl, self) . __init__()
        self.turtle = turtle

        self.left_btn = QtWidgets.QPushButton("Left", self)
        self.right_btn = QtWidgets.QPushButton("Right", self)
        self.move_btn = QtWidgets.QPushButton("Move", self)
        self.distance_spin = QtWidgets.QSpinBox()

        self.controlsLayout = QtWidgets.QGridLayout()
        self.controlsLayout.addWidget(self.left_btn, 0, 0)
        self.controlsLayout.addWidget(self.right_btn, 0, 1)
        self.controlsLayout.addWidget(self.distance_spin,1 , 0)
        self.controlsLayout.addWidget(self.move_btn,1 , 1)
        self.setLayout(self.controlsLayout)

        self.distance_spin.setRange(0, 100)
        self.distance_spin.setSingleStep(5)
        self.distance_spin.setValue(20)

        self.move_btn.clicked.connect(self.move_turtle)
        self.right_btn.clicked.connect(self.turn_turtle_right)
        self.left_btn.clicked.connect(self.turn_turtle_left)

    def turn_turtle_left(self):
        self.turtle.left(45)

    def turn_turtle_right(self):
        self.turtle.right(45)

    def move_turtle(self):
        self.turtle.forward(self.distance_spin.value())

#set up turtle
window = turtle.Screen()
babbage = turtle.Turtle()

#Create a QT application
app = QApplication(sys.argv)
control_window = TurtleControl(babbage)
control_window.show()

#Enter Qt application main loop
sys.exit(app.exec_())

