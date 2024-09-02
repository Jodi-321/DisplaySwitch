# DisplaySwitch for Multiple Displays

This Python script automatically changes the desktop wallpaper on macOS based on the number of connected displays. It allows for dynamic switching between two sets of wallpapers: one formatted for a single display setup and another for a multi-display setup.

## Purpose

The need for this script arose from managing different wallpaper formats tailored to either single or multiple display setups. By detecting the number of connected displays, this script provides a quick way to set the appropriate wallpapers to fit the display configuration without manual adjustments.

## Features

- **Automatic Detection of Connected Displays:** Utilizes macOS's `AppKit` framework to determine the number of connected displays.
- **Dynamic Wallpaper Management:** Chooses a random wallpaper from a predefined folder based on the number of displays.
- **Simple and Secure Execution:** Validates inputs and securely executes AppleScript commands using Python's `subprocess` module.

## How It Works

1. **Display Detection:**
   - The script detects the number of connected displays using the `NSScreen` class from the `AppKit` framework.
   
2. **Wallpaper Selection:**
   - If there is **one display**, it selects a random wallpaper from the `SINGLE_DISPLAY_FOLDER`.
   - If there are **multiple displays**, it selects a random wallpaper from the `MULTI_DISPLAY_FOLDER`.

3. **Wallpaper Application:**
   - The selected wallpaper is applied to all desktops (Spaces) using `osascript` (AppleScript commands) through the Terminal.

## Current Known Issue

While the script successfully changes the wallpaper for new desktops added after running the script, existing desktops (Spaces) may not always reflect the updated wallpaper. This appears to be due to a caching mechanism or specific behavior in macOS that prevents existing desktops from immediately reflecting new settings. We are currently investigating the cause and possible resolutions for this issue.

## Setup

1. **System Requirements:**
   - macOS with Python 3 installed.
   - `pyobjc` library to interface with macOS APIs:
     ```bash
     pip install pyobjc
     ```

2. **Folder Structure:**
   - Two folders containing wallpapers:
     - `SINGLE_DISPLAY_FOLDER`: Folder with wallpapers formatted for single display setups.
     - `MULTI_DISPLAY_FOLDER`: Folder with wallpapers formatted for multi-display setups.

3. **Configure the Script:**
   - Update the paths for `SINGLE_DISPLAY_FOLDER` and `MULTI_DISPLAY_FOLDER` in the script to point to your desired directories.

## Usage

1. **Run the Script:**
   - Open Terminal and navigate to the directory containing the script.
   - Execute the script using Python:
     ```bash
     python3 wallpaper_changer.py
     ```
   
2. **Output:**
   - The script will output the number of displays detected, the selected wallpaper folder, and the status of the wallpaper change process.


## Troubleshooting

- **No Image Found:** Ensure the folders contain image files with extensions `.jpg`, `.jpeg`, `.png`, or `.bmp`.
- **Permissions:** Make sure Terminal or any IDE you use (e.g., VS Code) has Accessibility permissions enabled under **System Settings > Privacy & Security > Accessibility**.

## Conclusion

This script provides a simple way to manage desktop wallpapers on macOS based on display configurations. Further investigation is needed to resolve the issue of existing desktops not always updating their wallpaper correctly.



