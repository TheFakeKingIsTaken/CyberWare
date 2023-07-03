import os
import time

from colored import fg

white   =fg("white")
red     =fg("red")
yellow  =fg("yellow")
blue    =fg("blue")
green   =fg("green")

from configparser import ConfigParser

Config = ConfigParser()
Config.read("Data.ini")


def PickTheme():#theme picker
    os.system("title CyberWare (Picking Theme)")

    start = True
    CurrentTheme = 1
    while start:
        os.system("cls")
        print(f"""{green}████████╗██╗  ██╗███████╗███╗   ███╗███████╗    ██████╗ ██╗ ██████╗██╗  ██╗███████╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝████╗ ████║██╔════╝    ██╔══██╗██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   ███████║█████╗  ██╔████╔██║█████╗      ██████╔╝██║██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██╔══██║██╔══╝  ██║╚██╔╝██║██╔══╝      ██╔═══╝ ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ██║  ██║███████╗██║ ╚═╝ ██║███████╗    ██║     ██║╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝    ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                      
{white}
{red}|======================================================================================================================|\n{white}""")
        
        if CurrentTheme == 1:
            print(f"""{white}██████╗ ███████╗███████╗ █████╗ ██╗   ██╗██╗     ████████╗
██╔══██╗██╔════╝██╔════╝██╔══██╗██║   ██║██║     ╚══██╔══╝
██║  ██║█████╗  █████╗  ███████║██║   ██║██║        ██║   
██║  ██║██╔══╝  ██╔══╝  ██╔══██║██║   ██║██║        ██║   
██████╔╝███████╗██║     ██║  ██║╚██████╔╝███████╗   ██║   
╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   """)
        if CurrentTheme == 2:  
            print(f"""{blue}                           ██                   
                           ██                   
▀██▀    ▄█    ▀██▀▄█▀██▄ ██████  ▄▄█▀██▀███▄███ 
  ██   ▄███   ▄█ ██   ██   ██   ▄█▀   ██ ██▀ ▀▀ 
   ██ ▄█  ██ ▄█   ▄███▓█   ██   ▓█▀▀▀▀▀▀ █▓     
    ███    █▓▓   █▓   ▓█   █▓   ▓█▄    ▄ █▓     
    ▓█▓▓   ▓▒▓    ▓▓▓▓▒▓   ▓▓   ▓▓▀▀▀▀▀▀ ▓▓     
    ▓▓▓    ▓▒▓   ▓▓   ▒▓   ▓▓   ▒▓▓      ▓▒     
     ▒      ▒    ▒▓▒ ▒ ▓▒  ▒▒▒ ▒ ▒ ▒ ▒▒▒ ▒▒▒                                                
{white}""")
        if CurrentTheme == 3:
            print(f"""{red}      ██▓    ▄▄▄      ██▒   █▓ ▄▄▄{yellow}       
     ▓██▒   ▒████▄   ▓██░   █▒▒████▄      
     {red}▒██░   ▒██  ▀█▄  ▓██  █▒░▒██  ▀█▄{yellow}     
     ▒██░   ░██▄▄▄▄██  ▒██ █░░░██▄▄▄▄██    
    {red}▒░██████▒▓█   ▓██   ▒▀█░  ▒▓█   ▓██{yellow}   
    {red}░░ ▒░▓  ░▒▒   ▓▒█   ░ ▐░  ░▒▒   ▓▒█    
    ░░ ░ ▒  ░ ░   ▒▒    ░ ░░  ░ ░   ▒▒{yellow}   
    {red}   ░ ░    ░   ▒        ░    ░   ▒{yellow}      
    ░    ░        ░        ░        ░""")
        if CurrentTheme == 4:
            print(f"""{green}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒     ▒▒▒  ▒    ▒▒▒▒   ▒▒▒▒▒▒     ▒▒▒     ▒
▓   ▓▓   ▓▓   ▓▓▓▓▓   ▓▓   ▓▓   ▓▓▓▓▓   ▓▓▓▓
▓  ▓▓▓   ▓▓   ▓▓▓▓   ▓▓▓   ▓▓▓▓    ▓▓▓▓    ▓
▓    ▓   ▓▓   ▓▓▓▓   ▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓   
█████   ██    ██████   █    █      ██      █
███    █████████████████████████████████████
{white}""") 
       
        print(f"""{red}\n|======================================================================================================================|\n{white}""")
        UserInput = input(f"<{yellow}Set As Theme {white}[{green}y{white}]>:<{yellow}Input back to go back to Main Menu{white}>\n<{blue}ThemeID{red}:{green}{CurrentTheme}{white}>")
        if UserInput == "y" or UserInput == "ye" or UserInput == "yes":
            if CurrentTheme == 1:
                Config["THEME DATA"]["Theme"] = ""
                with open("Data.ini","w") as FILE:
                    FILE.write("""[MAIN DATA]
Verison = 0.0.1
Verison_Tpye = CyberWare-Main

[THEME DATA]
Theme = default

[RANDOM THEME DATA]
white  =None
blue   =None
red    =None
green  =None
yellow =None""")
                
            if CurrentTheme == 2:
                    Config["THEME DATA"]["Theme"] = ""
                    with open("Data.ini","w") as FILE:
                        FILE.write("""[MAIN DATA]
Verison = 0.0.1
Verison_Tpye = CyberWare-Main

[THEME DATA]
Theme = Water

[RANDOM THEME DATA]
white  =None
blue   =None
red    =None
green  =None
yellow =None""")
                                    
                    
            if CurrentTheme == 2:
                    Config["THEME DATA"]["Theme"] = ""
                    with open("Data.ini","w") as FILE:
                        FILE.write("""[MAIN DATA]
Verison = 0.0.1
Verison_Tpye = CyberWare-Main

[THEME DATA]
Theme = Water

[RANDOM THEME DATA]
white  =None
blue   =None
red    =None
green  =None
yellow =None""")
                                    
                    
            if CurrentTheme == 3:
                    Config["THEME DATA"]["Theme"] = ""
                    with open("Data.ini","w") as FILE:
                        FILE.write("""[MAIN DATA]
Verison = 0.0.1
Verison_Tpye = CyberWare-Main

[THEME DATA]
Theme = Lava

[RANDOM THEME DATA]
white  =None
blue   =None
red    =None
green  =None
yellow =None""")
                                    
                    
            if CurrentTheme == 4:
                    Config["THEME DATA"]["Theme"] = ""
                    with open("Data.ini","w") as FILE:
                        FILE.write("""[MAIN DATA]
Verison = 0.0.1
Verison_Tpye = CyberWare-Main

[THEME DATA]
Theme = Grass

[RANDOM THEME DATA]
white  =None
blue   =None
red    =None
green  =None
yellow =None""")  


            os.system(f'start {os.getcwd()}\CyberWare.exe')  #note to self change this to .EXE
            raise SystemError            
        if UserInput == "back":
            return
        CurrentTheme += 1

        if CurrentTheme > 4:
            CurrentTheme = 1


