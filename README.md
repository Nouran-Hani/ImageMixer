# Image Mixer Application
The Image Mixer project is a graphical application designed for mixing and processing images using Fourier Transform (FT) components. It provides a user-friendly interface to load images, perform Fourier Transform operations, and create composite images by combining selected FT components.

## Features

### 1. Graphical User Interface (GUI)
The application offers a user-friendly GUI with the following components:
- **Image Viewports**: Display loaded images for processing.
- **Fourier Transform (FT) Viewports**: Show FT components of the loaded images.
- **Output Viewports**: Display the final mixed and processed images.

### 2. Image Loading and Processing
- **Load Images**: Users can upload images in formats like PNG, JPG, JPEG, and JFIF using the "Browse" option in each Image Viewport.
- **Image Processing**: Loaded images are transformed into Fourier Transform components, visualized in the FT Viewports. These components form the basis for mixing operations.

### 3. Image Mixing
- **Mixing Options**: Users can mix pairs of FT components (Magnitude, Phase, Real, Imaginary) selected from combo boxes. The application ensures valid selections before proceeding.
- **Adjustable Parameters**: Sliders allow users to control the weights of the selected FT components, enabling fine-tuning of the final mixed image.

### 4. Realtime Mixing
- **Progress Bar**: Since the mixing process requires an Inverse Fourier Transform (IFFT) operation that can take some time, a progress bar is displayed to indicate the status of the process.
- **Thread Management**: If the user changes the mixing settings and requests an update while a previous operation is still running, the program cancels the previous operation and starts processing the new request. This ensures responsiveness and seamless user experience.

### 4. Interactive User Interactions
- **Component Selection**: Users can select and manipulate specific regions of images or FT components to enhance control over the mixing process.
- **Brightness and Contrast Adjustment**: Adjust brightness and contrast of images interactively via mouse movements, ensuring clear visualization of regions during the mixing process.

### 5. Error Handling
- **Informative Feedback**: The application provides error messages to guide users when invalid inputs or operations occur, such as improper FT component selections.

### 6. Logging
- **Activity Logs**: Events and errors are logged into a file named `Mixer.log`. This log aids in debugging and provides a record of the application's activities.

---

## How to Use

### Run the Application:
1. Execute the script to launch the GUI.

### Load Images:
1. Double-click on any Image Viewport and use the "Browse" option to upload images.

### Adjust Visualization:
1. Use right-click and drag (horizontal/vertical) on the mouse to modify brightness and contrast.

### Select Mixing Options:
1. Choose FT components and adjust the mixing parameters using the sliders.

### Mix Images:
1. Click the **"Mix"** button to generate the mixed image.

### View Output:
1. The mixed image will appear in the selected Output Viewport.

---

## Dependencies

This project relies on the following Python libraries:
- **PyQt5**: For GUI development.
- **NumPy**: For numerical computations and FFT computations.
- **OpenCV (cv2)**: For image processing.

---

- ## Demo
Check out the demo video for a walkthrough of the application: `Demo.mp4`

---

## How to run
### Install the dependencies:
```bash
pip install -r requirements.txt
```
### Run the application using:
```bash
python main.py
```

---

## Contributors
| [**Talal Emara**](https://github.com/TalalEmara) | [**Meram Mahmoud**](https://github.com/Meram-Mahmoud) | [**Maya Mohammed**](https://github.com/Mayamohamed207) | [**Nouran Hani**](https://github.com/Nouran-Hani) | [**Nariman Ahmed**](https://github.com/nariman-ahmed) |
|:------------------------------------------:|:------------------------------------------:|:------------------------------------------:|:------------------------------------------:|:------------------------------------------:|

---
## Contributors

| ![Talal Emara](https://avatars.githubusercontent.com/TalalEmara?s=100) [**Talal Emara**](https://github.com/TalalEmara) | ![Meram Mahmoud](https://avatars.githubusercontent.com/Meram-Mahmoud?s=100) [**Meram Mahmoud**](https://github.com/Meram-Mahmoud) | ![Maya Mohammed](https://avatars.githubusercontent.com/Mayamohamed207?s=100) [**Maya Mohammed**](https://github.com/Mayamohamed207) | ![Nouran Hani](https://avatars.githubusercontent.com/Nouran-Hani?s=100) [**Nouran Hani**](https://github.com/Nouran-Hani) | ![Nariman Ahmed](https://avatars.githubusercontent.com/nariman-ahmed?s=100) [**Nariman Ahmed**](https://github.com/nariman-ahmed) |
|:------------------:|:----------------------:|:-----------------------:|:-------------------:|:-------------------:|


Feel free to explore, experiment, and enhance the Image Mixer application.

