import urllib.parse

path = "./sh.ps1"
file = open(path, "r")

maxOutchar = 100
outLine = ""
output = ""
outFile = "./a.txt"
urlConvert = True
prepend = "@echo "
append = " >> c:\\Users\\merlin\\AppData\\Local\\Temp\\vmware-merlin\\VMwareDnD\\d7c161a1\\UploadedFiles\\sodomak\\shell.ps1" #TODO: Add bckslashes on input
append1st = " > c:\\Users\\merlin\\AppData\\Local\\Temp\\vmware-merlin\\VMwareDnD\\d7c161a1\\UploadedFiles\\sodomak\\shell.ps1"
urlConverAll = True
"""
if urlConverAll:
    prepend = urllib.parse.quote_plus(prepend)
    append = urllib.parse.quote_plus(append)
"""

with file as f:

    for line in f:
        chunksNr = (len(line)//maxOutchar)+1
        i = 0
        j = 1
        eol = ""
        for chunks in range(0,chunksNr):
            if j == chunksNr:
                eol = "\n"
            if firstLine:
                outLine = prepend + line[i+chunks:(i+chunks)+maxOutchar+1].rstrip() + eol + append1st
            else:	
                outLine = prepend + line[i+chunks:(i+chunks)+maxOutchar+1].rstrip() + eol + append
            firstLine = False
            if urlConverAll:
                outLine = urllib.parse.quote_plus(outLine)
 #           print(outLine)
            j += 1
            i +=maxOutchar
            outLine += "\n"

            output += outLine

with open(outFile, 'a') as out:
    out.write(output)


# TODO: Add all txt's in the path
