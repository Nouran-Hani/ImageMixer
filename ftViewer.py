from PyQt5.QtWidgets import QLabel, QWidget, QComboBox, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import cv2
import numpy as np

class FourierTransformViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.width, self.height, self.radius = 250, 350, 15
        self.image = None
        self.magnitude = None
        self.phase = None
        self.real = None
        self.imaginary = None

        # ComboBox for selecting Fourier components
        self.component_combo = QComboBox(self)
        self.component_combo.addItem("Choose Component")
        self.component_combo.addItem("Magnitude")
        self.component_combo.addItem("Phase")
        self.component_combo.addItem("Real")
        self.component_combo.addItem("Imaginary")
        self.component_combo.setStyleSheet("""
            QComboBox {
                background-color: #01240e;
                color: #ffffff;
                border: 1px solid #888888;
                border-radius: 5px;
                padding: 5px;
            }
        """)

        # Fourier component display
        self.ft_image_label = QLabel(self)
        self.ft_image_label.setAlignment(Qt.AlignCenter)
        self.ft_image_label.setStyleSheet("border-radius: 10px; border: 2px solid #01240e;")
        self.ft_image_label.setFixedSize(self.width, self.height)

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.component_combo)
        layout.addWidget(self.ft_image_label)

        # Connections
        self.component_combo.currentIndexChanged.connect(self.update_ft_view)

    def compute_fft(self, image):
        """Computes Fourier Transform of the input image."""
        f_transform = np.fft.fft2(image)
        f_shift = np.fft.fftshift(f_transform)
        self.magnitude = np.log1p(np.abs(f_shift))
        self.phase = np.angle(f_shift)
        self.real = np.real(f_shift)
        self.imaginary = np.imag(f_shift)

    def update_ft_view(self):
        """Updates the Fourier component display based on user selection."""
        if not self.image:
            return

        selected = self.component_combo.currentText()
        if selected == "Magnitude":
            component = self.magnitude
        elif selected == "Phase":
            component = self.phase
        elif selected == "Real":
            component = self.real
        elif selected == "Imaginary":
            component = self.imaginary
        else:
            return

        self.display_component(component)

    def display_component(self, component):
        """Displays the selected Fourier component."""
        normalized_component = cv2.normalize(component, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        height, width = normalized_component.shape
        qimage_component = QImage(normalized_component.data, width, height, width, QImage.Format_Grayscale8)
        pixmap_component = QPixmap.fromImage(qimage_component)
        self.ft_image_label.setPixmap(pixmap_component.scaled(self.width, self.height, Qt.KeepAspectRatio))
