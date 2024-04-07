#!/bin/bash

set -e

DIR_PATH=$(pwd)
FINAL_PLIST_FILENAME="auto-wallpaper.plist"
PLIST_FILE_TEMPLATE="${DIR_PATH}/template-auto-wallpaper.plist"
PLIST_FILE="${DIR_PATH}/${FINAL_PLIST_FILENAME}"
PLIST_TRANSIENT_FILE="${DIR_PATH}/transient-auto-wallpaper.plist"

PYTHON_PATH=$(which python3)
PY_SCRIPT_PATH="$DIR_PATH/auto-wallpaper.py"
WALLPAPER_DIR_PATH="/Users/prashantsihag/Desktop/wallpaper" # path of directory that holds all wallpapers
LOG_FILE_PATH="/Users/prashantsihag/Downloads/projects/scriptarium/auto-wallpaper/auto-wallpaper.log" # path of directory that holds all wallpapers


echo "Attempting to unload previous plist file from launchctl ..."
launchctl unload ~/Library/LaunchAgents/$FINAL_PLIST_FILENAME

echo "Updating path values in new plist file ..."
sed "s|PYTHON_PATH|${PYTHON_PATH}|g" "$PLIST_FILE_TEMPLATE" > "$PLIST_FILE"
sed "s|PY_SCRIPT_PATH|$PY_SCRIPT_PATH|g" "$PLIST_FILE" > "$PLIST_TRANSIENT_FILE"
sed "s|WALLPAPER_DIR_PATH|$WALLPAPER_DIR_PATH|g" "$PLIST_TRANSIENT_FILE" > "$PLIST_FILE"
sed "s|LOG_FILE_PATH|$LOG_FILE_PATH|g" "$PLIST_FILE" > "$PLIST_TRANSIENT_FILE"
cp -f $PLIST_TRANSIENT_FILE $PLIST_FILE

rm $PLIST_TRANSIENT_FILE

echo "Copying new plist file to ~/Library/LaunchAgents directory ..."
cp auto-wallpaper.plist ~/Library/LaunchAgents/$FINAL_PLIST_FILENAME

echo "Loading new plist file into launchctl ..."
launchctl load ~/Library/LaunchAgents/$FINAL_PLIST_FILENAME

echo "Setup finished."
launchctl list | grep "scriptarium.auto-wallpaper"
