# Folder Path Memorizer

A simple desktop application to save, organize, and quickly access your frequently used folders. Never lose track of important directories again!

## 🚀 Features

- **Save Folders**: Add folders with custom names and their full paths
- **Quick Search**: Real-time search through saved folders by name or path
- **Easy Access**: Double-click to open folders directly in file explorer
- **Data Persistence**: All your saved folders are stored locally and persist between sessions
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **User-Friendly Interface**: Clean and intuitive GUI built with Python Tkinter

## 📸 Screenshots

The application provides:
- Add new folders with browse functionality
- Search through your saved folders
- List view of all memorized folders
- Quick open and delete operations

## 🛠️ Installation & Usage

### Option 1: Run Executable (Windows)
1. Download the latest `folder_memorizer.exe` from the releases
2. Double-click to run - no installation required!
3. The application will create a `folder_paths.json` file to store your data

### Option 2: Run from Source Code
1. Ensure you have Python 3.6+ installed
2. Download `folder_memorizer.py`
3. Run: `python folder_memorizer.py`

## 🔧 Building from Source

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Creating Windows Executable

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. **Build the executable**:
   ```bash
   pyinstaller --windowed folder_memorizer.py
   ```

3. **Find your executable**:
   - Navigate to the `dist/folder_memorizer/` folder
   - The `folder_memorizer.exe` file is ready to use
   - Copy the entire `folder_memorizer` folder to distribute the application

### Alternative Build Options

For a single file executable (larger file, slower startup):
```bash
pyinstaller --onefile --windowed folder_memorizer.py
```

For executable with custom icon:
```bash
pyinstaller --windowed --icon=your_icon.ico folder_memorizer.py
```

## 📁 How to Use

### Adding Folders
1. Enter a custom name for your folder in the "Folder Name" field
2. Click "Browse Folder" to select a directory, or manually type the path
3. Click "Add Folder" to save it

### Searching Folders
- Use the search box to filter folders by name or path
- Search is real-time - results update as you type
- Click "Clear" to show all folders again

### Opening Folders
- **Double-click** any folder in the list to open it
- Or select a folder and click the "Open Folder" button
- Folders open in your default file explorer

### Managing Folders
- Select any folder and click "Delete Selected" to remove it
- Confirm deletion in the popup dialog

## 💾 Data Storage

The application automatically saves your folder data in a `folder_paths.json` file in the same directory as the executable. This file contains:
- Folder names and their corresponding paths
- Data persists between application sessions
- JSON format for easy backup and portability

## 🔧 Technical Details

- **Language**: Python 3
- **GUI Framework**: Tkinter (built-in with Python)
- **Data Storage**: JSON file
- **Build Tool**: PyInstaller
- **Dependencies**: No external dependencies (uses Python standard library)

## 📋 System Requirements

- **Windows**: Windows 7 or later
- **macOS**: macOS 10.12 or later  
- **Linux**: Most modern distributions
- **Memory**: 50MB RAM
- **Storage**: 30-50MB disk space

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

**Application won't start on other computers:**
- The built executable should work on Windows machines without Python installed
- If issues persist, try building with `--onefile` flag

**Antivirus software blocks the executable:**
- This is common with PyInstaller executables
- Add an exception in your antivirus software
- The application is safe and contains no malicious code

**Folders don't open:**
- Ensure the folder paths still exist on your system
- Check that you have permissions to access the folders

**Data not saving:**
- Ensure the application has write permissions in its directory
- Check if `folder_paths.json` is being created

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

If you encounter any issues or have suggestions:
- Create an issue in the repository
- Check existing issues for solutions
- Provide detailed information about your system and the problem

## 🔄 Version History

- **v1.0.0** - Initial release
  - Basic folder memorization functionality
  - Search and browse capabilities
  - Cross-platform support

---

**Made with ❤️ for better file management**