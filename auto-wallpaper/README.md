# Auto Wallpaper

Automatically changes wallpaper by randomly selecting any one img from a list of images. Changes occurs on set schedules.

## Dependencies

> pip install --no-cache-dir -r requirements.txt

## Execution

NOTE: The script is only built for MacOS and utilises launchctl for execution.

### To execute as a launch item, follow below instructions:

- From the root of this script's directory, execute following cmd,
  > sh setup.sh

### To execute as a standalone script, follow below instructions:

- From the root of this script's directory, execute following cmd,
  > python3 auto-wallpaper.py <absolute_path_to_directory_of_wallpaper_images>
