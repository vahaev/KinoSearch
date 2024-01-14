import webbrowser

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QIcon

def getHarryPotter():
    webbrowser.open('https://www.kinopoisk.ru/film/689/')

app = QApplication([])
window = QWidget()
window.setWindowTitle('Кинопоиск')
window.resize(400,200)

main_line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()

text = QLabel('Выберите фильм:')
button1 = QPushButton('Гарри Поттер')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')

button1.clicked.connect(getHarryPotter)

line1.addWidget(button1, alignment=Qt.AlignCenter)
line1.addWidget(button2, alignment=Qt.AlignCenter)
line2.addWidget(button3, alignment=Qt.AlignCenter)
line2.addWidget(button4, alignment=Qt.AlignCenter)

main_line.addWidget(text, alignment=Qt.AlignCenter)
main_line.addLayout(line1)
main_line.addLayout(line2)

window.setLayout(main_line)
window.show()
app.exec()
