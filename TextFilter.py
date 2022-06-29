from FileManager import FileManager


class TextFilter:

    def __init__(self, RawFile, OutFile):
        self.OutFile = OutFile
        self.File = open(RawFile)

    def ProcessData(self):
        TotalLines = 0
        OutFileManager = FileManager('', 'filtered-creds.csv')
        FileWriter = OutFileManager.WriteFile()
        lines = self.File.readlines()
        for line in lines:
            if TotalLines < 758:
                splits = line.split(':')
                if len(splits) == 2:
                    FileWriter.writerow({'Username': splits[0], 'Password': splits[1].strip('\n')})
                elif len(splits) == 3 and 'Telegram' not in line:
                    password = ':'.join(splits[1:])
                    FileWriter.writerow({'Username': splits[0], 'Password': password.strip('\n')})
                TotalLines += 1
