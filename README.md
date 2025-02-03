# Youtube-DL

![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blue) ![License](https://img.shields.io/badge/License-Apache%202.0-green)

## 📌 Overview

**Youtube-DL** is a simple, no-frills Python GUI application that utilizes [youtube-dl](https://github.com/ytdl-org/youtube-dl) to download videos from various streaming platforms. It provides an easy-to-use interface for users who prefer a graphical experience over command-line usage.

## 🚀 Features

- Lightweight and easy-to-use GUI built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Supports downloading videos from multiple streaming services [See Here](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)
- Compatible with Windows and Linux
- No module installations required – just run the script or executable

## 🛠 Installation

### Requirements

- Python **2.6, 2.7, or 3.2+**
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- **Windows** (preferred) or **Linux**

### Setup

1. Download the project ZIP file from the [GitHub repository](#).
2. Extract the contents to a folder of your choice.
3. Ensure Python is installed on your system.

## 📖 Usage

### Running the Application

#### Using Python:

```sh
python main.py
```

#### Using the Executable (Windows Only):

- Locate `Youtube-DL.exe` in the extracted folder.
- Double-click to open the application.

### Troubleshooting

If you encounter an **Error 403**, try the following solutions:

If the video fails to download it may be because:

the video requires authentication to view ie. age restricted
The website is requiring a custom web header
Video may be Geoblocked
The video is from a playlist you need to utilize the main video URL
```
pip install --upgrade yt-dlp
```
    

## 📜 License

This project is licensed under the **Apache 2.0 License**.

### Acknowledgments

This project utilizes:

- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

---

💡 **Contributions & Issues**: Feel free to submit issues or contribute via pull requests!
