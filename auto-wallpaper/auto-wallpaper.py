#!/usr/bin/env python3

import argparse
import os
import schedule
import logging
import random
import time
from appscript import app, mactypes

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)

def randomly_change_wallpaper(directory: str, img_list: list[str]):
    img_name = random.choice(img_list)
    update_img_path = f'{directory}/{img_name}'
    app('Finder').desktop_picture.set(mactypes.File(update_img_path))
    desktop_picture = app('Finder').desktop_picture.get()
    try:
        if desktop_picture.name.get() == img_name:
            logger.info(f"Successfully updated wallpaper to {img_name}")
        else :
            logger.error(f"Failed to update wallpaper to {img_name}")
    except Exception as ex:
        logger.error(f"Exception encountered while validating wallpaper update attempt: {str(ex)}")

def schedule_wallpaper_update(directory_path: str, all_imgs: list[str]):
    schedule.every().day.at("08:00").do(randomly_change_wallpaper, directory_path, all_imgs)
    schedule.every().day.at("12:30").do(randomly_change_wallpaper, directory_path, all_imgs)
    schedule.every().day.at("17:00").do(randomly_change_wallpaper, directory_path, all_imgs)
    schedule.every().day.at("21:00").do(randomly_change_wallpaper, directory_path, all_imgs)
    logger.info(f"Schedules have been created for changing wallpaper with any random img from the {directory_path} directory.")
    logger.info(f"Scheduler will run on 08:00, 12:30, 17:00, 21:00 times")
    randomly_change_wallpaper(directory_path, all_imgs)    

def main(args):
    # Create a file handler and set its log level
    file_handler = logging.FileHandler(args.log_file, mode='w')
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter and set it to the file handler
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(file_formatter)

    # Add the file handler to the root logger
    logger = logging.getLogger(__name__)
    logger.addHandler(file_handler)

    directory_path = args.directory

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    if os.path.isdir(directory_path):
        rejected_files: list[str] = [
            ".DS_Store",
            ".log"
        ]
        all_imgs: list[str] = os.listdir(directory_path)
        filtered_all_imgs: list[str] = [item for item in all_imgs if item not in rejected_files]
        schedule_wallpaper_update(directory_path, filtered_all_imgs)
    else:
        logger.error(f'Error: {directory_path} wallpaper directory is not a valid directory.')

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                prog='Auto Wallpaper',
                description='Automatically change wallpaper based on provided list of images.'     
    )

    parser.add_argument('directory') # positional argument
    parser.add_argument('log_file', metavar='LOG_FILE', type=str, help='Path to the logging file')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging') # positional argument
    args = parser.parse_args()

    main(args)