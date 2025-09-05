# File Manager Automation

A Python script that automatically organizes files in your Documents folder by categorizing them based on their file extensions. The script creates organized subfolders and moves files accordingly while safely handling hidden and system files.

## Features

- **Automatic File Organization**: Automatically sorts files into predefined categories based on file extensions
- **Safe Processing**: Skips hidden and system files to prevent accidental modification of critical system files

## Supported File Categories

### Images
- `.jpg`, `.png`, `.jpeg`, `.gif`, `.jfif`, `.webp`, `.svg`

### Documents
- `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`

### Audio
- `.mp3`, `.wav`, `.m4a`, `.ogg`, `.aac`, `.flac`, `.wma`, `.aiff`

### Video
- `.mp4`, `.avi`, `.mkv`, `.wmv`, `.webm`

### Other
- Any file extension not covered by the above categories

## How It Works

1. **File Discovery**: Scans the Documents folder for all files
2. **Hidden File Detection**: Identify and skip hidden or system files (windows only)
3. **Extension Analysis**: Extracts file extensions and converts them to lowercase for case-insensitive matching
4. **Category Assignment**: Maps file extensions to appropriate categories using a predefined dictionary
5. **Directory Creation**: Creates target directories if they don't exist
6. **File Organization**: Moves files to their respective category folders

## Requirements

- Python 3.x
- Windows operating system (uses Windows-specific API calls)

## Usage

1. Open a command prompt or PowerShell
2. Navigate to the project directory
3. Run the script:
   ```bash
   python script.py
   ```

## Target Directory

The script operates on your Documents folder by default:
- **Windows**: `C:\Users\[username]\Documents`

## File Structure After Organization

```
Documents/
├── Images/
│   ├── photo1.jpg
│   ├── image2.png
│   └── ...
├── Documents/
│   ├── report.pdf
│   ├── spreadsheet.xlsx
│   └── ...
├── Audio/
│   ├── song1.mp3
│   ├── music.wav
│   └── ...
├── Video/
│   ├── movie.mp4
│   ├── clip.avi
│   └── ...
└── other/
    ├── unknown_file.xyz
    └── ...
```

## Technical Details

- Uses `pathlib.Path` for cross-platform path handling
- Implements Windows API calls via `ctypes` for file attribute checking
- Creates directories with `exist_ok=True` and `parents=True` for safe directory creation

## Customization

To modify the file categories or add new file types:

1. Edit the `categories` dictionary in `script.py`
2. Add new extensions to existing categories or create new categories
3. The script will automatically handle the new categories

## Future Improvements

### Planned Enhancements

- **Graphical User Interface (GUI)**: Add a user-friendly interface to make the tool more accessible to non-technical users
  - Progress tracking and status updates
  - Settings and preferences panel

- **Executable Script**: Convert the Python script into a standalone executable file

- **System Integration**: Integrate with Windows Task Scheduler for automated execution
  - Scheduled file organization (daily, weekly, or custom intervals)

## Notes

- The script processes files in the order they are found in the directory
- Hidden and system files are completely skipped and will not be moved
- The script will create the target directory structure as needed
- Files with unrecognized extensions will be placed in the "other" category
