import datetime
import calendar
import os
import requests
import re
import pickle
import emotes

# Add one for space
TIMESTAMP_LEN = len('[2309-04-27 04:20:69 UTC]') + 1

def isValidDGGLine(line):
    strlen = len(line)
    if strlen <= TIMESTAMP_LEN:
        return False

    i = TIMESTAMP_LEN
    while (i < strlen and line[i] != ':'):
        i += 1

    return i < strlen

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

def downloadLog(year, month, day, output):
    """Downloads a DGG logs to logs/<year>-<month>-<day> for a given year, month, and day"""
    filename = output + str(year) + '-' + str(month) + '-' + str(day) + '.txt'
    if (not os.path.isfile(filename)):
        print("Retrieving logs for " + calendar.month_name[month] + ' ' + str(day) + ', ' + str(year))
        URL = getLogURL(year, month, day)
        r = requests.get(URL)

        if (r.status_code == 200):
            f = open(filename, 'x', encoding='utf-8')
            f.write(r.text)
            f.close()
        else:
            print('Failed to get URL: ' + URL)

def getLog(year, month, day):
    print("Retrieving logs for " + calendar.month_name[month] + ' ' + str(day) + ', ' + str(year))
    URL = getLogURL(year, month, day)
    r = requests.get(URL)

    if (r.status_code == 200):
        return r.text
    else:
        print('Failed to get URL: ' + URL)
        return ''

def createLogsDirectory(start_date, output):
    """Creates logs directory if not already there and downloads all DGG logs from start_date to today"""
    current_date = start_date
    today = datetime.date.today()
    day = datetime.timedelta(days=1)

    if (not os.path.isdir('logs')):
        os.mkdir('logs')

    while (current_date <= today):
        downloadLog(current_date.year, current_date.month, current_date.day, output)
        current_date += day

def getUsername(line):
    """Given a valid DGG chat line returns the username of the message"""
    i = TIMESTAMP_LEN
    while (line[i] != ':'):
        i += 1

    return line[:i][TIMESTAMP_LEN:]

def getMessage(line):
    """Given a valid DGG chat line returns the content of the message"""
    i = TIMESTAMP_LEN
    while (line[i] != ':'):
        i += 1

    # add 2 to not include colon and space
    return line[i + 2:]

def findOccurances(start_date, patterns):
    current_date = start_date
    today = datetime.date.today()
    day = datetime.timedelta(days=1)

    emote_dict = {}
    while (current_date <= today):
        log = getLog(current_date.year, current_date.month, current_date.day)
        lines = log.splitlines()

        for line in lines:
            if (isValidDGGLine(line)):
                username = getUsername(line)
                message = getMessage(line)

                for pattern in patterns:
                    matches = re.findall(pattern, message)

                    if pattern in emote_dict:
                        if username in emote_dict[pattern]:
                            emote_dict[pattern][username] += len(matches)
                        else:
                            emote_dict[pattern][username] = len(matches)
                    else:
                        emote_dict[pattern] = {}
                        emote_dict[pattern][username] = len(matches)
            else:
                print('Invalid line: ' + line)

        current_date += day

    if (not os.path.isfile('dictionary.bin')):
        f = open('dictionary.bin', 'x')
        f.close()

    with open('dictionary.bin', 'wb') as f:
        pickle.dump(emote_dict, f)

'''
createLogsDirectory(datetime.date(2021, 1, 1), 'logs/')
print(getUsername('[2021-06-26 22:11:21 UTC] FunkPhysics: SOY Clap'))
print(getMessage('[2021-06-26 22:11:21 UTC] FunkPhysics: SOY Clap'))

for emote in emotes.emoteFileNameTest:
    print(emote + ': ' + str(findOccurances(datetime.date(2021, 1, 5), emote)))
'''
findOccurances(datetime.date(2021, 6, 1), emotes.emoteFileNameTest.keys())
abathur = pickle.load(open('dictionary.bin', 'rb'))
print(abathur['Abathur']['TheChadLinker'])