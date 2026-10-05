# Automated File Organizer

A lightweight Python script that automatically scans a designated directory and organizes loose files into categorized subfolders based on their file extensions.

## Features

- **Automatic Categorization:** Automatically groups files into dedicated folders:
  - **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`
  - **Documents:** `.pdf`, `.docx`, `.txt`, `.xlsx`
  - **Audio:** `.mp3`, `.wav`
  - **Videos:** `.mp4`, `.mov`
  - **Archives:** `.zip`, `.rar`
- **Fallback Handling:** Files with uncategorized extensions are moved to an **Others** directory.
- **Safe Directory Operations:** Skips pre-existing subfolders and creates new subfolders dynamically only when needed.
- **Case-Insensitive Matching:** Handles extensions regardless of uppercase/lowercase formatting (e.g., `.JPG` vs `.jpg`).

## Prerequisites

- Python 3.x installed on your system.
- Uses Python standard modules (`os` and `shutil`), so no external packages (`pip install`) are required.

## Quick Start

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/your-username/file-organizer.git
   cd file-organizer
   ```

2. **Configure Target Directory:**
   Open `file_organizer.py` and update the `TARGET_DIR` path to the directory you want to clean up:
   ```python
   TARGET_DIR = r"C:\Users\YourUsername\Path\To\Your\Workspace"
   ```

3. **Run the Script:**
   ```bash
   python file_organizer.py
   ```

## Customization

You can add or modify file categories by extending the `TRACKED_EXTENSIONS` dictionary in `file_organizer.py`:

```python
TRACKED_EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Code": [".py", ".js", ".html", ".css"],
    # Add custom categories here
}
```

## License

This project is open source and available under the [MIT License](LICENSE).