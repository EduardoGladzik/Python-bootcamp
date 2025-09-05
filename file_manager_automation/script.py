import os
from pathlib import Path
import ctypes

FILE_ATTRIBUTE_HIDDEN = 0x02
FILE_ATTRIBUTE_SYSTEM = 0x04

def is_hidden_or_system(path):
    """
    Checks if the given file or directory at 'path' is marked as hidden or system on Windows.

    This function uses the Windows API via ctypes to retrieve the file attributes.
    It returns True if the file has either the HIDDEN or SYSTEM attribute set, otherwise False.

    Args:
        path (str or Path): The path to the file or directory to check.

    Returns:
        bool: True if the file is hidden or a system file, False otherwise.
    """
    attributes = ctypes.windll.kernel32.GetFileAttributesW(str(path))
    if attributes == -1:
        # If the attributes could not be retrieved (e.g., file does not exist), return False
        return False
    # Check if either the HIDDEN or SYSTEM attribute is set
    return bool(attributes & (FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM))

target_folder = Path.home() / "Documents"

categories = {
    "Images": [".jpg", ".png", ".jpeg", ".gif", ".jfif", ".webp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".m4a", ".ogg", ".aac", ".flac", ".wma", ".aiff"],
    "Video": [".mp4", ".avi", ".mkv", ".wmv", ".webm"]
}

other_catorie = ["other"]

# This block creates a dictionary called 'category_extension' that maps each file extension
# (in lowercase) to its corresponding category (such as "Images", "Documents", etc.).
# It iterates through the 'categories' dictionary, and for each extension in each category,
# it adds an entry to 'category_extension' with the extension as the key and the category as the value.
category_extension = {}
for category, extensions in categories.items():
    for extension in extensions:
        category_extension[extension.lower()] = category
# print(category_extension)

# Step 1: List all files in the target_folder (Download folder)
# The 'iterdir()' method of a Path object yields all entries (files and directories) in the folder.
# The list comprehension filters these entries to include only files, using 'is_file()'.
files = [file for file in target_folder.iterdir() if file.is_file()]

# Step 2: Iterate over each file found in the folder, cheking if it is hidden or a system file
for file in files:
    # The is_hidden_or_system function ensures that hidden or system files are skipped and not processed by the organizer.
    # The path is constructed using os.path.join for compatibility with the Windows API.
    path = os.path.join(target_folder, file)
    if is_hidden_or_system(path):
        # If the file is hidden or a system file, skip it and continue to the next file.
        continue
    print(f"Processing {file}")
    # Step 3: Get the file extension in lowercase
    # 'file.suffix' returns the file extension (e.g., '.jpg'), and 'lower()' ensures case-insensitivity.
    extension = file.suffix.lower()
    
    # Step 4: Determine the category for the file based on its extension
    # 'category_extension.get()' looks up the extension in the dictionary.
    # If the extension is not found, it defaults to "other".
    category = category_extension.get(extension, "other")
    
    # Step 5: Print out the file and its determined category
    print(f"{file} is a {category} file")
    
    # Step 6: Prepare the path to the folder where this file should be moved.
    # In Python's pathlib, using the '/' operator with Path objects lets you join paths easily.
    # Here, 'target_folder' is the main Downloads folder, and 'category' is a string like "Images" or "Documents".
    # Writing 'target_folder / category' creates a new Path object representing a subfolder inside Downloads,
    # such as 'Downloads/Images' or 'Downloads/Documents'.
    # This is necessary because we want to organize files into subfolders based on their type.
    target_dir = target_folder / category
    
    # Step 7: Create the target directory if it doesn't exist
    # The 'mkdir' method creates a new directory at the path specified by 'target_dir'.
    # The argument 'exist_ok=True' means that if the directory already exists, no error will be raised.
    # The argument 'parents=True' ensures that any missing parent directories are also created as needed.
    # This is important because if, for example, the 'Downloads/Images' folder does not exist,
    # this line will create it (and any necessary parent folders) so that files can be moved there.
    target_dir.mkdir(exist_ok=True, parents=True)
    
    # Step 8: Print a message indicating the file will be moved
    print(f"Moving {file} to {category}")

    # Step 9: Move the file to the target directory
    # The 'rename' method moves the file to the new location specified by 'target_dir / file.name'.
    # This effectively organizes the file into its corresponding category folder.
    file.rename(target_dir / file.name)