import csv
import os


class FileManager:

    def __init__(self, InFileName, OutFileName):
        self.InFileName = InFileName
        self.OutFileName = OutFileName

    def ReadFile(self):
        if os.stat(self.InFileName).st_size == 0:
            raise Exception("Input File is Empty")
        else:
            data = open(self.InFileName, 'r')
            fReader = csv.reader(data)
            next(fReader)
            return fReader

    # Code to Append IDs to Old File
    # def WriteFile(self):
    #     header = ["Username", "Password"]
    #     if os.stat(self.OutFileName).st_size == 0:
    #         file = open(self.OutFileName, 'w', encoding='UTF8', newline='')
    #         fWriter = csv.DictWriter(file, fieldnames=header)
    #         fWriter.writeheader()
    #     else:
    #         file = open(self.OutFileName, 'a', encoding='UTF8', newline='')
    #         fWriter = csv.DictWriter(file, fieldnames=header)
    #     return fWriter

    # Code to delete all data on every run and rewrite
    def WriteFile(self):
        header = ["Username", "Password"]
        file = open(self.OutFileName, 'w', encoding='UTF8', newline='')
        fWriter = csv.DictWriter(file, fieldnames=header)
        fWriter.writeheader()
        return fWriter
