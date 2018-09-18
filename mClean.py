import os
from sys import argv

def main(inpath):
    for p, d, f in os.walk(inpath):
        lastDict = p.split(os.sep)[-1]
        for file in f:
            fileName = os.path.splitext(file)[0]
            if file.endswith(".exe") and fileName == lastDict:
                filePath = os.path.join(p, file)
                if int(os.stat(filePath).st_size) == 131584:
                    print("Tespit: " + filePath)
                    os.remove(filePath)

if len(argv) == 1:
    print("Kullanim:\n\t~$ python3 {0} [path]".format(argv[0]))
    print("\nGitHub: @MuReCoder | Twitter: @MuReCoder | www.emregeldegul.net")
else:
    main(argv[1])
