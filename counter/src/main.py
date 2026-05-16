from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
import sys

class Counter(QWidget):
    def __init__(self):
        # initialization
        super().__init__()

        self.value = 0

        # setup
        self.setWindowTitle('Counter App')
        self.resize(500, 500)

        # gui
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.label = QLabel(str(self.value))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        add_button = QPushButton('Add 1', clicked=self.add_one)
        take_button = QPushButton('Take 1', clicked=self.take_one)

        layout.addWidget(add_button)
        layout.addWidget(self.label)
        layout.addWidget(take_button)

    def add_one(self):
        self.value += 1
        self.label.setText(str(self.value))

    def take_one(self):
        self.value -= 1
        self.label.setText(str(self.value))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Counter()
    window.show()
    sys.exit(app.exec())