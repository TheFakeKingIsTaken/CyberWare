import threading
import os
import time
import random
import math 

BasicFlagedKeyWords = [ 
    ["ip",2],
    ["hack",1],
    ["hacked",1],
    ["Cyber",0.1],
    ["cyber",0.1],
    ["cyberware",2],
    ["turn off anti",6],
    ["dont turn on anti",4],
    ["virus",2],
    ["antivirus",5],
    ["play my game",2],
    ["hey can you play my game",4],
    ["play my game file",7],
    ["its a file",11],
    ["file",2],
    ["exe",6],
    [".jar",3],
    [".bat",13],
    ["batch file",13],
    ["batch",13],
    ["python file",8],
    ["safe file",4],
    ["this file safe",7],
    ["trust me the file is safe",4],
    ["trust me file safe",14],
    [".jar isent .exe",16],
    ["exe is safe",20],
    ["hey play my game click the link",5],
    ["click the link",3],
    ["bro click the link",4],
    ["heres the link its safe",8],
    ["download this file its safe",12],
    ["download file",3],
    ["file download",3],
    ["download exe",12],
    ["download .jar",10],
    ["download .exe",14],
    ["run it",3],
    ["run exe",5],
    ["run .jar",3],
    ["run jar file",3],
    ["run .exe",7],
    ["its free",5],
    ["free robux",4],
    ["free money",5],
    ["free cash",10],
    ["FREEE",0.3],
    ["paypal",10],
    ["debit",10],
    ["credit card",10],
    ["password",10],
    ["username",0.4],
    ["gmail",4],
    ["give gmail",4],
    ["i need your gmail",6],
    ["can i have your gmail",4],
    ["give me your password",3.5],
    ["can i have your password",3.5],
    ["pass",1],
    ["can i have your pass",3.5],
    ["give me your pass",3.5],
    ["handle",0.3],
    ["give yor handle",0.3],
    ["login to your",0.2],
    ["token",3],
    ["discord token",20],
    ["give discord token",20],
    ["can i have discord token",20],
    ["i really need your discord token",20],
    ["give me your handle and i wont",10],
    ["give me your password and i wont",20],
    ["give me your token and i wont",20],
    ["give me your file and i wont",20],
    ["flies",1],
    ["download the files",4],
    ["give files",2],
    ["run files",3],
    ["it has files",1],
    ["give me your data",1],
    ["data",0.1],
    ["can i have that data",0.4],
    ["i need that data",0.6],
    ["yo can you play my game",4],
    ["yo give me that data",0.6],
    ["yo give me some data",0.6],
    ["i need some data",0.6],
    ["download this",3],
    ["its a not virus",12],
    ["your antivirus thinks",20],
    ["your antvirus thinks its a virus",20],
    ["put this file in here",0.4],
    ["put the file there",0.5],
    ["put the file",0.4],
    ["install",6],
    ["install that",2],
    ["can you install this",4],
    ["install this",3],
    ["yo install this app",0.8],
    ["install please",2],
    ["to do this you most install this",0.7],
    ["install the app before the time is up",1],
    ["install please",1],
    ["its safe dont worry",14],
    ["we need play testers",10],
    ["i need play testers",10],
    ["test the game",6],
    ["pls test game",6],
    ["test game now",6],
    ["can you test my game",17],
    ["test my game bro",16],
    ["test my game file",23],
    ]

def Scan(Context,white,yellow,red,green,blue):
    os.system(f"title CyberWare [Scaning]")
    Info = "Scaning"
    MessageFlagLevel = 0


    print(f"""{blue}
                                ███████╗ ██████╗ █████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗          
                                ██╔════╝██╔════╝██╔══██╗████╗  ██║██║████╗  ██║██╔════╝          
                                ███████╗██║     ███████║██╔██╗ ██║██║██╔██╗ ██║██║  ███╗         
                                ╚════██║██║     ██╔══██║██║╚██╗██║██║██║╚██╗██║██║   ██║         
                                ███████║╚██████╗██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝██╗██╗██╗
                                ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝{white}""")
    print(f"{red}\n|=====================================================[{green}Scaning{red}]========================================================|\n{white}")
   
    string = ""
    import difflib
    for letter in enumerate(Context): #basic scan
        string += letter[1]

        for KeyWord in enumerate(BasicFlagedKeyWords):
            FullKeyWord = KeyWord[1]
            
            if string == FullKeyWord[0]:
                MessageFlagLevel += FullKeyWord[1]
            if FullKeyWord[0] in string:
                MessageFlagLevel += FullKeyWord[1]
  


    os.system(f"title CyberWare [Scaning]")
    print(f"\n{red}|======================================================================================================================|{white}\n[{blue}MessageFlagLevel{white}]|<{red}{math.floor(MessageFlagLevel)}{white}>\n")
    print(f"{green}[Message Info]{white}")
    print(f"\n[{blue}Message{white}]\n({green}{Context}{white}\n)\n")
    if MessageFlagLevel < 20:
        print(f"{red}This message doesnt seem to have any bad intent{white}")
    elif MessageFlagLevel < 75:
        print(f"{red}This message might be an exploiter trying to trick you \noverall this message is mostly safe but might be unsafe{white}")
    elif MessageFlagLevel < 150:
        print(f"{red}This message is very unsafe and is mosty has bad intent{white}")
    elif MessageFlagLevel < 200:
        print(f"{red}This message is trying to trick you and is not safe{white}")
    elif MessageFlagLevel < 250:
        print(f"{red}This message is not safe{white}")
    elif MessageFlagLevel > 300:
        print(f"{red}This message is a exploiter trying to do the listed below to you\nscam,hack,steal your info,steal your passwords{white}")

    print("\nPlease report any false flaging in the github\n <https://github.com/TheFakeKingIsTaken/CyberWare/issues>")
    input("\n<press anything to quit>")

    return



