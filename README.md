# Desktop Widget Application

This is a simple desktop widget application that allows users to set an image on their desktop. The image can be resized, repositioned, and the widget will persist even after shutting down or restarting the PC. The application supports right-click options to change the image or exit the widget.

## Features
- **Add Image to Desktop**: Add any image as a widget that stays on your desktop.
- **Resizable Widget**: Resize the widget by dragging its edges.
- **Persistent**: The widget stays on the desktop even after system shutdowns and power-ons.
- **Right-Click Options**: Right-click on the widget to either change the image or exit the widget.
- **Minimize/Maximize**: Minimize or maximize the widget window as required.

To format your markdown so that the images appear below each step, you can adjust the structure like this:

## To Use the Program 
- just go to Desktop-Image-widget folder
- click on dist folder
- now you can see widget_app.exe file click on this and run this program without any hasale 


## Picture

1. Click on the .exe file  
   ![image](https://github.com/user-attachments/assets/fdfa096a-a5da-446c-824e-4d177d01c795)

2. This window will appear  
   ![image](https://github.com/user-attachments/assets/46dceb64-06b8-4a92-ac1b-557cb5505aaa)

3. Right-click to choose an image or exit  
   ![image](https://github.com/user-attachments/assets/e6bb98b3-d305-43b5-8d27-51fe2ca6d345)

4. Click "Choose Image"  
   ![image](https://github.com/user-attachments/assets/2ac4004f-b059-4cd2-9f9d-31ab15981544)

5. The image will be display on this window  
   ![image](https://github.com/user-attachments/assets/f5932ded-234f-4c55-b8c0-a5bea9f62d85)


## Installation

### Prerequisites

Before installing the application, make sure you have the following installed:

- Python (version 3.7 or higher)
- `tkinter` (for the GUI)
- `Pillow` (for image handling)

### Steps to Install

1. **Clone the Repository**:
   If you haven't already, clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/widget-app.git
   cd widget-app
   ```

2. **Install Python Dependencies**:
   Install the necessary Python libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can manually install the required packages:
   ```bash
   pip install tkinter pillow
   ```

3. **Run the Application**:
   After setting up the environment, you can run the application by executing the following command:
   ```bash
   python widget_app.py
   ```

   The application will open a window where you can set your image, resize the widget, and place it on your desktop.

## Known Issues

1. **Icon Setup Issue**:
   - There is a known issue with setting the application icon. While we have attempted to use `PyInstaller` to compile the application with a custom icon, the icon might not be displayed correctly when the application is executed.
   - If you are facing issues with the icon setup, please follow the steps mentioned in the instructions below:
     - **PyInstaller Icon Setup**:
       To set a custom icon for your executable, use the following command:
       ```bash
       pyinstaller --onefile --noconsole --icon=path_to_your_icon.ico widget_app.py
       ```
       However, some users have reported that the icon doesn’t display as expected in the compiled `.exe` file.
     - This issue is still under investigation, and we will update the README with more details once it is resolved.

2. **Widget Behavior**:
   - If you resize the widget too much, it may cause the image to look distorted. The widget only adjusts its size based on the image size, but it may not maintain the aspect ratio perfectly when resized manually.
   - The widget may sometimes not be properly aligned with the screen after maximizing/minimizing. We recommend adjusting the position manually after maximizing.

## Usage

Once the application is running:

1. **Set Image**: 
   - Use the "Set Image" button to select an image that you want to display on your desktop.
   - You can also right-click on the widget to change the image.

2. **Resize Widget**:
   - You can resize the widget by dragging its right botttom corner edge.
   
3. **Right-Click Options**:
   - **Change Image**: Right-click to select a new image for the widget.
   - **Exit Widget**: Right-click to exit the widget.

4. **Minimize/Maximize**:
   - Minimize the widget to the taskbar when you no longer need it open, or maximize it to adjust its size.

## Troubleshooting

If you encounter any issues:

- Ensure that you are running the script with the appropriate permissions, especially if it involves writing to system files or directories.
- If the widget doesn’t stay on top of the desktop after restarting, make sure the application is configured to launch on startup, either manually or by using the provided `auto-start` feature.
  
## Contributing

Feel free to contribute to the project by reporting bugs or submitting pull requests. If you encounter any issues with the widget (e.g., the icon setup or functionality)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


