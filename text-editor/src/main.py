from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QHBoxLayout, QMessageBox
import sys

class TextEditor(QWidget):
    def __init__(self):
        # initialization
        super().__init__()

        # setup
        self.setWindowTitle('Text Editor')
        self.resize(800, 600)

        # gui
        sl_layout = QHBoxLayout() # buttons
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.text_box = QTextEdit()
        save_button = QPushButton('Save', clicked=self.save)
        load_button = QPushButton('Load', clicked=self.load)

        sl_layout.addWidget(save_button)
        sl_layout.addWidget(load_button)

        main_layout.addLayout(sl_layout)
        main_layout.addWidget(self.text_box)

    def save(self):
        with open('document.txt', 'w') as f:
            f.write(self.text_box.toPlainText())

    def load(self):
        try:
            with open('document.txt', 'r') as f:
                self.text_box.setPlainText(f.read())

        except FileNotFoundError:
            QMessageBox.warning(self, "File not found", "Please save / create document.txt")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec())