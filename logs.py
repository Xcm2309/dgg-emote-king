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
    """
    Checks if the given string, line, is a valid DGG chat message.
    """
    validRE = '^\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} UTC\] \w+:'
    if re.match(validRE, line):
        return True
    else:
        return False

def isValidDGGLog(log):
    """
    Checks if the given string, log, is a valid DGG log.
    """
    lines = log.splitlines()
    # If the last line isn't valid something probably went wrong
    return isValidDGGLine(lines[len(lines) - 1])

def getLogURL(year, month, day):
    """
    Return the URL of a DGG chatlog for a given year, month, and day.
    """
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

def getLog(year, month, day):
    """
    Sends an HTML request for the DGG chatlog for a given year, month, and day.
    """
    print("Retrieving logs for " + calendar.month_name[month] + ' ' + str(day) + ', ' + str(year))
    URL = getLogURL(year, month, day)
    r = requests.get(URL)

    if (r.status_code == 200):
        return r.text
    else:
        print('Failed to get URL: ' + URL)
        return ''

def getUsername(line):
    """
    Given a valid DGG chat line returns the username of the message.
    """
    i = TIMESTAMP_LEN
    while (line[i] != ':'):
        i += 1

    return line[:i][TIMESTAMP_LEN:]

def getMessage(line):
    """
    Given a valid DGG chat line returns the content of the message.
    """
    i = TIMESTAMP_LEN
    while (line[i] != ':'):
        i += 1

    # add 2 to not include colon and space
    return line[i + 2:]

def findOccurances(start_date, patterns):
    """
    Creates a dictionary for each pattern that relates a username to the
    number of occurances of that pattern since start_date and then saves
    that dictionary as 'dictionary.bin'
    """
    current_date = start_date
    today = datetime.date.today()
    day = datetime.timedelta(days=1)

    emote_dict = {}
    while (current_date <= today):
        log = getLog(current_date.year, current_date.month, current_date.day)
        while (not isValidDGGLog(log)):
            print("Invalid Log, Retrying...")
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

findOccurances(datetime.date(2021, 6, 1), emotes.emoteFileName.keys())
abathur = pickle.load(open('dictionary.bin', 'rb'))
print(abathur['Abathur']['TheChadLinker'])