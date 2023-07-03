import os
import MessageScan.BasicScan as BasicScan



def Menu(white,yellow,red,green,blue):
    while True:
        os.system("cls")
        print(f"""{blue}
███╗   ███╗███████╗███████╗███████╗ █████╗  ██████╗ ███████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███████╗██████╗ 
████╗ ████║██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝ ██╔════╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
██╔████╔██║█████╗  ███████╗███████╗███████║██║  ███╗█████╗      ███████╗██║     ███████║██╔██╗ ██║█████╗  ██████╔╝
██║╚██╔╝██║██╔══╝  ╚════██║╚════██║██╔══██║██║   ██║██╔══╝      ╚════██║██║     ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║███████╗███████║███████║██║  ██║╚██████╔╝███████╗    ███████║╚██████╗██║  ██║██║ ╚████║███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝{white}

{red}|======================================================[{green}Main Commands{red}]=================================================|{white}

        <{blue}1{white}>{yellow}Basic Message Scaning{red}(not recommended){white}

        <{blue}2{white}>{yellow}Normal Message Scaning{green}(recommended){white}|Not Here Yet!|

        <{blue}3{white}>{yellow}Advanced Message Scaning{white} |Not Here Yet!|

        <{green}back{white}>{yellow}Goes back to MainMenu{white}

{red}|======================================================================================================================|{white}
""")

        UserInput = input(f"<{green}User{white}>")
        if UserInput == "back":
            return
        if UserInput == "1":
            print(f"""\n
{red}|======================================================================================================================|{white}

{blue}
                                ███████╗ ██████╗ █████╗ ███╗   ██╗███████╗██████╗ 
                                ██╔════╝██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
                                ███████╗██║     ███████║██╔██╗ ██║█████╗  ██████╔╝
                                ╚════██║██║     ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
                                ███████║╚██████╗██║  ██║██║ ╚████║███████╗██║  ██║
                                ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

                                                                    
{red}|===========================================[{green}Input The Message To Scan{red}]================================================|

                  {white}""")
            Context = ""
            print(f"{red}[Enter 'done' to start scaning your message]:{green}(Enter back to go back to menu){white}")

            run = True
            while run:
                Message = input("")
                if Message == "done":
                    run = False
                elif Message == "back":
                    run = None
                else:
                    Context += "\n" + Message 
                

            if run == False:
                os.system("cls")
                BasicScan.Scan(Context,white,yellow,red,green,blue)

        if UserInput == "2":
            print(f"{green}This option is comeing soon")
            input()
        if UserInput == "3":
            print(f"{green}This option is comeing soon")
            input()