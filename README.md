[better wallpaper by time](https://imgur.com/a/ycrbgId)
# Wallpaper Changer By Time!

This repository contains a collection of wallpapers categorized into Light, Dark, Mountain-Light, Mountain-Dark, and Mountain-Sunset themes. 

The `BetterWallpaperByTime.py` Python program is designed to randomly change the wallpaper based on the time of day, using the Nitrogen application on Linux window systems.

## Installation

Start by installing Nitrogen if you're using a Linux distribution. Additionally, ensure you have Python 3 or above installed.
check:- [nitrogen](https://github.com/l3ib/nitrogen) for more info

```bash
# Install Nitrogen
sudo apt install nitrogen #For ubuntu
sudo pacman -S nitrogen #For Arch and arch like os

# Clone the repository
git clone https://github.com/bigbuny/BetterWallpaperByTime.git
cd BetterWallpaperByTime
```

## Usage:
```
usage: BetterWallpaperByTime.py [-h] [--MODE MODE] [--TIMER TIMER] [--FOLDER_PATH FOLDER_PATH]

options:
  -h, --help            show this help message and exit
  --MODE MODE           Specify the mode (Possible-modes:- (1) wall_on_start )
  --TIMER TIMER         Specify the timer duration in only float datatype
  --FOLDER_PATH FOLDER_PATH
                        Specify the FOLDER_PATH of the git repository in your system

```

You can run this forever in the particular X Window System by starting it in you're `.xinitrc`, for KDE-plasma or for GNOME or any other desktop linux Window systems, start by creating a desktop entry in `~/.config/autostart`.

X window System;- (add this line before `exec YouTilingWindowManager`)

```
python3 Pictures/dt/wallpapers/BetterWallpaperByTime.py --MODE=wall_on_start --TIMER=1800
```

Desktop Window System;-

```
[Desktop Entry]
Type=Application
Name=MyApplication
Exec=/wallpapers_/BetterWallpaperByTime.py wall_on_start
```

Wallpaper Source: [https://gitlab.com/dwt1/wallpapers](https://gitlab.com/dwt1/wallpapers)
