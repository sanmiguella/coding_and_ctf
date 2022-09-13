#!/usr/bin/env python3
import jsbeautifier 
import argparse
import os

class Beautify:
    def __init__(self, filename, show):
        self.filename = filename
        self.show = show

    def writeToFile(self, code, outputFile):
        with open(outputFile, 'w') as f:
            f.writelines(code)

        print(f"[+] Beautified file - {outputFile}")

    def beautify(self):
        beautifiedJS = jsbeautifier.beautify_file(self.filename) 
        self.writeToFile(beautifiedJS, self.filename)

        if self.show:
            print(beautifiedJS)

class MassBeautify(Beautify):
    def __init__(self, filename, show, directory):
        super().__init__(filename, show) 
        self.directory = directory

    def beautify(self):
        for directory in self.directory:
            jsFiles = os.scandir(directory)

            for file in jsFiles:
                jsFile = file.path
                beautifiedJS = jsbeautifier.beautify_file(jsFile)
                self.writeToFile(beautifiedJS, jsFile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Beautify JS file.")     
    subParser = parser.add_subparsers(dest="command")

    singleBeautifyParser = subParser.add_parser("single", help="Beautify a single JS file.")
    singleBeautifyParser.add_argument("-f", "--filename", help="JS file to beautify.", required=True)
    singleBeautifyParser.add_argument("-s", "--show", help="Show results to stdout.", action="store_true")

    multipleBeautifyParser = subParser.add_parser("multiple", help="Beautify multiple JS file.")
    multipleBeautifyParser.add_argument("-d", "--dir", nargs='+', help="Directory containing JS files to beautify.", required=True)

    args = parser.parse_args()
    cmd = args.command

    if cmd == "single":
        beautifyFile = Beautify(args.filename, args.show) 
        beautifyFile.beautify()

    elif cmd == "multiple":
        massBeautifyFile = MassBeautify(None, None, args.dir)
        massBeautifyFile.beautify()
    
    else:
        parser.print_usage()
