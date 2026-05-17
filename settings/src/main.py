"""
Settings/Config Panel - Requirements:Settings/Config Panel - Requirements:
Goals:

Create a window titled "Settings"
Window size: 600x400 pixels
Input fields for settings:

Name (text input)
Theme (dropdown/combobox: Light, Dark)
Font size (spinbox or slider: 8-24)


"Apply" button saves settings to a file
"Reset" button loads settings from file
Settings persist when you close and reopen the app
"""

from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QTextEdit, QComboBox, QSlider
from PyQt6.QtCore import Qt
import json
import sys

class Settings(QWidget):
    def __init__(self):
        # initialization
        super().__init__()

        # setup
        self.setWindowTitle('Settings')
        self.resize(600, 400)

        # gui
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        settings = QVBoxLayout()
        ar_buttons = QHBoxLayout()
        name_box = QHBoxLayout()
        theme_combo = QHBoxLayout()
        font_size_slider = QHBoxLayout()

        apply_button = QPushButton('Apply', clicked=self.apply)
        reset_button = QPushButton('Reset', clicked=self.reset)

        # name text edit
        name_label = QLabel('Name:')
        self.name_field = QTextEdit()
        self.name_field.setFixedHeight(24)

        name_box.addWidget(name_label)
        name_box.addWidget(self.name_field)

        # theme combo box
        theme_label = QLabel('Theme:')
        self.theme_dropdown = QComboBox()
        self.theme_dropdown.addItem('Light')
        self.theme_dropdown.addItem('Dark')

        theme_combo.addWidget(theme_label)
        theme_combo.addWidget(self.theme_dropdown)

        # font size slider
        font_label = QLabel('Font Size:')
        self.font_labels = QLabel('_')
        font_label.setFixedHeight(24)
        self.font_slider = QSlider()
        self.font_slider.setOrientation(Qt.Orientation.Horizontal)
        self.font_slider.setMinimum(8)
        self.font_slider.setMaximum(24)

        font_size_slider.addWidget(font_label)
        font_size_slider.addWidget(self.font_labels)
        font_size_slider.addWidget(self.font_slider)

        # add/reset
        ar_buttons.addWidget(apply_button)
        ar_buttons.addWidget(reset_button)

        # add to main settings layout
        settings.addLayout(font_size_slider)
        settings.addLayout(theme_combo)
        settings.addLayout(name_box)
        settings.addLayout(ar_buttons)

        # apply
        main_layout.addLayout(settings)

        # import settings
        #self.reset()
        with open('settings.json', 'r') as f:
            self.settings_cnfg = json.load(f)
            self.name_field.setText(self.settings_cnfg["name"])
            self.theme_dropdown.setCurrentText(self.settings_cnfg["theme"].capitalize())
            self.font_slider.setValue(self.settings_cnfg["font_size"])
            self.font_labels.setText(f'{self.settings_cnfg["font_size"]}')

    def apply(self):
        with open('settings.json', 'w') as f:
            self.settings_cnfg["name"] = self.name_field.toPlainText()
            self.settings_cnfg["theme"] = self.theme_dropdown.itemText(self.theme_dropdown.currentIndex()).lower()
            self.settings_cnfg["font_size"] = self.font_slider.value()
            self.font_labels.setText(f'{self.settings_cnfg["font_size"]}')
            json.dump(self.settings_cnfg, f)

    def reset(self):
        with open('default.json', 'r') as f:
            self.settings_cnfg = json.load(f)
            self.name_field.setText(self.settings_cnfg["name"])
            self.theme_dropdown.setCurrentText(self.settings_cnfg["theme"].capitalize())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Settings()
    window.show()
    sys.exit(app.exec())