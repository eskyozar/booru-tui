# Importing libaries

from pybooru import Danbooru 
import webbrowser
import time
import sys
import random

def write(write):

    for i in write:

        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.035)

# function for asciiart
def asciiart():


   

    asciiartlist = ["""\


                    ⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
                    ⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
                    ⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
                    ⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
                    ⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
                    ⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
                    ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
                    ⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
                    ⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
                    ⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
                    ⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
                    ⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
                    ⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
                    ⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
                    ⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿


                    """,

                    """\

                     _                                  
                    | |                                 
           ___  ___ | | __ _   _   ___  ____ __ _  _ __ 
          / _ \/ __|| |/ /| | | | / _ \|_  // _` || '__|
         |  __/\__ \|   < | |_| || (_) |/ /| (_| || |   
          \___||___/|_|\_\ \__, | \___//___|\__,_||_|   
                            __/ |                       
                           |___/                        

                    """,

                    """\

          ___           ___           ___           ___           ___           ___           ___           ___     
         /\  \         /\  \         /\__\         |\__\         /\  \         /\  \         /\  \         /\  \    
        /::\  \       /::\  \       /:/  /         |:|  |       /::\  \        \:\  \       /::\  \       /::\  \   
       /:/\:\  \     /:/\ \  \     /:/__/          |:|  |      /:/\:\  \        \:\  \     /:/\:\  \     /:/\:\  \  
      /::\~\:\  \   _\:\~\ \  \   /::\__\____      |:|__|__   /:/  \:\  \        \:\  \   /::\~\:\  \   /::\~\:\  \ 
     /:/\:\ \:\__\ /\ \:\ \ \__\ /:/\:::::\__\     /::::\__\ /:/__/ \:\__\ _______\:\__\ /:/\:\ \:\__\ /:/\:\ \:\__\\
     \:\~\:\ \/__/ \:\ \:\ \/__/ \/_|:|~~|~       /:/~~/~    \:\  \ /:/  / \::::::::/__/ \/__\:\/:/  / \/_|::\/:/  /
      \:\ \:\__\    \:\ \:\__\      |:|  |       /:/  /       \:\  /:/  /   \:\~~\~~          \::/  /     |:|::/  / 
       \:\ \/__/     \:\/:/  /      |:|  |       \/__/         \:\/:/  /     \:\  \           /:/  /      |:|\/__/  
        \:\__\        \::/  /       |:|  |                      \::/  /       \:\__\         /:/  /       |:|  |    
         \/__/         \/__/         \|__|                       \/__/         \/__/         \/__/         \|__|    

                    """,

                    """\

        __                                 ____     __       __             
       / /_  ____  ____  _______  __      / __/__  / /______/ /_  ___  _____
      / __ \/ __ \/ __ \/ ___/ / / /_____/ /_/ _ \/ __/ ___/ __ \/ _ \/ ___/
     / /_/ / /_/ / /_/ / /  / /_/ /_____/ __/  __/ /_/ /__/ / / /  __/ /    
    /_.___/\____/\____/_/   \__,_/     /_/  \___/\__/\___/_/ /_/\___/_/     
                                                                        
                                                                                                                                                                                                                                                        
                    """,
                    """\


                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&#@@@@@@@@&@@@@@@@@@@%&&&&/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(@&&&(((,,,,,,,,,.,((%&&&&&&#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@#&&#,%(&&&&%%%##############(&%((##@%(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@#(##&@@@@&#.,,,,,#####(/(%#########################,**,/&@@@@@@&&&@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@%%%&&&(&#&,,,/#################################%######(,,/(%@(&&&#%(@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@&#&&&&@&&%##########################(##%####(#####///#####&&&&&&&&%&@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@#&,&&&############################*%#######/##**#%#####(&&&%&&/*((/#@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@#%,,(%#%############(################*###(((((/(*//////(#####(#/*#@@//@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@&*,,,##########(########################,#####((*#*%#########%##%*/#(@%(@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@(#,,###########(######/##################*((#%*/####/%##########/##//###(@@*/(#@@@@@@@@@@
                    @@@&&#&&(@/(##############/######(###################%%//*######/######%##///(#/(#/*(/@&/(@@@@@@@@@@
                    @@@@#&&&&&&&&###(###(#####(#######################(##*&&%/#######/##(##%&#///##/*//,@@@&/(@@@@@@@@@@
                    @@@@@&(###&&(##(#####%####(#########%#############(%#(&&&&%/######/#(#####///###//(.//&%(#@@@@@@@@@@
                    @@@@@@@@%##%%##/%##(#%####(#########&################**##&&&%*####(#(######(,(//,***/#//#@@@@@@@@@@@
                    @@@@@@@@(#####(####(####%#(#########%##################&&&&&&&&#/##//####%#*//#/*#***#@(/@@@@@@@@@@@
                    @@@@@@@@######(####(######(######(#################/###&&&&&&&&&&%#/*#######/#/*##////@@/(@@@@@@@@@@
                    @@@@@@@&##&###(###########/######/#################*#(#&&&&,#%&&&&&&(#######**/(##*(*/(/*@@@@@@@@@@@
                    @@@@@@@&##&#%#(#####/#####(########################/##,      %@ #.%&(#####%(**/(##/((**%@@@@@@@@@@@@
                    @@@@@@@@##%%##(############/######(#(##############/%/%&../////. &&%(###*##*(&&/#/*#(/*(@@@@@@@@@@@@
                    @@@@@@@@(######(#####*#####(#########################/&& /// *// %&####(###&(#%&(###((//&@@@@@@@@@@@
                    @@@@@@@@#######(######/#####*######(#/############/##&&&&/&#((/.%&&(###/##(/%%%&/###/(#(#@@@@@@@@@@@
                    @@@@@@@@@/######/####(#(#####/######(#/%##########(#(&&&&&&&%&%&&&####/##/&*%(%&/###*/&/(@@@@@@@@@@@
                    @@@@@@@@@@#######/####(#(####%/######(%/########%(##&&&&&&&&&&&&&&(##(##(%/###&/(###//@/(@@@@@@@@@@@
                    @@@@@@@@@@&#######/####/%/%###########(#(##%%&&&&&&&&&&&&&&&&&&&&######&#//%&#*/(%*@//@//@@@@@@@@@@@
                    @@@@@@@@@@@%#######%,###(#(#######%%&&&&&&&&&&&&%&&&&&&&&&&&&&&&&&&&&&&&&&%%,***#/@#((@//@@@@@@@@@@@
                    @@@@@@@@@@@@@(########((###%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%*/*//***(/@@*/&&//@@@@@@@@@@@
                    @@@@@@@@@@@@@@(##(######%(%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#*/*//*,**%@@@(/@%/(@@@@@@@@@@@
                    @@@@@@@@@@@@@@@&(##/*%####(%&&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&/*/*,,@**%@@@@*/#@%(#@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@&(%(*/**((#/%&&&&&&&&&&&&&&&&&&%&&%@&&&&&&&&&&&&%/*****%@/@@@@@@&(/@@(/%@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@(#(*/*****/*%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*****%%%@@@@@@@@@@/(%@@//@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@%((/,,**/****(&&&&&&&&&&&&&&&&&&&&&&#/,*/*%@@@@@@@@@@@@@@&(*@@&((@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%*/***/./%&&&&&&&&&&&&*/%%#@###&@@@@@@@@@@@@@@//@@@(/%@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#&&&&&(#%%%#%#(/**(%#%%%%#%&&/&%@@@@@@@@@@@@/(&@@@&&@@@@@@@@@@@@@
                    @@@@@@@@@@@@@&#%&@@@@@@@@@@@@@@@@@@%&&%&&&&(#%%%%#%%#%%%%%(%&&&&%&#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@(&&&&&%&&&&%&@@@@@@@@@@@@@@@%&&&&&&&&*&&&&/%#%(&&&(&&&&&&&#@@@@@@@@&@@@@@@@@&(&&&&(#%&&&&/@@@
                    @@@@@@(&&&&&&&&&&&&&%&@@@@@@@@@@@@@@#&&&&&&&&&&&&&(%#&&&&&&&&&&&/%@@@@&##&&@@@@@@#&&&&&&&&&&&&&&#@@@
                    @@@@@@%&&&&&&&&&&&&&&(&&&#@@@@@@&%%&&&%#&&&&&&&&&&%%&&&&&&%&&&&&&&&&&&&#(%@@&#&&%%&&&&&&&&&&&&&&#@@@
                    @@@@@@@%&&&&&&&&&&&&&/&&&&&##&&&&&&&&&&&&&&&%%&&&&&&&&&&&#&&&&&&&&&&&&&&&&#(&&&&#&&&&&&&&&&&&&&#@@@@
                    @@@@@@@(&&&&&&&&&&&&&&(&&&&#(%&&&&&&&&&&&&&&%*,,,,.**&&&&&&&&&&&&&&&&&&&&##&%&&%&&&&&&&&&&&&&&#@@@@@
                    @@@@@@@@(&&&&&&&&&&&&/&&&&&%#&&&&&&&&%&&(,,,,/%&/,..,(*,,,,(&&&&&&&&&&&&##&&&&(&&&&&&&&&&&&&&%&@@@@@
                    @@@@@@@@@&%&&&&&&&&&&&(&&&&&((&&&&&&&&,,,*%&&&#,.,&,.,(&&&%(,,.#&&&&&&&(/&&&&&#&&&&&&&&&%###/@@@@@@@
                    @@@@@@@@@@@&#(&&&&&&&&&%(&&&&#(&&&&&&(,.&&&&%.,..&&#,/,*&&&&&&#,*&&&&&#(&%&&%%&&&&&#####(%@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



                    """,
                    """\

      ..                                                                      s                      .    
. uW8"                                                                       :8                     @88>  
`t888              u.          u.      .u    .      x.    .                 .88       x.    .       %8P   
 8888   .    ...ue888b   ...ue888b   .d88B :@8c   .@88k  z88u              :888ooo  .@88k  z88u      .    
 9888.z88N   888R Y888r  888R Y888r ="8888f8888r ~"8888 ^8888            -*8888888 ~"8888 ^8888    .@88u  
 9888  888E  888R I888>  888R I888>   4888>'88"    8888  888R              8888      8888  888R   ''888E` 
 9888  888E  888R I888>  888R I888>   4888> '      8888  888R              8888      8888  888R     888E  
 9888  888E  888R I888>  888R I888>   4888>        8888  888R              8888      8888  888R     888E  
 9888  888E u8888cJ888  u8888cJ888   .d888L .+     8888 ,888B . 88888888  .8888Lu=   8888 ,888B .   888E  
.8888  888"  "*888*P"    "*888*P"    ^"8888*"     "8888Y 8888"  88888888  ^%888*    "8888Y 8888"    888&  
 `%888*%"      'Y"         'Y"          "Y"        `Y"   'YP                'Y"      `Y"   'YP      R888" 
    "`                                                                                               ""   
                                                                                                          
                                                                                                          
                                                                                                          


                    """
                                           


    ]
    

    rand_index = random.randint(0,5) 

    print(asciiartlist[rand_index])


# Main booru function
def booru():

    # Client for the booru
    client = Danbooru('safebooru')

    # print(client.site_url)

    write("booru-tui is a terminal-based booru tool written by eskyozar. It uses safebooru as the client (It is below 18 content)")

    print("")
    print("")

    write("These are some example tags you can search for")


    print("")
    print("")
    write("short_hair")
    print("")
    write("blush")
    print("")
    write("looking_at_viewer")
    print("")
    print("")

    write("Enter your tags or keywords of what you want to search about:- ")

    # search for the keyword
    search = str(input(""))

    # combaining the result into one url
    result = client.site_url + "/posts?tags=" + search + "&z=2"

    # print(result)

    print("")

    write(f"Your tags or keyword are {search}")

    webbrowser.open(result)

# calling the functions

asciiart();
booru();
