import os
import subprocess
import random
import time
import datetime
import argparse

class Main:
    def __init__(self, full_folder_path=os.path.expanduser("~"), random_walls=False):
        self.random_walls = random_walls
        self.count = 0
        self.Wallpaper_Changed = False
        parser = argparse.ArgumentParser()

        # parser.add_argument('--MODE', type=str, default='', help='Specify the mode (Possible-modes:- \n (1) wall_on_start  )')
        # parser.add_argument('--TIMER', type=float, default=None, help='Specify the timer duration in only float datatype')
        parser.add_argument('--FOLDER_PATH', type=str, default='/Pictures/dt/wallpapers/',help='Specify the FOLDER_PATH of the git repository in your system')

        self.args = parser.parse_args()
        self.full_folder_path = full_folder_path + self.args.FOLDER_PATH
        # self.arg_ = (self.args.MODE, self.args.TIMER)
    def GetDarkThemes(self):
        self.DarkThemes_path = self.full_folder_path+"Dark-themes/"
        self.DarkThemes_files = subprocess.getoutput(f"ls {self.DarkThemes_path}")

        self.DarkThemes_list = self.DarkThemes_files.split()
        return self.DarkThemes_list
    def GetLightThemes(self):
        self.LightThemes_path = self.full_folder_path+"Light-themes/"
        self.LightThemes_files = subprocess.getoutput(f"ls {self.LightThemes_path}")

        self.LightThemes_list = self.LightThemes_files.split()

        return self.LightThemes_list
    def MountainLightThemes(self):
        self.MlightThemes_path = self.full_folder_path+"Mountain_nature_kinda/Mountain_light"
        self.MlightThemes_files = subprocess.getoutput(f"ls {self.MlightThemes_path}")

        self.MlightThemes_list = self.MlightThemes_files.split()

        return self.MlightThemes_list
    def MountainDarkThemes(self):
        self.MdarkThemes_path = self.full_folder_path+"Mountain_nature_kinda/Mountain_dark"
        self.MdarkThemes_files = subprocess.getoutput(f"ls {self.MdarkThemes_path}")

        self.MdarkThemes_list = self.MdarkThemes_files.split()

        return self.MdarkThemes_list
    def MountainSunsetThemes(self):
        self.MSUNThemes_path = self.full_folder_path+"Mountain_nature_kinda/mountain_sunset"
        self.MSUNThemes_files = subprocess.getoutput(f"ls {self.MSUNThemes_path}")

        self.MSUNThemes_list = self.MSUNThemes_files.split()

        return self.MSUNThemes_list
    def GetRandomNumber(self, function_):
        self.GetList_ = function_()
        self.RandomInt = random.randint(0,len(self.GetList_))
        try:
            return self.GetList_[self.RandomInt]
        except IndexError:
            return self.GetList_[random.randint(0,10)]

    def Main(self):
        return [
                self.GetRandomNumber(self.GetLightThemes),
                self.GetRandomNumber(self.GetDarkThemes),
                self.GetRandomNumber(self.MountainDarkThemes),
                self.GetRandomNumber(self.MountainLightThemes),
                self.GetRandomNumber(self.MountainSunsetThemes)
        ]

    def get_time_period(self, current_time=datetime.datetime.now()):
        hour = current_time.hour
        if 5 <= hour < 10:
            return "Sunrise"
        elif 10 <= hour < 17:
            return "Noon"
        elif 17 <= hour < 19:
            return "Sunset"
        else:
            return "Night"
    def SetWall(self):
        self.image_list = self.Main()

        self.MdarkThemeran_image = self.image_list[2]
        self.darkThemeran_image = self.image_list[1]
        self.MlightThemeran_image = self.image_list[3]
        self.lightThemeran_image = self.image_list[0]
        self.Msunran_image = self.image_list[-1]

        if self.random_walls == False:
            if self.get_time_period() == "Sunrise" or self.get_time_period() == "Sunset":
                os.system('betterlockscreen -u '+'/home/Akash/Pictures/dt/wallpapers/Mountain_nature_kinda/mountain_sunset/'+self.Msunran_image)
                self.Wallpaper_Changed = True
                with open('log_lock.txt','a') as log_lock:
                    log_lock.write(f'Updated The Lockscreen Wall {self.Msunran_image} (Msunset) on {datetime.datetime.now()}  \n')
            elif self.get_time_period() == "Noon":
                ksfja=random.randint(0,1)
                if ksfja == 0:
                    os.system('betterlockscreen -u '+'/home/Akash/Pictures/dt/wallpapers/Mountain_nature_kinda/Mountain_light/'+self.MlightThemeran_image)
                    self.Wallpaper_Changed = True
                    with open('log_lock.txt','a') as log_lock:
                        log_lock.write(f'Updated The Lockscreen Wall {self.MlightThemeran_image} (Mlight) on {datetime.datetime.now()} \n')
                elif ksfja == 1:
                    os.system('betterlockscreen -u '+'/home/Akash/Pictures/dt/wallpapers/Light-themes/'+self.lightThemeran_image)
                    self.Wallpaper_Changed = True
                    with open('log_lock.txt','a') as log_lock:
                        log_lock.write(f'Updated The Lockscreen Wall {self.lightThemeran_image} (Light) on {datetime.datetime.now()} \n')
            elif self.get_time_period() == "Night":
                ksfja=random.randint(0,1)
                if ksfja == 0:
                    os.system('betterlockscreen -u '+'/home/Akash/Pictures/dt/wallpapers/Mountain_nature_kinda/Mountain_dark/'+self.MdarkThemeran_image)
                    self.Wallpaper_Changed = True
                    with open('log_lock.txt','a') as log_lock:
                        log_lock.write(f'Updated The Lockscreen Wall {self.MdarkThemeran_image} (Mdark) on {datetime.datetime.now()} \n')
                elif ksfja == 1:
                    os.system('betterlockscreen -u '+'/home/Akash/Pictures/dt/wallpapers/Dark-themes/'+self.darkThemeran_image)
                    self.Wallpaper_Changed = True
                    with open('log_lock.txt','a') as log_lock:
                        log_lock.write(f'Updated The Lockscreen Wall {self.darkThemeran_image} (Dark) on {datetime.datetime.now()} \n')
if __name__ == "__main__":
    main_Instance = Main()
    main_Instance.SetWall()

