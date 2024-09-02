import subprocess
import os
import random
from AppKit import NSScreen # Import NSScreen for display detection

#Define Predefined wallpaper Folders using absolute paths
# Ensure these folders exists and have the desired wallpapers

SINGLE_DISPLAY_FOLDER = os.environ.get('SINGLE_DISPLAY_FOLDER')
MULTI_DISPLAY_FOLDER = os.environ.get('MULTI_DISPLAY_FOLDER')

def validate_folder_path(folder_path):
    """
    Validates if the given folder path is set and exists.

    Args:
        folder_path (str): The folder path to be validated.

    Returns:
        bool: True if the path is valid, False otherwise.
    """

    if folder_path and os.path.isdir(folder_path):
        return True
    else:
        print(f"Invalid for folder path is not set: {folder_path}")
        return False
    
def get_number_of_displays():
    """
    Securely returns the number of connected displays on macOS.

    This function uses the NSScreen class from the AppKit framework to retrieve
    the number of screens currently connected to the system. It includes error 
    handling to manage any exceptions that may occur during the process.
    
    Returns:
        int: The number of connected displays. Returns 0 if an error occurs.
    """

    try:
        # Use NSScreen.screens() to get a list of all connected displays
        screens = NSScreen.screens()

        # Return the length of the screens list which indicates the number of displays
        return len(screens)
    except Exception as e:
        # Print an error message to indicate what went wrong
        print(f"Error retrieving display information: {e}")

        # Return 0 as a safe default if theres an error
        return 0
    
def set_wallpaper_folder(folder_path):
    """
    Securely sets the wallpaper source folder for all desktops using a predefined AppleScript command.

    This function uses osascript to interact with macOS System Events to change the wallpaper folder.
    It validates the folder path to ensure it's a predefined, secure path before executing the command.
    Proper error handling is included to manage potential issues during execution.

    Args:
        folder_path (str): The absolute path to the wallpaper folder to set.

    Returns:
        None
    
    Validate the input folder path to ensure it's secure and predefined
    """
    if not validate_folder_path(folder_path):
        return
    
    try:
        image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg','.jpeg','.png','.bmp'))]
        if not image_files:
            print(f"No image files found in the folder: {folder_path}")
            return
    except Exception as e:
        print(f"Error accessing wallpaper folder: {e}")
        return
    
    # Selecting random image from the folder
    chosen_image = os.path.join(folder_path, random.choice(image_files))

    # Prep AppleScript command to change the wallpaper for each desktop
    script = f'''
    tell application "System Events"
        repeat with d in desktops
            set picture of d to POSIX file "{chosen_image}"
        end repeat
    end tell
    '''


    try:
        # Use subprocess.run() to execute the AppleScript securely
        result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True, check=True)
        print(f"Wallpaper succesfully set to: {chosen_image}")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
    except subprocess.CalledProcessError as e:
        # Print an error message if the osascript command fails
        print(f"Error changing wallpaper: {e}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Informative logging for script execution
    print("Starting wallpaper change script...")

    # Detect the number of displays
    num_displays = get_number_of_displays()
    print(f"Number of connected displays detected: {num_displays}")

    # Determine which wallpaper folder to use based on the number of displays
    if num_displays == 1:
        print("Setting wallpaper for single display setup.")
        set_wallpaper_folder(SINGLE_DISPLAY_FOLDER)
    elif num_displays > 1:
        print("Setting wallpaper for multi-display setup.")
        set_wallpaper_folder(MULTI_DISPLAY_FOLDER)
    else:
        print("Error: No displays detected or an error occurred while detecting displays.")
    
    print("Wallpaper change script completed.")