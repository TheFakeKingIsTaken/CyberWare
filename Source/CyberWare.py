import os
os.system("title CyberWare")

import MessageScan 
import ThemePicker as ThemePicker

from colored import fg

#Data to be changes later on
Verison      =None
Verison_Tpye =None

Theme        =None

#green  = info
#blue   = info but better
#red    = visuals like walls
#white  = visuals 
#yellow = CyberWare Info and just info

white   =fg("white")
red     =fg("red")
yellow  =fg("yellow")
blue    =fg("blue")
green   =fg("green")

#Loads UserData
from configparser import ConfigParser

Config = ConfigParser()
Config.read("Data.ini")


Start = True

try:
    #MAIN DATA
    Verison      = Config["MAIN DATA"]["Verison"]
    Verison_Tpye = Config["MAIN DATA"]["Verison_Tpye"]

    #THEME DATA
    Theme = Config["THEME DATA"]["Theme"]

    if Theme == "default":
        white   =fg("white")
        red     =fg("red")
        yellow  =fg("yellow")
        blue    =fg("blue")
        green   =fg("green")
    elif Theme == "Water":
        white   =fg("white")
        red     =fg("blue")
        yellow  =fg("green")
        blue    =fg("blue")
        green   =fg("blue")
    elif Theme == "Lava":
        white   =fg("white")
        red     =fg("red")
        yellow  =fg("yellow")
        blue    =fg("yellow")
        green   =fg("red")
    elif Theme == "Grass":
        white   =fg("white")
        red     =fg("green")
        yellow  =fg("yellow")
        blue    =fg("green")
        green   =fg("green")
except:
    #creates errorlog
    with open("ErrorLog.txt","w") as FILE:
        FILE.write(f'''[ERROR LOG]\n            
|->BASEDATA<-|
Verison: {Verison}
Verison_Tpye: {Verison_Tpye}

Theme: {Theme}

-LOG-
Couldent load settings for unknown reason
''')    
        DataList =[]#list of items that didnt load
        if Verison == None:DataList.append("Verison")
        if Verison_Tpye == None:DataList.append("VerisonTpye")
        if Theme == None:DataList.append("Theme")

        FILE.write(f"\nCouldent load items listed below\n{DataList}\n")


        FILE.write("""\n|->Cause<-|
Data files most likey deleted or invaild""")



    os.system("title CyberWare [NO DATA]")

    #TEMP COLORS
    red     =fg("red")
    green   =fg("green")
    white   =fg("white")

    print(f"{red}Couldent Find Data\nplease reinstall CyberWare or repair messing Data files\nfor more info check the ErrorLog.txt File in path\n   <{os.getcwd()}\ErrorLog.txt>\n\nError[001]")
    Start = False

    print(f"\nOpen {green}ErrorLog.txt?{white} [{green}y{white}/{red}n{white}]")
    InputData = input()

    if InputData == "y" or "ye" or "yes":
        os.system("title CyberWare [NO DATA] (Opening Errorlog.txt)")
        os.system(f'start {os.getcwd()}\ErrorLog.txt')








#main loop
def MainMenu():
    os.system("cls")
    print(f"""{blue}
                     ▄████▄ ▓██   ██▓ ▄▄▄▄    ▓█████ ██▀███   ██     ██░ ▄▄▄      ██▀███   ▓█████
                    ▒██▀ ▀█  ▒██  ██▒▓█████▄  ▓█   ▀▓██ ▒ ██▒▓██░ ██ ░██░▒████▄   ▓██ ▒ ██▒ ▓█   ▀
                    ▒▓█    ▄  ▒██ ██░▒██▒ ▄██ ▒████ ▓██ ░▄█ ▒▒██░ ██ ░██ ▒██  ▀█▄ ▓██ ░▄█ ▒ ▒████  
                    ▒▓▓▄ ▄██  ░ ▐██▓░▒██░█▀   ▒▓█  ▄▒██▀▀█▄  ░██░ ██ ░██ ░██▄▄▄▄██▒██▀▀█▄   ▒▓█  ▄
                     ▓███▀    ░ ██▒▓░░▓█  ▀█▓▒░▒████░██▓ ▒██▒░░█████▓██  ▓█     ██ ██▓ ▒██▒▒░▒████
                    ░ ░▒ ▒     ██▒▒▒ ░▒▓███▀▒░░░ ▒░ ░ ▒▓ ░▒▓░░ ▓░▒ ▒  ░▒▒▓▒█░    ▒▓ ░▒▓░░░░ ▒░ 
                    ░  ▒     ▓██░▒░ ▒░▒   ░ ░ ░ ░    ░▒ ░ ▒   ▒ ░ ░  ░ ░   ▒▒   ░▒ ░ ▒ ░ ░ ░  
                    ░        ▒ ▒ ░░   ░    ░     ░    ░░   ░   ░   ░    ░   ▒    ░░   ░     ░  
                    ░ ░      ░ ░      ░      ░   ░     ░         ░          ░     ░     ░   ░  {white}

{red}|=====================================================[{green}Helpful Commands{red}]===============================================|{white}

        <{green}help{white}>{yellow}Gives a little info on how to use CyberWare also gives the user a link to the CyberWare Docs{white}
        
        <{green}exit{white}>{yellow}Exits the software{white}                                

        <{green}theme{white}>{yellow}Lets the user change the CyberWare theme{white}

        <{green}more{white}>{yellow}Shows more Commands{white}
        
{red}|======================================================[{green}Main Commands{red}]=================================================|{white}
        
        <{blue}1{white}>{yellow}Message Scaning{white}
                           
{red}|======================================================[{green}CyberWare Info{red}]================================================|{white}
{yellow}Theme{white}[{blue}{Theme}{white}]
{yellow}Verison{white}[{green}{Verison}{white}]
{red}|======================================================================================================================|{white}
""")



    UserInput = input(f"<{green}User{white}>")#checks for a command if command not vaild command outputs an error

    if UserInput == "help":#gives info about CyberWare and gives users link to CyberWare github docs
        print(f"{green}CyberWare is a open Source {white}exploit prevention{green} software\nthis software helps you {white}prevent{green} being {white}hacked {green}or{white} exploited{green}\ngo to the doc for more info on CyberWare and how to use it\n      <{yellow}https://github.com/TheFakeKingIsTaken/CyberWare/blob/main/Documentation/Dictionrary.md{green}>{white}")
        input()
    elif UserInput == "exit": #leaves the program:
        raise SystemError
    elif UserInput == "theme":#opens theme editer
        
        ThemePicker.PickTheme()
        os.system("title CyberWare")
    elif UserInput == "1":#opens scaning menu
        MessageScan.Menu(white,yellow,red,green,blue)
    elif UserInput == "restart":#restarts cyberware
        os.system(f'start {os.getcwd()}\CyberWare.exe') #note to self change this to .EXE
        raise SystemError  
    elif UserInput == "more":#shows more info
        os.system("cls")
        print(f"""{blue}
                     ▄████▄ ▓██   ██▓ ▄▄▄▄    ▓█████ ██▀███   ██     ██░ ▄▄▄      ██▀███   ▓█████
                    ▒██▀ ▀█  ▒██  ██▒▓█████▄  ▓█   ▀▓██ ▒ ██▒▓██░ ██ ░██░▒████▄   ▓██ ▒ ██▒ ▓█   ▀
                    ▒▓█    ▄  ▒██ ██░▒██▒ ▄██ ▒████ ▓██ ░▄█ ▒▒██░ ██ ░██ ▒██  ▀█▄ ▓██ ░▄█ ▒ ▒████  
                    ▒▓▓▄ ▄██  ░ ▐██▓░▒██░█▀   ▒▓█  ▄▒██▀▀█▄  ░██░ ██ ░██ ░██▄▄▄▄██▒██▀▀█▄   ▒▓█  ▄
                     ▓███▀    ░ ██▒▓░░▓█  ▀█▓▒░▒████░██▓ ▒██▒░░█████▓██  ▓█     ██ ██▓ ▒██▒▒░▒████
                    ░ ░▒ ▒     ██▒▒▒ ░▒▓███▀▒░░░ ▒░ ░ ▒▓ ░▒▓░░ ▓░▒ ▒  ░▒▒▓▒█░    ▒▓ ░▒▓░░░░ ▒░ 
                    ░  ▒     ▓██░▒░ ▒░▒   ░ ░ ░ ░    ░▒ ░ ▒   ▒ ░ ░  ░ ░   ▒▒   ░▒ ░ ▒ ░ ░ ░  
                    ░        ▒ ▒ ░░   ░    ░     ░    ░░   ░   ░   ░    ░   ▒    ░░   ░     ░  
                    ░ ░      ░ ░      ░      ░   ░     ░         ░          ░     ░     ░   ░  {white}
{red}|======================================================[{green}More Commands{red}]=================================================|{white}

        <{green}restart{white}>{yellow}Restarts CyberWare{white}

{red}|======================================================================================================================|{white}
""")
        input(f"{blue}<Press anything to go back>{white}")
    else:
        print(f"{red}[Invaild Command]{white}")
        input()
        
    os.system("title CyberWare")
    MainMenu()
    



if Start:
    MainMenu()