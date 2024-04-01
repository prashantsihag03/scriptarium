#!/usr/bin/env python3

import argparse
import os
import schedule
import random
from appscript import app, mactypes

def randomly_change_wallpaper(directory: str, img_list: list[str]):
    app('Finder').desktop_picture.set(mactypes.File(f'{directory_path}/{random.choice(img_list)}'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='Auto Wallpaper',
                    description='Automatically change wallpaper based on provided list of images.'     
    )

    parser.add_argument('directory') # positional argument
    args = parser.parse_args()
    directory_path = args.directory

    all_imgs: list[str] = []

    # Check if the directory exists
    if os.path.isdir(directory_path):
        # Get all the files in the directory
        all_imgs = os.listdir(directory_path)
    else:
        print(f'Error: {directory_path} is not a valid directory')

    schedule.every().day.at("08:00").do(randomly_change_wallpaper, directory_path, all_imgs)
    schedule.every().day.at("12:30").do(randomly_change_wallpaper, directory_path, all_imgs)
    schedule.every().day.at("17:00").do(randomly_change_wallpaper, directory_path, all_imgs)
    schedule.every().day.at("21:00").do(randomly_change_wallpaper, directory_path, all_imgs)
    print(f"Schedules have been created for changing wallpaper with any random img from the {directory_path} directory.")
    print(f"Scheduler will run on 08:00, 12:30, 17:00, 21:00 times")
    randomly_change_wallpaper(directory_path, all_imgs)

    while True:
        schedule.run_pending()