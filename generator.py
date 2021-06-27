import pickle
import emotes
import re
import os
import datetime

NUMBER_OF_RANKINGS = 25

def load_dictionary(filename):
    with open(filename, 'rb') as d:
        return pickle.load(d)

def parse_macro(emote, dictionary, macro):
    macro = macro[len('!!!'):][:-len('!!!')]
    if (macro == 'EMOTE_NAME'):
        return emote
    elif (macro == 'EMOTE_URL'):
        return emotes.getEmoteURL(emote)
    elif (macro == 'GENERATION_DATE'):
        return str(datetime.datetime.today())
    elif (macro.startswith('USERNAME')):
        rank = int(macro[len('USERNAME'):])
        emote_dict = dictionary[emote]
        return getRankings(emote_dict, NUMBER_OF_RANKINGS)[rank - 1]
    elif (macro.startswith('USERCOUNT')):
        rank = int(macro[len('USERCOUNT'):])
        emote_dict = dictionary[emote]
        rankings = getRankings(emote_dict, NUMBER_OF_RANKINGS)
        return str(emote_dict[rankings[rank - 1]])
    elif (macro.startswith('MAINENTRY')):
        return parse_main_entry(macro, dictionary)
    else:
        return macro

def getRankings(emote_dict, n):
    #https://stackoverflow.com/questions/7197315/5-maximum-values-in-a-python-dictionary
    return sorted(emote_dict, key=emote_dict.get, reverse=True)[:n]

def parse_main_entry(macro, dictionary):
    emote = macro[len('MAINENTRY_'):]
    return generate_main_entry(emote, dictionary)

def generate_main_entry(emote, dictionary):
    main_entry = ''
    with open('main_template_entry.html', 'r', encoding='utf-8') as t:
        tlines = t.readlines()
        for tline in tlines:
            print(tline)
            macros = re.findall('!!!\w+!!!', tline)
            line = tline
            for macro in macros:
                line = line.replace(macro, parse_macro(emote, dictionary, macro))
            main_entry += line
    return main_entry


def generate_emote_page(emote, dictionary, template, output):
    """Generates a page for the given emote based off the given template and saved to the given output"""
    filename = output + emote + '.html'
    if (not os.path.isfile(filename)):
        f = open(filename, 'x', encoding='utf-8')
        f.close()

    rankings = getRankings(dictionary[emote], NUMBER_OF_RANKINGS)
    with open(filename, 'w', encoding='utf-8') as f:
        with open(template, 'r', encoding='utf-8') as t:
            tlines = t.readlines()
            for tline in tlines:
                macros = re.findall('!!!\w+!!!', tline)
                fline = tline
                for macro in macros:
                    fline = fline.replace(macro, parse_macro(emote, dictionary, macro))
                f.write(fline)

def generate_main_page(emotes, dictionary, template, output):
    """Generates a page for the given emote based off the given template and saved to the given output"""
    filename = output + 'index.html'
    if (not os.path.isfile(filename)):
        f = open(filename, 'x', encoding='utf-8')
        f.close()

    with open(filename, 'w', encoding='utf-8') as f:
        with open(template, 'r', encoding='utf-8') as t:
            tlines = t.readlines()
            for tline in tlines:
                print(tline)
                macros = re.findall('!!!\w+!!!', tline)
                fline = tline
                for macro in macros:
                    fline = fline.replace(macro, parse_macro('Abathur', dictionary, macro))
                f.write(fline)


dictionary = load_dictionary('dictionary.bin')
for emote in emotes.emoteFileName.keys():
    generate_emote_page(emote, dictionary, 'emote_template.html', 'generated/')

generate_main_page(emotes.emoteFileName.keys(), dictionary, 'main_template.html', 'generated/')