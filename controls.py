from PyQt5.QtWidgets import QComboBox, QHBoxLayout, QVBoxLayout, QRadioButton, QWidget, QLabel, QButtonGroup
from PyQt5.QtCore import pyqtSignal

import logging

# Configure logging
logging.basicConfig(
    filename='ImageMixer/Mixer.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Controls(QWidget):
    set_mode = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.option = "Port 1"
        self.selected_roi = "Inner"
        self.selected_mode = "Magnitude/Phase"

        self.layout = QVBoxLayout(self)

        logging.debug("Initializing Controls widget with default values.")
        self.mode()
        self.roi()
        self.radio()
    
    def mode(self):
        logging.debug("Setting up mode combo box.")
        row = QHBoxLayout()

        label = QLabel("Mode:")
        label.setStyleSheet("""color: #11361e;
                            font-size: 20px;
                            font-weight: bold;
                            background: #cdd1cf;""")
        
        self.mode_combo = QComboBox(self)
        self.mode_combo.addItem("Magnitude/Phase")
        self.mode_combo.addItem("Real/Imaginary")
        self.mode_combo.setStyleSheet("""
            QComboBox {
                background-color: #11361e;
                color: #ffffff;
                border: 1px solid #888888;
                border-radius: 5px;
                padding: 5px;
                font-size: 18px;
            }
        QComboBox QAbstractItemView {
            background-color: #cdd1cf;
            border: 1px solid #888888;
            selection-background-color: #3c7551; /* Background color for selected item */
            selection-color: #ffffff; /* Text color for selected item */
        }
        """)
        row.addWidget(label, 1)
        row.addWidget(self.mode_combo, 2)
        self.layout.addLayout(row)

        self.mode_combo.currentIndexChanged.connect(self.update_mode)

    def roi(self):
        logging.debug("Setting up ROI combo box.")
        row = QHBoxLayout()

        label = QLabel("ROI:")
        label.setStyleSheet("""color: #11361e;
                            font-size: 20px;
                            font-weight: bold;
                            background: #cdd1cf;""")
        
        self.roi_combo = QComboBox(self)
        self.roi_combo.addItem("Inner")
        self.roi_combo.addItem("Outer")
        self.roi_combo.setStyleSheet("""
            QComboBox {
                background-color: #11361e;
                color: #ffffff;
                border: 1px solid #888888;
                border-radius: 5px;
                padding: 5px;
                font-size: 18px;
            }
        QComboBox QAbstractItemView {
            background-color: #cdd1cf;
            border: 1px solid #888888;
            selection-background-color: #3c7551; /* Background color for selected item */
            selection-color: #ffffff; /* Text color for selected item */
        }
        """)
        row.addWidget(label, 1)
        row.addWidget(self.roi_combo, 2)
        self.layout.addLayout(row)

        self.roi_combo.currentIndexChanged.connect(self.update_roi)

    def radio(self):
        logging.debug("Setting up radio buttons.")
        row = QHBoxLayout()
        label = QLabel("View:")
        label.setStyleSheet("""color: #11361e;
                            font-size: 20px;
                            font-weight: bold;
                            background: #cdd1cf;""")
        
        self.radio1 = QRadioButton("Port 1")
        self.radio2 = QRadioButton("Port 2")

        self.radio1.setChecked(True)

        self.setStyleSheet("""
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                border-radius: 10px;
                border: 2px solid #11361e;
                background-color: lightgray;
            }
            QRadioButton::indicator:checked {
                background-color: #11361e;
            }
            QRadioButton {
                font-size: 18px;
                color: #11361e;
                padding: 5px;
                background: #cdd1cf;
            }
        """)
        row.addWidget(label)
        row.addWidget(self.radio1)
        row.addWidget(self.radio2)
        self.layout.addLayout(row)

        self.radio1.toggled.connect(self.on_radio_button_toggled)
        self.radio2.toggled.connect(self.on_radio_button_toggled)

    def on_radio_button_toggled(self):
        selected_button = self.sender()
        if selected_button.isChecked():
            self.option = selected_button.text()
            logging .debug(f"Radio button toggled: {self.option}")

    def update_mode(self):
        self.selected_mode = self.mode_combo.currentText()
        self.set_mode.emit(self.selected_mode)
        logging.debug(f"Mode updated: {self.selected_mode}")
    
    def update_roi(self):
        self.selected_roi = self.roi_combo.currentText()
        logging.debug(f"ROI updated: {self.selected_roi}")
    
    def get_option(self):
        logging.debug(f"Getting option: {self.option}")
        return self.option
    
    def get_mode(self):
        logging .debug(f"Getting mode: {self.selected_mode}")
        return self.selected_mode

    def get_roi(self):
        logging.debug(f"Getting ROI: {self.selected_roi}")
        return self.selected_roi
