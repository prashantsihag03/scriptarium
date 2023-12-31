import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"New file created: {event.src_path}")
        organize_files(self.directory_path)

def organize_files(directory_path):
    # Create a dictionary to store file extensions and their corresponding folders
    extensions_folders = {}

    # Iterate through all files in the directory
    for filename in os.listdir(directory_path):
        # Get the file extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()  # Convert to lowercase for consistency

        # Skip directories
        if os.path.isdir(os.path.join(directory_path, filename)):
            continue

        if filename == ".DS_Store":
            continue

        # Create a folder for the extension if it doesn't exist
        if extension not in extensions_folders:
            folder_path = os.path.join(directory_path, extension[1:] + "_files")  # Exclude the dot in the extension
            os.makedirs(folder_path, exist_ok=True)
            extensions_folders[extension] = folder_path
        
        # Move the file to the corresponding folder
        old_path = os.path.join(directory_path, filename)
        new_path = os.path.join(extensions_folders[extension], filename)
        shutil.move(old_path, new_path)
        print(f"Moved: {filename} to {extensions_folders[extension]}")

if __name__ == "__main__":
    your_directory_path = "/Users/prashantsihag/Downloads"

    if os.path.exists(your_directory_path):
        event_handler = FileHandler(your_directory_path)
        observer = Observer()
        observer.schedule(event_handler, path=your_directory_path, recursive=False)
        observer.start()
        print(f"Watching directory: {your_directory_path}")

        try:
            while True:
                pass
        except KeyboardInterrupt:
            observer.stop()
            observer.join()
    else:
        print(f"Directory '{your_directory_path}' does not exist.")