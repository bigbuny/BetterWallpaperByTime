import os
import subprocess
import random
import time
import datetime
import sys

class Main:
    def __init__(self, full_folder_path=os.path.expanduser("~") + "/Pictures/dt/wallpapers/", random_walls=False):
        self.random_walls = random_walls
        self.full_folder_path = full_folder_path
        self.arg_ = sys.argv
        self.Wallpaper_Changed_Time = datetime.datetime.now()
        self.count = 0
    def GetUnClassified(self):
        self.UnClassified_path = self.full_folder_path+"Un-classified/"
        self.UnClassified_files = subprocess.getoutput(f"ls {self.UnClassified_path}")
        
        self.Unclassified_list = self.UnClassified_files.split()
        for a in range(len(self.Unclassified_list)):
            item_a = list(self.Unclassified_list[a])
            item_a = item_a[:-4]
            self.Unclassified_list[a] = int(''.join(item_a))

        return self.Unclassified_list
    def GetDarkThemes(self):
        self.DarkThemes_path = self.full_folder_path+"Dark-themes/"
        self.DarkThemes_files = subprocess.getoutput(f"ls {self.DarkThemes_path}")
        
        self.DarkThemes_list = self.DarkThemes_files.split()
        for b in range(len(self.DarkThemes_list)):
            item_b = list(self.DarkThemes_list[b])
            item_b = item_b[:-4]
            self.DarkThemes_list[b] = ''.join(item_b)

        return self.DarkThemes_list
    def GetLightThemes(self):
        self.LightThemes_path = self.full_folder_path+"Light-themes/"
        self.LightThemes_files = subprocess.getoutput(f"ls {self.LightThemes_path}")
        
        self.LightThemes_list = self.LightThemes_files.split()
        for c in range(len(self.LightThemes_list)):
            item_c = list(self.LightThemes_list[c])
            item_c = item_c[:-4]
            self.LightThemes_list[c] = ''.join(item_c)

        return self.LightThemes_list
    def MountainLightThemes(self):
        self.MlightThemes_path = self.full_folder_path+"Mountain_nature_kinda/Mountain_light"
        self.MlightThemes_files = subprocess.getoutput(f"ls {self.MlightThemes_path}")
        
        self.MlightThemes_list = self.MlightThemes_files.split()
        for d in range(len(self.MlightThemes_list)):
            item_d = list(self.MlightThemes_list[d])
            item_d = item_d[:-4]
            self.MlightThemes_list[d] = ''.join(item_d)

        return self.MlightThemes_list
    def MountainDarkThemes(self):
        self.MdarkThemes_path = self.full_folder_path+"Mountain_nature_kinda/Mountain_dark"
        self.MdarkThemes_files = subprocess.getoutput(f"ls {self.MdarkThemes_path}")
        
        self.MdarkThemes_list = self.MdarkThemes_files.split()
        for e in range(len(self.MdarkThemes_list)):
            item_e = list(self.MdarkThemes_list[e])
            item_e = item_e[:-4]
            self.MdarkThemes_list[e] = ''.join(item_e)

        return self.MdarkThemes_list
    def MountainSunsetThemes(self):
        self.MSUNThemes_path = self.full_folder_path+"Mountain_nature_kinda/mountain_sunset"
        self.MSUNThemes_files = subprocess.getoutput(f"ls {self.MSUNThemes_path}")
        
        self.MSUNThemes_list = self.MSUNThemes_files.split()
        for f in range(len(self.MSUNThemes_list)):
            item_f = list(self.MSUNThemes_list[f])
            item_f = item_f[:-4]
            self.MSUNThemes_list[f] = ''.join(item_f)

        return self.MSUNThemes_list
    def GetRandomNumber(self, function_):
        self.GetList_ = function_()
        self.RandomInt = random.randint(0,len(self.GetList_))
        try:
            return self.GetList_[self.RandomInt]
        except IndexError:
            return self.GetList_[random.randint(0,1)]
    
    def Main(self):
        return [        
                self.GetRandomNumber(self.GetUnClassified),
                self.GetRandomNumber(self.GetLightThemes),
                self.GetRandomNumber(self.GetDarkThemes),
                self.GetRandomNumber(self.MountainDarkThemes),
                self.GetRandomNumber(self.MountainLightThemes),
                self.GetRandomNumber(self.MountainSunsetThemes)
        ]

    def get_time_period(self, current_time=datetime.datetime.now()):
        hour = current_time.hour
        if 6 <= hour < 10:
            return "Sunrise"
        elif 10 <= hour < 17:
            return "Noon"
        elif 17 <= hour < 20:
            return "Sunset"
        else:
            return "Night"

    def FindMood_and_SetWall(self):
        self.image_list = self.Main()
        #case Un-classified
        if self.image_list[1] == '326':
            self.unclassifiedran_image = self.image_list[1] + '.png'
        else:
            self.unclassifiedran_image = self.image_list[1] + '.jpg'
        if self.image_list[2] == '344':
            self.MdarkThemeran_image = self.image_list[3] + '.png'
        else:
            self.MdarkThemeran_image = self.image_list[3] + '.jpg'
        self.darkThemeran_image = self.image_list[2] + '.jpg'
        self.MlightThemeran_image = self.image_list[4] + '.jpg'
        self.lightThemeran_image = self.image_list[1] + '.jpg'
        self.Msunran_image = self.image_list[-1] + '.jpg' 
        if self.random_walls == False:
            if self.get_time_period(self.Wallpaper_Changed_Time) == "Sunrise" or self.get_time_period(self.Wallpaper_Changed_Time) == "Sunset":
                os.system('nitrogen --set-zoom-fill '+os.path.expanduser("~")+'/Pictures/dt/wallpapers/Mountain_nature_kinda/mountain_sunset/'+self.Msunran_image)
            elif self.get_time_period(self.Wallpaper_Changed_Time) == "Noon":
                ksfja=random.randint(0,1)
                if ksfja == 0:
                    os.system('nitrogen --set-zoom-fill '+os.path.expanduser("~")+'/Pictures/dt/wallpapers/Mountain_nature_kinda/Mountain_light/'+self.MlightThemeran_image)
                elif ksfja == 1:
                    os.system('nitrogen --set-zoom-fill '+os.path.expanduser("~")+'/Pictures/dt/wallpapers/Light-themes/'+self.lightThemeran_image)
            elif self.get_time_period(self.Wallpaper_Changed_Time) == "Night":
                ksfja=random.randint(0,1)
                if ksfja == 0:
                    os.system('nitrogen --set-zoom-fill '+os.path.expanduser("~")+'/Pictures/dt/wallpapers/Mountain_nature_kinda/Mountain_dark/'+self.MdarkThemeran_image)
                elif ksfja == 1:
                    os.system('nitrogen --set-zoom-fill '+os.path.expanduser("~")+'/Pictures/dt/wallpapers/Dark-themes/'+self.darkThemeran_image)
    def UpdateWall(self):
        if self.arg_[1] == 'wall_on_start':
            if self.count == 0:
                self.FindMood_and_SetWall()
                self.count += 1
        time.sleep(1800)
        self.FindMood_and_SetWall()
if __name__ == "__main__":
    main_Instance = Main()
    while True:
        main_Instance.UpdateWall()
