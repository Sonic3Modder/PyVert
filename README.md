# Image Converter Or simply known as, PyVert

A simple GUI application for converting images between different formats, including TIFF, PNG, and JPEG. This application supports a variety of image types, including RAW formats like NEF.

## Features

- Select images from your filesystem
- Choose output format (TIFF, PNG, JPEG)
- Convert NEF (Nikon RAW) images and standard formats (PNG, JPG, JPEG)
- Progress bar to show conversion status
- User-friendly interface built with Tkinter

## Requirements

- Python 3.x
- Required libraries:
  - `tkinter`
  - `opencv-python`
  - `rawpy`
  - `numpy`
  - `tqdm`

You can install the required libraries using pip:

```bash
pip install opencv-python rawpy numpy tqdm
```

## Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/image-converter.git
    cd image-converter
    ```

2. Run the application:

    ```bash
    python image_converter.py
    ```

3. Use the GUI to select an image and choose the desired output format.
4. Click "Convert Image" to start the conversion process. A progress bar will display the status.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the contributors of the libraries used in this project.
- Inspiration from various image processing tools and frameworks.
