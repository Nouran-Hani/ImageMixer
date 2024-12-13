import sys
import logging
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout
from imageLoader import ImageUploader
from output import Output
from mix import Mix
from PyQt5.QtCore import Qt
from controls import Controls

# Configure logging
logging.basicConfig(
    filename='ImageMixer/logging/mixer.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Mixer(QMainWindow):
    def __init__(self):
        super().__init__()
        logging.info("Initializing Mixer application.")
        
        self.setWindowTitle("Mixer")
        self.setGeometry(50, 50, 1800, 900)

        self.centralWidget = QWidget(self)
        self.centralWidget.setStyleSheet("background-color: #11361e;")
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QHBoxLayout(self.centralWidget)
        self.createLeftColumn()
        self.createRightColumn()
        logging.debug("UI setup complete.")

    def createLeftColumn(self):
        logging.info("Setting up the left column.")
        leftColumn = QVBoxLayout()

        # Create the top row
        topRow = QHBoxLayout()
        self.image_uploader1 = ImageUploader()
        self.image_uploader2 = ImageUploader()
        topRow.addWidget(self.image_uploader1)
        topRow.addWidget(self.image_uploader2)

        topRowWidget = QWidget(self)
        topRowWidget.setLayout(topRow)
        topRowWidget.setObjectName("topRowWidget")
        topRowWidget.setStyleSheet("""
            #topRowWidget {
                border: 3px solid #11361e;
                border-radius: 20px;
                background: #cdd1cf;
            }""")
        leftColumn.addWidget(topRowWidget)

        bottomRow = QHBoxLayout()
        self.image_uploader3 = ImageUploader()
        self.image_uploader4 = ImageUploader()
        bottomRow.addWidget(self.image_uploader3)
        bottomRow.addWidget(self.image_uploader4)

        bottomRowWidget = QWidget(self)
        bottomRowWidget.setLayout(bottomRow)
        bottomRowWidget.setObjectName("bottomRowWidget")
        bottomRowWidget.setStyleSheet("""
            #bottomRowWidget {
                border: 3px solid #11361e;
                border-radius: 20px;
                padding: 10px;
                background: #cdd1cf;
            }""")
        leftColumn.addWidget(bottomRowWidget)

        leftColumnWidget = QWidget(self)
        leftColumnWidget.setLayout(leftColumn)
        self.mainLayout.addWidget(leftColumnWidget, 3)

    def createRightColumn(self):
        logging.info("Setting up the right column.")
        rightColumn = QVBoxLayout()

        self.controls = Controls()
        rightColumn.addWidget(self.controls, 1)

        self.port1 = Output()
        self.port2 = Output()
        rightColumn.addWidget(self.port1, 5)
        rightColumn.addWidget(self.port2, 5)

        self.mix_button = Mix()
        rightColumn.addWidget(self.mix_button, 1)
        rightColumn.setAlignment(self.mix_button, Qt.AlignmentFlag.AlignCenter)
        self.mix_button.clicked.connect(self.get_ft_components)

        rightColumnWidget = QWidget()
        rightColumnWidget.setLayout(rightColumn)
        rightColumnWidget.setObjectName("RightColumnWidget")
        rightColumnWidget.setStyleSheet("""
            #RightColumnWidget {
                border: 3px solid #11361e;
                border-radius: 20px;
                padding: 10px;
                background: #cdd1cf;
            }""")
        rightColumnWidget.setFixedHeight(960)

        self.mainLayout.addWidget(rightColumnWidget, 1)

    def get_ft_components(self):
        logging.info("Collecting Fourier Transform components.")
        try:
            mode, img1, img2, img3, img4, components = None, None, None, None, None, None
            roi = self.controls.get_roi()
            logging.debug(f"ROI selected: {roi}")
            if roi == "Inner":
                if self.controls.get_mode() == "Magnitude/Phase":
                    mode = "mp"
                else:
                    mode = "ri"
                img1 = self.image_uploader1.get_component()[0]
                img2 = self.image_uploader2.get_component()[0]
                img3 = self.image_uploader3.get_component()[0]
                img4 = self.image_uploader4.get_component()[0]
            else:
                if self.controls.get_mode() == "Magnitude/Phase":
                    mode = "mp"
                else:
                    mode = "ri"
                img1 = self.image_uploader1.get_component()[1]
                img2 = self.image_uploader2.get_component()[1]
                img3 = self.image_uploader3.get_component()[1]
                img4 = self.image_uploader4.get_component()[1]

            components = [
                self.image_uploader1.image_ft.get_component(),
                self.image_uploader2.image_ft.get_component(),
                self.image_uploader3.image_ft.get_component(),
                self.image_uploader4.image_ft.get_component()
            ]
            port = self.controls.get_option()
            logging.debug(f"Port selected: {port}, Mode: {mode}")

            if port == "Port 1":
                self.port1.set_data([img1, img2, img3, img4], mode, components)
            else:
                self.port2.set_data([img1, img2, img3, img4], mode, components)
            
            logging.info("Fourier Transform components successfully processed.")
        except Exception as e:
            logging.error(f"Error while processing Fourier Transform components: {e}")

if __name__ == "__main__":
    logging.info("Starting application.")
    app = QApplication(sys.argv)
    window = Mixer()
    window.show()
    try:
        sys.exit(app.exec_())
    except Exception as e:
        logging.critical(f"Application crashed with exception: {e}")