import urllib.parse

path = "./test.txt"
file = open(path, "r")

maxOutchar = 6
outLine = ""
output = ""
outFile = "./out.txt"
urlConvert = True
prepend = "echo "
append = " >> test.ps1"
urlConverAll = True
firstLine = True # TODO: Different first line >
"""
if urlConverAll:
    prepend = urllib.parse.quote_plus(prepend)
    append = urllib.parse.quote_plus(append)
"""

with file as f:

    for line in f:
#        print("line: " + line)
        chunksNr = (len(line)//maxOutchar)+1
        i = 0
        j = 1
        eol = ""
        for chunks in range(0,chunksNr):
            if j == chunksNr:
                eol = "\\n"
            outLine = prepend + line[i+chunks:(i+chunks)+maxOutchar+1].rstrip() + eol + append
            if urlConverAll:
                outLine = urllib.parse.quote_plus(outLine)
            print(outLine)
            j += 1
            i +=maxOutchar
            outLine += "\n"

            output += outLine
 #           print("Chunk: ")

with open(outFile, 'a') as out:
    out.write(output)

print((10//4)+1)
