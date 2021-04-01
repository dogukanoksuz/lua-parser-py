'''

DOGUKAN.DEV NPCDATA.LUA PARSER

TXT'YE EXPORT ALMAK İÇİN:
python main.py <NPCData.lua> <Output Alacağınız Txt Adı> export

TXT'DEN YENİ BİR LUA OLUŞTURMAK İÇİN:
python main.py <NPCData.lua> <Output Txtnizin Adı> import <Final.lua>

'''

import sys
import os.path

f = open(sys.argv[1], "r")
lines = f.readlines()
f.close()

if (sys.argv[3] == "export"):
    textlines = []

    for line in lines:
        if ".   .   .   ." in line or "_" in line or "Unlock" in line:
            continue
        if line.startswith("					Text =") or line.startswith("   					Text =") or line.startswith("						Text =") or line.startswith("					Text ="):
            myline = line.strip().replace('Text = "', '')
            strwithoutlastchar = myline[:-1]
            if (myline[-1] == ','):
                strwithoutlastchar = myline[:-2]
            textlines.append(strwithoutlastchar + '\n')
    
    w = open(sys.argv[2], "w+")
    w.writelines(textlines)
    w.close()

if (sys.argv[3] == "import"):
    x = open(sys.argv[2], "r")
    translated = x.readlines()
    x.close()

    i = 0
    for a, line in enumerate(lines):
        if ".   .   .   ." in line or "_" in line or "Unlock" in line:
            continue
        if line.startswith("					Text =") or line.startswith("   					Text =") or line.startswith("						Text =") or line.startswith("					Text ="):
            lines[a] = '					Text = "' + translated[i].strip() + ' ", \n'
            i = i+1

    y = open(sys.argv[4], "w+")
    y.writelines(lines)
    y.close()
