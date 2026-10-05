import os
import shutil

# 1. Define the folder you want to clean up
# Change this path to match where your "ProjectWorkspace" folder is located
TARGET_DIR = r"C:\Users\VICTUS\OneDrive\Desktop\ProjectWorkspace"

# 2. Map folder names to the specific file extensions they should hold
TRACKED_EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".rar"]
}

def clean_directory():
    # Check if the target directory actually exists
    if not os.path.exists(TARGET_DIR):
        print(f"Error: The directory '{TARGET_DIR}' does not exist. Check your path!")
        return

    print(f"Scanning directory: {TARGET_DIR}...\n")
    
    # 3. Loop through every single item inside the target folder
    for filename in os.listdir(TARGET_DIR):
        # Get the full absolute path of the item
        file_path = os.path.join(TARGET_DIR, filename)
        
        # If the item is a folder, skip it (we don't want to move existing folders)
        if not os.path.isfile(file_path):
            continue
            
        # 4. Separate the filename from its extension (e.g., 'photo' and '.jpg')
        name, extension = os.path.splitext(filename)
        extension = extension.lower() # Convert to lowercase to catch .JPG and .jpg
        
        moved = False
        
        # 5. Look through our dictionary to see which folder matches this extension
        for folder_name, extensions in TRACKED_EXTENSIONS.items():
            if extension in extensions:
                # Define where the target subfolder should be
                destination_folder = os.path.join(TARGET_DIR, folder_name)
                
                # Create the subfolder if it doesn't exist yet
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                    print(f"Created Category Folder: [{folder_name}]")
                
                # Define the final full path for the file inside its new home
                destination_path = os.path.join(destination_folder, filename)
                
                # Move the file physically
                shutil.move(file_path, destination_path)
                print(f" -> Moved: '{filename}' to [{folder_name}]")
                
                moved = True
                break # Exit the inner loop since we found a match
                
        # 6. If the file has an extension but didn't match any category, send it to 'Others'
        if not moved and extension != "":
            other_folder = os.path.join(TARGET_DIR, "Others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f" -> Moved Unknown File: '{filename}' to [Others]")

    print("\nOrganization complete! Your workspace is clean.")

# This tells Python to execute our function when we run the script
if __name__ == "__main__":
    clean_directory()