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
        
        parser.add_argument('--MODE', type=str, default='', help='Specify the mode (Possible-modes:- \n (1) wall_on_start  )')
        parser.add_argument('--TIMER', type=float, default=None, help='Specify the timer duration in only float datatype')
        parser.add_argument('--FOLDER_PATH', type=str, default='/wallpapers_/',help='Specify the FOLDER_PATH of the git repository in your system')
    
        self.args = parser.parse_args() 
        self.full_folder_path = full_folder_path + self.args.FOLDER_PATH
        self.arg_ = (self.args.MODE, self.args.TIMER)
    def GetDarkThemes(self):
        self.DarkThemes_path = self.full_folder_path+"Dark-themes/"
        self.DarkThemes_files = subprocess.getoutput(f"ls {self.DarkThemes_path}")
        
        self.DarkThemes_list = self.DarkThemes_files.split()
        # for b in range(len(self.DarkThemes_list)):
        #     item_b = list(self.DarkThemes_list[b])
        #     item_b = item_b[:-4]
        #     self.DarkThemes_list[b] = ''.join(item_b)
        return self.DarkThemes_list
    def GetLightThemes(self):
        self.LightThemes_path = self.full_folder_path+"Light-themes/"
        self.LightThemes_files = subprocess.getoutput(f"ls {self.LightThemes_path}")
        
        self.LightThemes_list = self.LightThemes_files.split()
        # for c in range(len(self.LightThemes_list)):
        #     item_c = list(self.LightThemes_list[c])
        #     item_c = item_c[:-4]
        #     self.LightThemes_list[c] = ''.join(item_c)

        return self.LightThemes_list
    def MountainLightThemes(self):
        self.MlightThemes_path = self.full_folder_path+"Mountain_nature_kinda/Mountain_light"
        self.MlightThemes_files = subprocess.getoutput(f"ls {self.MlightThemes_path}")
        
        self.MlightThemes_list = self.MlightThemes_files.split()
        # for d in range(len(self.MlightThemes_list)):
        #     item_d = list(self.MlightThemes_list[d])
        #     item_d = item_d[:-4]
        #     self.MlightThemes_list[d] = ''.join(item_d)

        return self.MlightThemes_list
    def MountainDarkThemes(self):
        self.MdarkThemes_path = self.full_folder_path+"Mountain_nature_kinda/Mountain_dark"
        self.MdarkThemes_files = subprocess.getoutput(f"ls {self.MdarkThemes_path}")
        
        self.MdarkThemes_list = self.MdarkThemes_files.split()
        # for e in range(len(self.MdarkThemes_list)):
        #     item_e = list(self.MdarkThemes_list[e])
        #     item_e = item_e[:-4]
        #     self.MdarkThemes_list[e] = ''.join(item_e)

        return self.MdarkThemes_list
    def MountainSunsetThemes(self):
        self.MSUNThemes_path = self.full_folder_path+"Mountain_nature_kinda/mountain_sunset"
        self.MSUNThemes_files = subprocess.getoutput(f"ls {self.MSUNThemes_path}")
        
        self.MSUNThemes_list = self.MSUNThemes_files.split()
        # for f in range(len(self.MSUNThemes_list)):
        #     item_f = list(self.MSUNThemes_list[f])
        #     item_f = item_f[:-4]
        #     self.MSUNThemes_list[f] = ''.join(item_f)

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
                os.system('nitrogen --set-zoom-fill '+'/home/Akash/Pictures/dt/wallpapers/Mountain_nature_kinda/mountain_sunset/'+self.Msunran_image)
                self.Wallpaper_Changed = True
                with open('log.txt','a') as log:
                    log.write(f'Updated the wall {self.Msunran_image} (Msunset) on {datetime.datetime.now()}  \n')
            elif self.get_time_period() == "Noon":
                ksfja=random.randint(0,1)
                if ksfja == 0:
                    os.system('nitrogen --set-zoom-fill '+'/home/Akash/Pictures/dt/wallpapers/Mountain_nature_kinda/Mountain_light/'+self.MlightThemeran_image)
                    self.Wallpaper_Changed = True
                    with open('log.txt','a') as log:
                        log.write(f'Updated the wall {self.MlightThemeran_image} (Mlight) on {datetime.datetime.now()} \n')
                elif ksfja == 1:
                    os.system('nitrogen --set-zoom-fill '+'/home/Akash/Pictures/dt/wallpapers/Light-themes/'+self.lightThemeran_image)
                    self.Wallpaper_Changed = True
                    with open('log.txt','a') as log:
                        log.write(f'Updated the wall {self.lightThemeran_image} (Light) on {datetime.datetime.now()} \n')
            elif self.get_time_period() == "Night":
                ksfja=random.randint(0,1)
                if ksfja == 0:
                    os.system('nitrogen --set-zoom-fill '+'/home/Akash/Pictures/dt/wallpapers/Mountain_nature_kinda/Mountain_dark/'+self.MdarkThemeran_image)
                    self.Wallpaper_Changed = True
                    with open('log.txt','a') as log:
                        log.write(f'Updated the wall {self.MdarkThemeran_image} (Mdark) on {datetime.datetime.now()} \n')
                elif ksfja == 1:
                    os.system('nitrogen --set-zoom-fill '+'/home/Akash/Pictures/dt/wallpapers/Dark-themes/'+self.darkThemeran_image)
                    self.Wallpaper_Changed = True
                    with open('log.txt','a') as log:
                        log.write(f'Updated the wall {self.darkThemeran_image} (Dark) on {datetime.datetime.now()} \n')
    def UpdateWall(self):
        self.mode, self.timer = self.arg_
        if self.mode == "wall_on_start":
            if self.count == 0:
                self.SetWall()
                self.count += 1
        if self.Wallpaper_Changed:
            if self.timer == None:
                time.sleep(1800)
                self.SetWall()
            else:
                time.sleep(self.timer)
                self.SetWall()
        else:
            print("something went wrong somewhere! :(")
if __name__ == "__main__":
    main_Instance = Main()
    while True:
        main_Instance.UpdateWall()
        if main_Instance.Wallpaper_Changed == False:
            break
