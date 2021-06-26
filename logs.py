import datetime
import calendar
import os
import requests
import re
import emotes

# Add one for space
TIMESTAMP_LEN = len('[2309-04-27 04:20:69 UTC]') + 1

def getLogURL(year, month, day):
    """Return the URL of a DGG chatlog for a given year, month, and day"""
    URL = 'https://overrustlelogs.net/Destinygg%20chatlog/'
    URL += calendar.month_name[month]
    URL += '%20'
    URL += str(year)
    URL += '/'
    URL += str(year)
    URL += '-'
    URL += str(month).zfill(2)
    URL += '-'
    URL += str(day).zfill(2)
    URL += '.txt'
    return URL

def createLogsDirectory(start_date):
    """Creates logs directory if not already there and downloads all DGG logs from start_date to today"""
    current_date = start_date
    today = datetime.date.today()
    day = datetime.timedelta(days=1)

    if (not os.path.isdir('logs')):
        os.mkdir('logs')

    while (current_date <= today):
        filename = 'logs/' + str(current_date.year) + '-' + str(current_date.month) + '-' + str(current_date.day) + '.txt'
        if (not os.path.isfile(filename)):
            print("Retrieving logs for " + calendar.month_name[current_date.month] + ' ' + str(current_date.day) + ', ' + str(current_date.year))
            URL = getLogURL(current_date.year, current_date.month, current_date.day)
            r = requests.get(URL)

            if (r.status_code == 200):
                f = open(filename, 'x', encoding='utf-8')
                f.write(r.text)
                f.close()
            else:
                print('Failed to get URL: ' + URL)

        current_date += day

def getUsername(line):
    """Given a DGG chat line returns the username of the message"""
    i = TIMESTAMP_LEN

    while (line[i] != ':'):
        i += 1

    return line[:i][TIMESTAMP_LEN:]

def getMessage(line):
    """Given a DGG chat line returns the content of the message"""
    i = TIMESTAMP_LEN

    while (line[i] != ':'):
        i += 1

    # add 2 to not include colon and space
    return line[i + 2:]

def findOccurances(start_date, match):
    current_date = start_date
    today = datetime.date.today()
    day = datetime.timedelta(days=1)

    total_matches = 0
    while (current_date <= today):
        filename = 'logs/' + str(current_date.year) + '-' + str(current_date.month) + '-' + str(current_date.day) + '.txt'
        if (os.path.isfile(filename)):
            f = open(filename, 'r', encoding='utf-8')
            lines = f.readlines()

            for line in lines:
                matches = re.findall(match, line)
                total_matches += len(matches)

        current_date += day
    return(total_matches)

createLogsDirectory(datetime.date(2021, 1, 1))
print(getUsername('[2021-06-26 22:11:21 UTC] FunkPhysics: SOY Clap'))
print(getMessage('[2021-06-26 22:11:21 UTC] FunkPhysics: SOY Clap'))

for emote in emotes.emoteFileNameTest:
    print(emote + ': ' + str(findOccurances(datetime.date(2021, 1, 1), emote)))